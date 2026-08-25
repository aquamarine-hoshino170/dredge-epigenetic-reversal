import unittest
from dredge.bio_kernel import (
    HodgkinHuxleyCompartmentalEngine,
    QuantumFMOExcitonEngine,
    TuringMorphogenesisEngine,
    DNAOrigamiScaffoldEngine,
    ChronomorphicShannonEntropyEngine
)

class TestQuantumNeuromorphicCore(unittest.TestCase):
    def test_hh_compartmental_propagation(self):
        res = HodgkinHuxleyCompartmentalEngine.simulate_axon_cable(compartments=5, total_time_ms=2.0)
        self.assertEqual(res['compartments_count'], 5)
        self.assertTrue('final_soma_voltage' in res)

    def test_quantum_fmo_exciton(self):
        res = QuantumFMOExcitonEngine.simulate_coherence_dynamics(steps=20)
        self.assertTrue(0.0 <= res['site_1_population'] <= 1.0)
        self.assertTrue(res['final_off_diagonal_coherence'] >= 0.0)

    def test_turing_morphogenesis(self):
        res = TuringMorphogenesisEngine.render_turing_tissue(grid_size=12, iterations=30)
        self.assertEqual(len(res['ascii_visual']), 12)

    def test_dna_origami_torsion(self):
        res = DNAOrigamiScaffoldEngine.calculate_origami_torsion(7249, 180)
        self.assertTrue(res['optimal_crossover_junctions'] > 0)

    def test_chronomorphic_entropy_manifold(self):
        res = ChronomorphicShannonEntropyEngine.simulate_entropy_manifold(generations=30)
        self.assertTrue(res['final_retained_entropy'] < res['initial_information_fidelity'])

if __name__ == '__main__':
    unittest.main()
