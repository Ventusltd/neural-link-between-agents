"""Offline bounded synthetic-input replay of pinned prospecting score arithmetic.

CPU performs producer feature extraction. GPU adds integer hundredths and sorts.
No source acquisition, real-corpus parity, news parser or publication certification.
"""
import argparse
import ast
import datetime
import hashlib
import json
import math
import os
from pathlib import Path
import re
import statistics
import time
import types
import warnings

PINS = {'relevance': '8be79d5e5048b79eae425f14f749cfa439a03774c2c27fb0b1309aca3b953f43',
        'prospecting': '23c2c054a1d55b07e60af513709071476bdc6202dbf0e8b4ec87b23cf59ddf73'}
SOURCE_COMMIT = '0cb4f71e948df23e2985f189a5a1d77e88d332b2'
KERNEL = r'''
extern "C" __global__ void score(const int* x, int n, int* out) {
 int i=blockDim.x*blockIdx.x+threadIdx.x;
 if(i>=n) return;
 int s=x[i*4]+x[i*4+1]+1500;
 if(x[i*4+2]) s+=800;
 if(x[i*4+3]) s+=500;
 out[i]=s;
}
'''

def require(ok):
    if not ok:
        raise ValueError('verification_failed')

def producer():
    """Run only an explicit AST subset from SHA-pinned local producer sources."""
    env = {'math': math, 're': re, 'date': datetime.date}
    selected = {
        'relevance': {'_c', 'capacity_component', 'technology_component',
                      'national_route_component', 'evidence_component'},
        'prospecting': {'official_candidate', 'capacity', 'require', 'component',
                        'text', 'research_policy_fields', 'freshness'}}
    for name in ('relevance', 'prospecting'):
        raw = Path(__file__).with_name(name + '.source').read_bytes()
        require(hashlib.sha256(raw).hexdigest() == PINS[name])
        tree = ast.parse(raw)
        nodes = []
        for node in tree.body:
            if name == 'relevance' and isinstance(node, ast.Assign):
                if any(isinstance(t, ast.Name) and t.id in {'PROFILE_ID', 'DEFAULT_PROFILE'} for t in node.targets):
                    nodes.append(node)
            if isinstance(node, ast.FunctionDef) and node.name in selected[name]:
                nodes.append(node)
        local = dict(env)
        exec(compile(ast.Module(body=nodes, type_ignores=[]), '<pinned-producer-subset>', 'exec'), local)
        if name == 'relevance':
            env['relevance'] = types.SimpleNamespace(**{k: local[k] for k in selected[name]})
        else:
            return local['official_candidate'], env['relevance']

