import copy
import json
import pathlib
import tempfile
import unittest
import sync

class MirrorTests(unittest.TestCase):
    def source(self):
        return {'schemaVersion':1,'revision':11,'lastUpdatedAt':None,'lastLearningDate':'2026-11-01','currentCppLesson':{'number':18,'goal':'字符串','acceptance':'实验'},'cppLessons':[{'number':n,'title':str(n),'status':'已验收' if n<18 else '未开始'} for n in range(1,49)],'recentLearning':[],'continuity':{'verified':'已验证','openQuestions':'复习','nextStep':'第18节','longTermPlan':'C++ → CANN'},'notes':'PRIVATE NOTE','token':'SECRET','email':'private@example.test'}
    def test_allowlist_and_null_time(self):
        source=self.source(); before=copy.deepcopy(source); d=sync.project(source,'2026-11-01T06:00:00Z');self.assertEqual(source,before);self.assertEqual(d['current_cpp_lesson']['number'],18);self.assertIsNone(d['updated_at']);self.assertFalse(any(s in json.dumps(d) for s in ['PRIVATE NOTE','SECRET','private@example.test']));self.assertEqual(len(d['cpp_lessons']),48)
    def test_version_change(self):
        s=self.source();a=sync.project(s,'2026-11-01T06:00:00Z');s['revision']=12;s['cppLessons'][17]['status']='已验收';s['currentCppLesson']['number']=19;s['lastUpdatedAt']='2026-11-01T06:05:00Z';b=sync.project(s,'2026-11-01T06:06:00Z');self.assertEqual((a['data_version'],b['data_version']),(11,12));self.assertEqual(b['current_cpp_lesson']['number'],19);self.assertIn('第 19/48 节',sync.markdown(b))
    def test_redaction(self):
        s=self.source();s['continuity']['openQuestions']='API_KEY=private token:abc Bearer xyz ghp_hidden abc@example.test /Users/jjs/private ~/secret';out=json.dumps(sync.project(s,'2026-11-01T06:00:00Z'));self.assertFalse(any(x in out for x in ['private','abc@example.test','ghp_hidden','~/secret','xyz']))
    def test_regression_keeps_existing(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=pathlib.Path(tmp);s=self.source();d=sync.project(s,'2026-11-01T06:00:00Z');sync.save(d,path);before=(path/'learning-status.json').read_bytes();d['data_version']=10
            with self.assertRaises(ValueError):sync.save(d,path)
            self.assertEqual((path/'learning-status.json').read_bytes(),before)
    def test_incomplete_source_rejected(self):
        s=self.source();s['cppLessons'].pop()
        with self.assertRaises(ValueError):sync.project(s,'2026-11-01T06:00:00Z')
if __name__=='__main__':unittest.main()
