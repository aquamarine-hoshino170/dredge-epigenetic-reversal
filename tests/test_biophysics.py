import unittest
from dredge.bio_kernel import (
    ExactMultiSequenceAlignmentEngine,
    AbInitioProteinPhysicsEngine,
    MultiScaleTissueMorphogenesisEngine,
    VectorizedNLSOptimizerEngine
)

class TestNPHardBiophysicsCore(unittest.TestCase):
    def test_exact_nd_msa(self):
        seqs = ["ACGT", "ACG", "ACGT"]
        res = ExactMultiSequenceAlignmentEngine.align_exact_nd(seqs)
        self.assertTrue('exact_optimal_score' in res)

    def test_ab_initio_protein_physics(self):
        res = AbInitioProteinPhysicsEngine.compute_energy_landscape("MKWVTFISLLLL")
        self.assertTrue('total_conformational_energy' in res)

    def test_multiscale_morphogenesis(self):
        res = MultiScaleTissueMorphogenesisEngine.simulate_tissue_coupling(grid_size=8, time_steps=10)
        self.assertTrue(res['total_viable_cells_in_tissue'] >= 0)

    def test_vectorized_nls(self):
        x = [5.0, 10.0, 20.0, 40.0]
        y = [(100.0 * val) / (10.0 + val) for val in x]
        res = VectorizedNLSOptimizerEngine.optimize_fit(x, y)
        self.assertAlmostEqual(res['optimized_parameters']['Vmax'], 100.0, places=1)

if __name__ == '__main__':
    unittest.main()
