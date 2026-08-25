import unittest
from dredge.bio_kernel import (
    GrandFinaleBioEngine,
    FMIndexBwtEngine,
    AdaptivePhredTrimmerEngine,
    NonLinearKineticsEngine,
    ExactTreeBranchEngine,
    PureThermodynamicsEngine
)

class TestGrandFinaleCore(unittest.TestCase):
    def test_sw_affine_matrices(self):
        res = GrandFinaleBioEngine.smith_waterman_full_affine("ACGTACGT", "ACGT")
        self.assertEqual(res['max_score'], 12.0)
        self.assertIn("ACGT", res['local_align_seq1'])

    def test_fm_index_search(self):
        res = FMIndexBwtEngine.count_pattern("ANA", "BANANA")
        self.assertEqual(res['occurrences'], 2)
        self.assertEqual(res['status'], "EXACT_MATCH")

    def test_adaptive_trimmer(self):
        res = AdaptivePhredTrimmerEngine.adaptive_trim("ATGCGATCGCTA", "IIIIII######", min_q=20.0)
        self.assertTrue(res['trimmed_length'] <= 6)

    def test_nls_kinetics_curve_fit(self):
        subs = [5.0, 10.0, 20.0, 40.0]
        vels = [(100.0 * x) / (10.0 + x) for x in subs]
        res = NonLinearKineticsEngine.fit_direct_nls(subs, vels)
        self.assertAlmostEqual(res['v_max'], 100.0, places=1)
        self.assertAlmostEqual(res['k_m'], 10.0, places=1)

    def test_upgma_branch_verification(self):
        taxa = ["A", "B", "C"]
        mat = [[0.0, 2.0, 4.0], [2.0, 0.0, 4.0], [4.0, 4.0, 0.0]]
        res = ExactTreeBranchEngine.construct_verified_upgma(taxa, mat)
        self.assertTrue(res['newick_tree'].endswith(";"))
        self.assertEqual(res['root_tree_height'], 2.0)

if __name__ == '__main__':
    unittest.main()
