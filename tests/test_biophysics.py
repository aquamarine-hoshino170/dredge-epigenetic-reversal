import unittest
from dredge.bio_kernel import (
    MultithreadedBWTEngine,
    Constrained3DRNAEngine,
    GillespieStochasticKineticsEngine,
    JukesCantorMLEngine,
    DeBruijnGraphCorrectionEngine
)

class TestUltimateTheoreticalCore(unittest.TestCase):
    def test_parallel_bwt(self):
        res = MultithreadedBWTEngine.parallel_bwt_search("BANANABANANA", ["ANA", "BAN", "XYZ"])
        self.assertEqual(res['matches']['ANA'], 4)
        self.assertEqual(res['matches']['XYZ'], 0)

    def test_3d_rna_folding(self):
        seq = "GGGAAACCC"
        n = len(seq)
        dist_mat = [[abs(i - j) * 3.8 for j in range(n)] for i in range(n)]
        res = Constrained3DRNAEngine.fold_3d_constrained(seq, dist_mat)
        self.assertTrue(res['max_constrained_energy_score'] > 0.0)

    def test_gillespie_simulation(self):
        res = GillespieStochasticKineticsEngine.simulate_trajectory(s_init=100, e_init=20, t_max=1.5)
        self.assertTrue(res['total_stochastic_events'] > 0)

    def test_jc69_ml(self):
        res = JukesCantorMLEngine.calculate_ml_branch("ACGTACGTACGT", "ACGTACGTACGA")
        self.assertTrue(res['max_likelihood_branch_t'] > 0.0)

    def test_debruijn_repair(self):
        reads = ["ACGT", "ACGT", "ACGA"]
        res = DeBruijnGraphCorrectionEngine.repair_reads(reads, k=3, min_cov=2)
        self.assertTrue(res['corrections_applied'] >= 1)

if __name__ == '__main__':
    unittest.main()
