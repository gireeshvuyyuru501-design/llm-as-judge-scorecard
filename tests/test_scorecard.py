import unittest
from scorecard import evaluate, score_case

class TestScorecard(unittest.TestCase):
    def test_identical_answer(self):
        self.assertEqual(score_case({'id':'1','response':'Paris France','reference':'Paris France'})['lexical_f1'], 1.0)
    def test_empty_response(self):
        self.assertEqual(score_case({'id':'1','response':'','reference':'Paris'})['lexical_f1'], 0.0)
    def test_partial_match(self):
        self.assertGreater(score_case({'id':'1','response':'Paris','reference':'Paris France'})['lexical_f1'], 0)
    def test_empty_cases_rejected(self):
        with self.assertRaises(ValueError):
            evaluate([])
    def test_report_metadata(self):
        self.assertIn('not_llm_judge', evaluate([{'id':'1','response':'a','reference':'a'}])['method'])

if __name__ == '__main__':
    unittest.main()
