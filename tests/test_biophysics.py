import unittest
import os
from dredge.bio_kernel import (
    PurePythonPatternRecognitionEngine,
    SelfIntrospectionEngine
)

class TestCoreLogicSuite(unittest.TestCase):
    def test_pure_pattern_matching(self):
        scene = [
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0]
        ]
        template = [
            [1, 1],
            [1, 1]
        ]
        res = PurePythonPatternRecognitionEngine.match_template(scene, template)
        self.assertEqual(res['best_match_coordinate'], (1, 1))
        self.assertEqual(res['max_confidence_score'], 1.0)
        self.assertEqual(res['detection_verdict'], "MATCH_CONFIRMED")

    def test_self_introspection(self):
        current_file = os.path.abspath(__file__)
        res = SelfIntrospectionEngine.inspect_and_reverse_source(current_file)
        self.assertTrue(res['total_lines_read'] > 0)
        self.assertEqual(res['state_status'], "SECURE_INTROSPECTION_COMPLETED")

if __name__ == '__main__':
    unittest.main()
