import unittest
from dredge.bio_kernel import (
    ParallelFMIndexEngine, Constrained3DRNAEngine, GillespieStochasticKineticsEngine,
    JukesCantorMLEngine, DeBruijnGraphCorrectionEngine, EpigeneticShannonEntropyEngine
)

class TestDomainBreakerCore(unittest.TestCase):
    def test_parallel_fm_search(self):
        res = ParallelFMIndexEngine.parallel_search("BANANABANANA", ["ANA", "BAN", "XYZ"])
        self.assertEqual(res['match_results']['ANA'], 4)
        self.assertEqual(res['match_results']['XYZ'], 0)

    def test_3d_rna_folding(self):
        seq = "GGGAAACCC"
        n = len(seq)
        dist_mat = [[abs(i - j) * 3.8 for j in range(n)] for i in range(n)]
        res = Constrained3DRNAEngine.fold_with_spatial_constraints(seq, dist_mat)
        self.assertTrue(res['max_constrained_energy_score'] > 0.0)

    def test_gillespie_simulation(self):
        res = GillespieStochasticKineticsEngine.simulate_enzyme_system(s_init=100, e_init=20, t_max=2.0)
        self.assertTrue(res['total_reaction_events'] > 0)

    def test_jc69_ml_estimation(self):
        res = JukesCantorMLEngine.calculate_branch_ml("ACGTACGTACGT", "ACGTACGTACGA")
        self.assertTrue(res['maximum_likelihood_branch_t'] > 0.0)

    def test_debruijn_error_correction(self):
        reads = ["ACGT", "ACGT", "ACGA"]
        res = DeBruijnGraphCorrectionEngine.error_correct(reads, k=3, min_coverage=2)
        self.assertTrue(res['corrections_made'] >= 1)

    def test_shannon_methylation_entropy(self):
        patterns = ["1100", "1100", "1100", "1100"]
        res = EpigeneticShannonEntropyEngine.calculate_methylation_entropy(patterns)
        self.assertEqual(res['shannon_entropy_bits'], 0.0)

if __name__ == '__main__':
    unittest.main()