def write_receipt(path, receipt):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + '.tmp')
    temp.write_text(json.dumps(receipt, indent=2, sort_keys=True, allow_nan=False) + '\n', encoding='utf-8')
    os.replace(temp, path)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--cases', type=int, default=65536)
    parser.add_argument('--repeats', type=int, default=3)
    parser.add_argument('--seed', type=int, default=20261116)
    parser.add_argument('--inject-failure', action='store_true', help='Deliberately corrupt GPU score; must exit 1 with rejected receipt')
    args = parser.parse_args()
    receipt = dict(schema='furnace.prospecting-numeric-pilot.v1', accepted=False,
                   status='running', source_commit=SOURCE_COMMIT, source_sha256=PINS,
                   script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                   production_enabled=False, synthetic_inputs=True,
                   scope='Pinned official_candidate score and ID ordering on synthetic rows; CPU feature extraction; no real-corpus, news, provenance, rights, browser or publication acceptance',
                   seed=args.seed, requested_cases=args.cases, repeats=args.repeats,
                   deliberate_failure_requested=args.inject_failure, tolerance_hundredths=0,
                   ordering_validation='Both GPU scoring channels share CuPy lexsort; independent Python string-key oracle witnesses every rank')
    write_receipt(args.output, receipt)
    started = time.perf_counter()
    phase = 'input_validation'
    try:
        require(32 <= args.cases <= 262144 and 1 <= args.repeats <= 10 and 0 <= args.seed <= 2**32-1)
        import numpy as np
        oracle, relevance = producer()
        rng = np.random.default_rng(args.seed)
        n = args.cases
        # Independent synthetic records, not copies of any live/source project.
        mw = rng.uniform(0, 2000, n)
        known = rng.integers(0, 2, n, dtype=np.int32)
        tech_idx = rng.integers(0, 6, n, dtype=np.int32)
        route = rng.integers(0, 2, n, dtype=np.int32)
        age = rng.integers(-1, 60, (n, 2), dtype=np.int32)
        # Explicit zero/unknown/cap boundary + inclusive freshness windows + tied IDs.
        caps = [None, 0., 999., 998.999999, 999.000001, 1e-12, 1e9, 0., 0., 0., 0., 0.]
        for i, v in enumerate(caps):
            mw[i] = v or 0.; known[i] = int(v is not None)
        tech_idx[:12] = 0; route[:12] = 0
        age[:12] = [[-1,-1],[-1,-1],[30,14],[31,14],[30,15],[0,0],[-1,0],[30,14],[30,15],[-1,-1],[0,-1],[31,15]]
        techs = [None, 'Solar Photovoltaics', 'Battery', 'Wind Onshore', 'Hydrogen', 'Unknown technology']
        features = np.empty((n,4), np.int32)
        expected = np.empty(n, np.int32)
        extraction_start = time.perf_counter()
        for i in range(n):
            capacity = float(mw[i]) if known[i] else None
            tech = techs[int(tech_idx[i])]
            authority = 'Scottish Government (S36)' if route[i] else None
            a, b = (int(v) for v in age[i])
            fresh = a >= 0 and b >= 0 and a <= 30 and b <= 14
            article = {'freshness': {'state': 'WITHIN_WINDOW' if 0 <= a <= 30 else 'UNKNOWN' if a < 0 else 'STALE'},
                       'retrieval_freshness': {'state': 'WITHIN_WINDOW' if 0 <= b <= 14 else 'UNKNOWN' if b < 0 else 'STALE'}}
            row = dict(capacity_mw=capacity, capacity_known=bool(known[i]), repd_ref=str(i+1),
                       repd_technology=tech, planning_authority=authority, name=None, country=None,
                       technology=tech, status=None, repd_record_updated=None)
            actual = oracle(row, {}, {'articles':[article]}, None)
            expected[i] = round(actual['score']*100)
            features[i] = [round(relevance.capacity_component(capacity)['points']*100),
                           round(relevance.technology_component(tech)['points']*100), int(route[i]), int(fresh)]
            require(actual['heat']['state'] == 'UNKNOWN' and actual['heat']['score'] == 0)
        extraction_seconds = time.perf_counter()-extraction_start
        # Rank IDs exactly as producer string ordering (e.g. REPD-10 before REPD-2).
        ids = ['REPD-'+str(i+1) for i in range(n)]
        string_order = sorted(range(n), key=ids.__getitem__)
        id_key = np.empty(n, np.int32)
        id_key[string_order] = np.arange(n, dtype=np.int32)
        oracle_order = np.asarray(sorted(range(n), key=lambda i: (-int(expected[i]), ids[i])), dtype=np.int64)
        require(expected[0] == expected[1] == 1500 and known[0] != known[1])
        require(expected[2] == 5000 and expected[3] == 4500 and expected[4] == 4500)
        require(expected[7] == 2000 and expected[8] == 1500)
        input_hash = hashlib.sha256()
        for x in (mw,known,tech_idx,route,age,features,id_key):
            input_hash.update(str(x.dtype).encode()); input_hash.update(str(x.shape).encode()); input_hash.update(x.tobytes())
        receipt.update(input_sha256=input_hash.hexdigest(), processed_rows=n,
                       unique_source_feature_cases=int(np.unique(np.column_stack((np.where(known,mw,-1),known,tech_idx,route,age)),axis=0).shape[0]),
                       unique_numeric_feature_cases=int(np.unique(features,axis=0).shape[0]),
                       boundary_fixture_rows=12, cpu_oracle_rows=n,
                       cpu_feature_extraction_and_producer_oracle_seconds=extraction_seconds,
                       unknown_capacity_rows=int((known==0).sum()), known_zero_capacity_rows=int(((known==1)&(mw==0)).sum()),
                       array_memory_conservative_bound_bytes=512*n, array_memory_limit_bytes=256*1024*1024,
                       maximum_cases=262144, channels=['raw CUDA integer branches','CuPy independent expression graph'],
                       cpu_oracle='SHA-pinned official_candidate AST subset', integer_score_unit='hundredth point')
        phase = 'gpu_initialization'
        warnings.filterwarnings('ignore', message='CUDA path could not be detected.*', category=UserWarning)
        import cupy as cp
        cp.get_default_memory_pool().set_limit(size=128*1024*1024)
        require(cp.cuda.runtime.getDeviceCount() > 0)
        kernel = cp.RawKernel(KERNEL, 'score')
        def gpu(channel):
            x=cp.asarray(features); key=cp.asarray(id_key)
            if channel == 'raw':
                score=cp.empty(n, dtype=cp.int32)
                kernel(((n+255)//256,), (256,), (x,np.int32(n),score))
            else:
                score = cp.sum(cp.stack((x[:,0], x[:,1], cp.full(n,1500,dtype=cp.int32), x[:,2]*800, x[:,3]*500)),axis=0,dtype=cp.int32)
            if args.inject_failure:
                score[0] += 1
            order=cp.lexsort(cp.stack((key,-score)))
            result=(cp.asnumpy(score),cp.asnumpy(order))
            cp.cuda.Stream.null.synchronize()
            return result
        def cpu():
            x=features
            s=x[:,0]+x[:,1]+1500+800*x[:,2]+500*x[:,3]
            return s,np.lexsort((id_key,-s))
        warm_start=time.perf_counter()
        phase='gpu_compilation_and_warmup'
        for ch in ('raw','graph'):
            s,o=gpu(ch)
            receipt['mismatches']=int(np.count_nonzero(s!=expected))
            receipt['maximum_absolute_error_hundredths']=int(np.max(np.abs(s-expected)))
            require(np.array_equal(s,expected) and np.array_equal(o,oracle_order))
        receipt['gpu_warmup_compile_seconds']=time.perf_counter()-warm_start
        phase='paired_verification'
        timings={'cpu_numpy':[],'raw':[],'graph':[]}
        max_error=0
        for _ in range(args.repeats):
            for ch in timings:
                cp.cuda.Stream.null.synchronize()
                tick=time.perf_counter(); s,o=cpu() if ch=='cpu_numpy' else gpu(ch)
                elapsed=time.perf_counter()-tick
                timings[ch].append(elapsed)
                max_error=max(max_error,int(np.max(np.abs(s-expected))))
                require(np.array_equal(s,expected) and np.array_equal(o,oracle_order))
        broken_device=cp.asarray(s); broken_device[0]+=1
        broken=cp.asnumpy(broken_device)
        witness=np.flatnonzero(broken!=expected)
        require(witness.tolist()==[0])
        broken_order=oracle_order.copy(); broken_order[:2]=broken_order[:2][::-1]
        require(not np.array_equal(broken_order,oracle_order))
        receipt.update(accepted=True,status='passed', device=cp.cuda.runtime.getDeviceProperties(0)['name'].decode(),
                       cupy_version=cp.__version__,numpy_version=np.__version__,
                       cuda_runtime=cp.cuda.runtime.runtimeGetVersion(),
                       maximum_absolute_error_hundredths=max_error,mismatches=0,
                       injected_score_error_detected=True,injected_score_error_witness_row=0,
                       injected_error_channel='CuPy graph output copied to GPU then incremented by one hundredth',
                       injected_order_error_detected=True,
                       gpu_warmup_executions=2, repeated_gpu_executions=2*args.repeats,
                       repeated_gpu_row_evaluations=n*2*args.repeats,
                       timings_seconds=timings,median_seconds={k:statistics.median(v) for k,v in timings.items()},
                       timing_scope='Warm scoring+full ordering; GPU synchronized H2D+D2H included; extraction/oracle and compilation excluded and separately reported',
                       gpu_pool_reserved_bytes=cp.get_default_memory_pool().total_bytes(),
                       actual_producer_parity_scope='Synthetic official_candidate scores only; CPU pre-extracted rounded capacity, technology, route/freshness; full producer validation and real inputs not tested')
    except Exception as exc:
        receipt.update(accepted=False,status='gpu_unavailable' if phase=='gpu_initialization' else 'failed',
                       failure_phase=phase,error_type=type(exc).__name__)
    receipt['whole_seconds']=time.perf_counter()-started
    write_receipt(args.output,receipt)
    print(json.dumps({'accepted':receipt['accepted'],'status':receipt['status']}))
    return 0 if receipt['accepted'] else 1

if __name__=='__main__':
    raise SystemExit(main())
