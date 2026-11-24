import base64, tempfile, unittest
from pathlib import Path
from satnav_dependencies import materialise, blob_oid, census

class TestDependencies(unittest.TestCase):
    def fixture(self):
        data={'src/x.mjs':b'export const x=1;\n','LICENSE':b'license','NOTICE':b'notice'}
        lock={'schema_version':1,'files':[{'repo':'Ventusltd/example','commit':'a'*40,'path':k,'blob':blob_oid(v),'target':'vendor/example/'+k,'licence':'Apache-2.0'} for k,v in data.items()]}
        def fetch(url):
            key=url.split('/contents/')[1].split('?')[0];v=data[key]
            return {'type':'file','sha':blob_oid(v),'encoding':'base64','content':base64.b64encode(v).decode(),'size':len(v)}
        return lock,fetch
    def test_happy(self):
        lock,fetch=self.fixture()
        with tempfile.TemporaryDirectory() as t:
            dest=Path(t)/'pack';self.assertEqual(len(materialise(lock,dest,fetch)),3);self.assertTrue((dest/'receipt.json').exists())
            with self.assertRaises(FileExistsError):materialise(lock,dest,fetch)
    def test_bad_hash(self):
        lock,fetch=self.fixture();lock['files'][0]['blob']='0'*40
        with tempfile.TemporaryDirectory() as t:
            dest=Path(t)/'pack'
            with self.assertRaises(ValueError):materialise(lock,dest,fetch)
            self.assertFalse(dest.exists())
    def test_traversal(self):
        lock,fetch=self.fixture();lock['files'][0]['target']='vendor/../bad'
        with tempfile.TemporaryDirectory() as t:
            with self.assertRaises(ValueError):materialise(lock,Path(t)/'pack',fetch)
    def test_missing_notice(self):
        lock,fetch=self.fixture();lock['files'].pop()
        with tempfile.TemporaryDirectory() as t:
            with self.assertRaises(ValueError):materialise(lock,Path(t)/'pack',fetch)
    def test_census_truncated(self):
        def fetch(url):
            if '/users/' in url:return [{'full_name':'Ventusltd/test','owner':{'login':'Ventusltd'},'default_branch':'main'}]
            if '/commits/' in url:return {'sha':'a'*40,'commit':{'tree':{'sha':'b'*40}}}
            return {'truncated':True,'tree':[{'type':'blob','path':'gps.js','sha':'c'*40,'size':1}]}
        r=census(fetch=fetch);self.assertEqual(r['public_repo_count'],1);self.assertEqual(r['repositories'][0]['status'],'INCOMPLETE')
if __name__=='__main__':unittest.main()
