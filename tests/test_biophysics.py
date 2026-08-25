import unittest
from dredge.bio_kernel import (
    DynamicTopologyP2PLedgerEngine,
    OpenQuantumLindbladVisualizerEngine,
    FractalTuringMorphogenesisEngine,
    MultiAxisOrigamiTorsionEngine,
    DeepChronomorphicShannonEngine
)

class TestSingularitySuite(unittest.TestCase):
    def test_dynamic_p2p_mesh(self):
        res = DynamicTopologyP2PLedgerEngine.run_dynamic_mesh(["MUT_A", "MUT_B"], total_nodes=4, clusters=2)
        self.assertEqual(res['total_blocks'], 3)
        self.assertTrue(len(res['consensus_ledger']) > 0)

    def test_lindblad_open_quantum(self):
        res = OpenQuantumLindbladVisualizerEngine.simulate_and_render(sites=4, total_time_fs=20.0)
        self.assertEqual(len(res['final_site_populations']), 4)
        self.assertEqual(len(res['ascii_quantum_matrix']), 4)

    def test_fractal_turing_tissue(self):
        res = FractalTuringMorphogenesisEngine.render_fractal_tissue(grid_size=12, iterations=20)
        self.assertEqual(len(res['fractal_ascii_tissue']), 12)

    def test_multi_axis_origami(self):
        res = MultiAxisOrigamiTorsionEngine.calculate_multi_axis_strain(7249, 190, axes=3, hinge_count=4)
        self.assertTrue(res['optimal_crossovers'] > 0)

    def test_deep_chrono_decay(self):
        res = DeepChronomorphicShannonEngine.simulate_deep_decay(generations=40)
        self.assertTrue(res['final_retained_entropy'] < res['initial_information_bits'])

if __name__ == '__main__':
    unittest.main()
