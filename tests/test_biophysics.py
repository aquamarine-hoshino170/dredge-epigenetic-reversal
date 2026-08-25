import unittest
from dredge.bio_kernel import (
    NLSESolitonSolverEngine,
    HomomorphicMatrixLedgerEngine,
    MacroMolecularMeshTorsionEngine,
    FractionalDiffusionFractalEngine
)

class TestUniversalSingularityCore(unittest.TestCase):
    def test_schrodinger_soliton(self):
        res = NLSESolitonSolverEngine.solve_soliton_grid(nodes=16, time_steps=20)
        self.assertTrue(res['peak_soliton_density'] > 0.0)
        self.assertEqual(res['phase_envelope_stability'], "COHERENT_SOLITON_PROPAGATION")

    def test_homomorphic_ledger(self):
        balances = [600, 300, 1500]
        res = HomomorphicMatrixLedgerEngine.verify_ledger(balances)
        self.assertEqual(res['total_clients'], 3)
        self.assertEqual(res['proof_validation_status'], "ZERO_KNOWLEDGE_HOMOMORPHIC_VALIDATED")

    def test_mesh_torsion(self):
        res = MacroMolecularMeshTorsionEngine.calculate_mesh_torsion(nodes=50, axial_torque_n_m=20.0, axes=3)
        self.assertEqual(res['topological_nodes'], 50)
        self.assertTrue(res['von_mises_stress_MPa'] > 0.0)

    def test_fractal_diffusion(self):
        res = FractionalDiffusionFractalEngine.simulate_fractal_lattice(grid_size=12, steps=15)
        self.assertEqual(len(res['fractal_ascii_tissue']), 12)

if __name__ == '__main__':
    unittest.main()
