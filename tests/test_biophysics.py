import unittest
from dredge.bio_kernel import (
    DNASolitonWaveEngine,
    MultiTenantZKPedersenEngine,
    ChaosFractalDiffusionEngine,
    MacroMolecularTorsionEngine
)

class TestQuantumBiologicalInvariantCore(unittest.TestCase):
    def test_dna_soliton_wave(self):
        res = DNASolitonWaveEngine.simulate_soliton_propagation(lattice_nodes=16, time_steps=20)
        self.assertTrue(res['peak_soliton_amplitude'] > 0.0)
        self.assertEqual(res['mechanical_stability'], "STABLE_SOLITON_CONDUCTION")

    def test_zk_pedersen_homomorphism(self):
        balances = [400, 300, 800]
        res = MultiTenantZKPedersenEngine.verify_multi_tenant_state(balances)
        self.assertEqual(res['total_tenants'], 3)
        self.assertEqual(res['zk_proof_status'], "PROVEN_VALID_ZERO_KNOWLEDGE")

    def test_chaos_fractal_diffusion(self):
        res = ChaosFractalDiffusionEngine.simulate_chaos_fractal(grid_size=12, steps=15)
        self.assertEqual(len(res['fractal_ascii_tissue']), 12)

    def test_scaffold_joint_strain(self):
        res = MacroMolecularTorsionEngine.calculate_scaffold_strain(nodes=40, applied_torque_n_m=15.0, axes=3)
        self.assertEqual(res['topological_scaffold_nodes'], 40)
        self.assertTrue(res['von_mises_stress_MPa'] > 0.0)

if __name__ == '__main__':
    unittest.main()
