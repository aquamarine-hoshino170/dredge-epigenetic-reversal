import unittest
from dredge.bio_kernel import (
    PureMathCore,
    PureBiologyCore,
    PurePhysicsCore,
    PureChemistryCore
)

class TestPureOmniscienceCore(unittest.TestCase):
    def test_pure_math_curvature(self):
        metric = [[2.0, 0.5], [0.5, 3.0]]
        res = PureMathCore.calculate_curvature(metric)
        self.assertTrue(res['metric_determinant'] > 0.0)
        self.assertTrue('ricci_scalar_curvature' in res)

    def test_pure_biology_dna_thermo(self):
        seq = "CGCATGCATGCA"
        res = PureBiologyCore.calculate_dna_thermodynamics(seq)
        self.assertTrue(res['melting_temperature_Tm_C'] > 20.0)
        self.assertTrue(res['free_energy_delta_G_37C'] < 0.0)

    def test_pure_physics_quantum_wave(self):
        res = PurePhysicsCore.simulate_quantum_dispersion(nodes=16, time_fs=10.0)
        self.assertTrue(res['dispersed_width_sigma_t'] > res['initial_width_sigma_0'])

    def test_pure_chemistry_arrhenius(self):
        res = PureChemistryCore.compute_reaction_rate(temperature_c=25.0, ea_kj_mol=50.0)
        self.assertIn("s⁻¹", res['rate_constant_k'])

if __name__ == '__main__':
    unittest.main()
