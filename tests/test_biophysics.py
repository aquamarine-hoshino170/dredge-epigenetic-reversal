import unittest
from dredge.bio_kernel import (
    PureTensor,
    NLSESolitonSolverEngine,
    LatticeGaugeFieldEngine,
    RecursiveSTARKEngine,
    TensorContinuumElasticityEngine
)

class TestZeroDependencyPureCore(unittest.TestCase):
    def test_pure_tensor_matmul(self):
        A = [[1, 2], [3, 4]]
        B = [[2, 0], [1, 2]]
        C = PureTensor.matmul(A, B)
        self.assertEqual(C, [[4, 4], [10, 8]])

    def test_pure_schrodinger_soliton(self):
        res = NLSESolitonSolverEngine.solve_soliton_grid(nodes=16, time_steps=20)
        self.assertTrue(res['peak_soliton_density'] > 0.0)
        self.assertEqual(res['phase_envelope_stability'], "COHERENT_SOLITON_PROPAGATION")

    def test_pure_su3_gauge_lattice(self):
        res = LatticeGaugeFieldEngine.compute_wilson_lattice(grid_size=2, beta=4.0)
        self.assertTrue(res['mean_wilson_plaquette'] > 0.0)
        self.assertEqual(len(res['topological_charge_tensor_ascii']), 2)

    def test_pure_stark_enclave(self):
        trace = [1, 2, 4, 8, 16]
        res = RecursiveSTARKEngine.generate_recursive_stark_proof(trace)
        self.assertEqual(res['computation_trace_steps'], 5)
        self.assertEqual(res['verification_status'], "RECURSIVE_AIR_PROOF_VERIFIED")

    def test_pure_tensor_elasticity(self):
        grad_u = [
            [0.01, 0.0, 0.0],
            [0.0, 0.01, 0.0],
            [0.0, 0.0, 0.01]
        ]
        res = TensorContinuumElasticityEngine.compute_tensor_stress(grad_u)
        self.assertTrue(res['von_mises_equivalent_stress_MPa'] > 0.0)

if __name__ == '__main__':
    unittest.main()
