"""SATNAV-05: replay existing mock lifecycle test on pinned inputs.
Usage: python privacy_runner.py APP TEST RECEIPT
Obtain APP and TEST from the immutable GitHub links in the accompanying receipt.
No network, no dependency installation, no product writes. Node 22 required.
Interrupted runs retain the last completed stage; rerun from the start.
"""
import hashlib
import json
import pathlib
import re
import subprocess
import sys
import tempfile
import time

PINS = ('9ae118926d62b1bc8741ae73235e79a9e29378d1',
        'ffed1b7e523aff3cc0c448646f15a50deb3cb6a6')


def blob(data):
    return hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()


def run(app, test, output):
    report = {'status': 'IN_PROGRESS', 'stages': [], 'runs': [],
              'scope': 'mock DOM/geolocation; stubbed place and compass; not handset or browser acceptance'}
    def save():
        tmp = output.with_suffix(output.suffix + '.tmp')
        tmp.write_text(json.dumps(report, indent=2) + '\n')
        tmp.replace(output)
    def stage(name, **details):
        report['stages'].append({'name': name, **details})
        save()
    save()
    try:
        inputs = [app.read_bytes(), test.read_bytes()]
        identities = [blob(data) for data in inputs]
        stage('identity', actual=identities, expected=list(PINS),
              sha256=[hashlib.sha256(data).hexdigest() for data in inputs])
        if tuple(identities) != PINS:
            raise ValueError('Input identity mismatch; execution refused')
        version = subprocess.check_output(['node', '--version'], text=True, timeout=5).strip()
        if not version.startswith('v22.'):
            raise ValueError('Node 22 required')
        stage('runtime', node=version, python=sys.version.split()[0])
        with tempfile.TemporaryDirectory() as temp:
            root = pathlib.Path(temp)
            nav = root / 'nav'
            nav.mkdir()
            (nav / 'app.mjs').write_bytes(inputs[0])
            (root / 'test.mjs').write_bytes(inputs[1])
            (nav / 'place.mjs').write_text('export function parseDestination(){return null;}\n')
            (nav / 'compass.mjs').write_text("export function fixQuality(fix){return fix?'usable':'missing';}\nexport function guide(){return null;}\n")
            stage('isolated_fixture', dependencies='two explicit stubs')
            for i in range(3):
                start = time.monotonic()
                result = subprocess.run(['node', 'test.mjs'], cwd=root, capture_output=True,
                                        text=True, timeout=10)
                passes = re.findall(r'^PASS (.+)$', result.stdout, re.M)
                good = (result.returncode == 0 and len(passes) == len(set(passes)) == 8
                        and '8/8 passed' in result.stdout.splitlines())
                report['runs'].append({'run': i+1, 'passed': len(passes), 'cases': passes,
                                       'returncode': result.returncode, 'stderr': result.stderr,
                                       'elapsed_ms': round((time.monotonic()-start)*1000, 2), 'ok': good})
                save()
                if not good:
                    raise RuntimeError('Lifecycle replay failed')
        report['status'] = 'PASS'
    except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as error:
        report['status'] = 'FAIL'
        report['error'] = str(error)
    save()
    return report['status'] == 'PASS'


if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    sys.exit(0 if run(*(pathlib.Path(arg) for arg in sys.argv[1:])) else 1)
