import unittest
from dredge.bio_kernel import (
    AdvancedAlignmentEngine, InverseBwtDecoderEngine, SangerSlidingWindowQCEngine,
    PureEnzymeKineticsEngine, PhylogeneticTreeEngine
)

class TestBioMathChallenges(unittest.TestCase):
    def test_affine_smith_waterman(self):
        res = AdvancedAlignmentEngine.smith_waterman_affine("ACGTACGT", "ACGT", match=3, mismatch=-3, gap_open=5, gap_extend=1)
        self.assertEqual(res['max_alignment_score'], 12.0)

    def test_needleman_wunsch_visual(self):
        res = AdvancedAlignmentEngine.needleman_wunsch_visual("GATTACA", "GCATGCU")
        self.assertIn("G-ATTACA", res['aligned_seq1'])

    def test_bwt_inverse_decode(self):
        res = InverseBwtDecoderEngine.decode_bwt("ANNB$AA")
        self.assertEqual(res['decoded_sequence'], "BANANA")

    def test_sliding_window_qc(self):
        # 'I' = Q40, '#' = Q2
        res = SangerSlidingWindowQCEngine.trim_sliding_window("ATGCGATCGCTA", "IIIIII######", window_size=3, min_q=20.0)
        self.assertEqual(res['trimmed_length'], 6)
        self.assertEqual(res['trimmed_sequence'], "ATGCGA")

    def test_kinetics_curve_fit(self):
        subs = [5.0, 10.0, 20.0, 40.0]
        vels = [(100.0 * x) / (10.0 + x) for x in subs]
        res = PureEnzymeKineticsEngine.fit_lineweaver_burk(subs, vels)
        self.assertAlmostEqual(res['v_max'], 100.0, places=2)
        self.assertAlmostEqual(res['k_m'], 10.0, places=2)

    def test_upgma_matrix_parser(self):
        taxa = ["A", "B", "C"]
        mat = [[0.0, 2.0, 4.0], [2.0, 0.0, 4.0], [4.0, 4.0, 0.0]]
        res = PhylogeneticTreeEngine.construct_upgma_tree(taxa, mat)
        self.assertTrue(res['newick_tree_representation'].endswith(";"))

if __name__ == '__main__':
    unittest.main()
