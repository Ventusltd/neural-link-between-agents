"""Bounded negative controls, using only this pilot directory."""
import builtins
import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('pilot',HERE/'furnace_pilot.py')
pilot=importlib.util.module_from_spec(spec); spec.loader.exec_module(pilot)

class NegativeControls(unittest.TestCase):
    def invoke(self, *args):
        with tempfile.TemporaryDirectory(dir=HERE) as work:
            path=Path(work)/'receipt.json'
            with patch.object(sys,'argv',['pilot','--output',str(path),*args]),contextlib.redirect_stdout(io.StringIO()):
                code=pilot.main()
            raw=path.read_text(); receipt=json.loads(raw)
            self.assertNotIn(str(HERE),raw)
            self.assertNotIn('C:\\',raw)
            self.assertEqual(receipt['script_sha256'],hashlib.sha256((HERE/'furnace_pilot.py').read_bytes()).hexdigest())
            return code,receipt

    def test_cases_over_cap_fail_closed(self):
        code,r=self.invoke('--cases','262145')
        self.assertEqual(code,1); self.assertFalse(r['accepted'])

    def test_zero_repeats_rejected(self):
        code,r=self.invoke('--repeats','0')
        self.assertEqual(code,1); self.assertFalse(r['accepted'])

    def test_source_mutation_rejected_before_execution(self):
        original=Path.read_bytes
        def mutated(path):
            raw=original(path)
            return raw+b'\nraise Exception("must never execute")\n' if path.name=='prospecting.source' else raw
        with patch.object(Path,'read_bytes',mutated):
            with self.assertRaisesRegex(ValueError,'verification_failed'):
                pilot.producer()

    def test_missing_gpu_never_passes(self):
        original=builtins.__import__
        def no_gpu(name,*args,**kwargs):
            if name=='cupy': raise ImportError('synthetic_unavailable')
            return original(name,*args,**kwargs)
        with patch('builtins.__import__',no_gpu):
            code,r=self.invoke('--cases','32')
        self.assertEqual(code,1); self.assertFalse(r['accepted']); self.assertEqual(r['status'],'gpu_unavailable')

    def test_deterministic_seed_and_inputs(self):
        code,a=self.invoke('--cases','69','--repeats','1')
        other,b=self.invoke('--cases','69','--repeats','1')
        self.assertEqual((code,other),(0,0))
        self.assertEqual(a['input_sha256'],b['input_sha256'])
        self.assertEqual(a['unique_numeric_feature_cases'],b['unique_numeric_feature_cases'])

    def test_injected_gpu_failure_rejects_receipt(self):
        code,r=self.invoke('--cases','32','--inject-failure')
        self.assertEqual(code,1); self.assertFalse(r['accepted']); self.assertEqual(r['status'],'failed')
        self.assertEqual(r['mismatches'],1); self.assertEqual(r['maximum_absolute_error_hundredths'],1)

if __name__=='__main__':
    unittest.main()
