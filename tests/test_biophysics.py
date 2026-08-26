import unittest
from dredge.bio_kernel import (
    QuantumComputingCore,
    CellularMorphogenesisCore,
    InformationSignalPhysicsCore,
    OrbitalAstrophysicsCore
)

class TestOmniscienceSingularitySuite(unittest.TestCase):
    def test_quantum_bell_state(self):
        res = QuantumComputingCore.simulate_bell_state()
        self.assertAlmostEqual(res['basis_probabilities']['|00⟩'], 0.5, places=2)
        self.assertAlmostEqual(res['basis_probabilities']['|11⟩'], 0.5, places=2)
        self.assertEqual(res['entanglement_verdict'], "MAXIMALLY_ENTANGLED_BELL_STATE")

    def test_cellular_morphogenesis(self):
        res = CellularMorphogenesisCore.simulate_automata(grid_size=10, steps=5)
        self.assertTrue(res['final_shannon_entropy'] >= 0.0)
        self.assertEqual(len(res['terminal_morphology_ascii']), 8)

    def test_signal_fft_psd(self):
        res = InformationSignalPhysicsCore.analyze_signal(num_samples=32)
        self.assertTrue(res['dominant_peak_psd'] > 0.0)
        self.assertEqual(len(res['spectral_density_ascii']), 16)

    def test_orbital_astrophysics(self):
        res = OrbitalAstrophysicsCore.simulate_two_body_orbit(time_steps=20)
        self.assertTrue(res['semi_major_axis'] > 0.0)
        self.assertEqual(res['symplectic_stability'], "STABLE_ENERGY_PRESERVING_TRAJECTORY")

if __name__ == '__main__':
    unittest.main()
