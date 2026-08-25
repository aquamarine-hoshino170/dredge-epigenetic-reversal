import argparse
import sys
import os
import unittest
from dredge.bio_kernel import (
    PurePythonPatternRecognitionEngine,
    SelfIntrospectionEngine
)

def main():
    parser = argparse.ArgumentParser(prog='aquamarine-dredge', description='DREDGE Core Logic & Pattern Engine (v65.0.0)')
    parser.add_argument('--ai-trap', action='store_true', help='Run Zero-Dependency 2D Visual Pattern Recognition')
    parser.add_argument('--self-inspect', action='store_true', help='Read and reverse inspect own CLI source structure')
    parser.add_argument('--test', action='store_true', help='Run unit tests')

    args = parser.parse_args()

    if args.test:
        suite = unittest.defaultTestLoader.discover('tests')
        unittest.TextTestRunner(verbosity=2).run(suite)
        return

    if args.ai_trap:
        # 6x6 Scene with an embedded 3x3 target pattern (X shape)
        scene = [
            [0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]
        target = [
            [1, 0, 1],
            [0, 1, 0],
            [1, 0, 1]
        ]
        res = PurePythonPatternRecognitionEngine.match_template(scene, target)
        print("\n" + "="*50)
        print("  ZERO-DEPENDENCY VISUAL PATTERN RECOGNITION")
        print("="*50)
        print(f" • Best Match Coordinate: {res['best_match_coordinate']}")
        print(f" • Confidence Score: {res['max_confidence_score']} ({res['detection_verdict']})")
        print(f" • Image: {res['image_shape']} | Template: {res['template_shape']}\n" + "="*50 + "\n")
        return

    if args.self_inspect:
        current_file = os.path.abspath(__file__)
        res = SelfIntrospectionEngine.inspect_and_reverse_source(current_file)
        print("\n" + "="*50)
        print("  CODE SELF-INTROSPECTION & STREAM REVERSAL")
        print("="*50)
        print(f" • Target: {res['inspected_file']}")
        print(f" • Total Lines: {res['total_lines_read']} | SHA-256: {res['source_sha256'][:16]}...")
        print(" • Bottom-Up Traceback Preview:")
        for line in res['bottom_up_memory_stream']:
            print(f"   <-- {line}")
        print("="*50 + "\n")
        return

    parser.print_help()

if __name__ == '__main__':
    main()
