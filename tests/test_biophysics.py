import unittest
from dredge.bio_kernel import (
    AsyncP2PBioLedgerEngine,
    QuantumLindbladDensityVisualizerEngine,
    TuringMorphogenesisDynamicGridEngine,
    DNAOrigamiTorsionRouterEngine,
    ChronomorphicShannonManifoldEngine
)

class TestHyperDimensionalCore(unittest.TestCase):
    def test_async_bio_ledger(self):
        res = AsyncP2PBioLedgerEngine.run_consensus_mesh(["MUT_A", "MUT_B"], num_nodes=2)
        self.assertEqual(res['total_blocks'], 3)
        self.assertTrue(res['chain_ledger'][0]['block_hash'] != "")

    def test_quantum_lindblad_vis(self):
        res = QuantumLindbladDensityVisualizerEngine.simulate_and_visualize(sites=3, total_time_fs=20.0)
        self.assertEqual(len(res['site_populations']), 3)
        self.assertEqual(len(res['density_matrix_ascii']), 3)

    def test_turing_morphogenesis_mask(self):
        res = TuringMorphogenesisDynamicGridEngine.render_morphogenesis(grid_size=10, iterations=20)
        self.assertEqual(len(res['ascii_tissue_render']), 10)

    def test_dna_origami_3d(self):
        res = DNAOrigamiTorsionRouterEngine.calculate_routing_strain(7249, 190, target_planes=3)
        self.assertTrue(res['optimal_crossovers'] > 0)

    def test_chrono_shannon_decay(self):
        res = ChronomorphicShannonManifoldEngine.simulate_entropy_manifold(generations=30)
        self.assertTrue(res['final_retained_entropy'] < res['initial_shannon_fidelity'])

if __name__ == '__main__':
    unittest.main()
