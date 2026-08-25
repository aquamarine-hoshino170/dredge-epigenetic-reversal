import unittest
from dredge.bio_kernel import (
    ExactHamiltonianAssemblerEngine,
    TruncatedHilbertLindbladEngine,
    StochasticTuringLatticeEngine,
    OpenSpaceDNAOrigamiEngine
)

class TestSingularTheoreticalCore(unittest.TestCase):
    def test_exact_hamiltonian_assembly(self):
        reads = ["ATGCA", "GCATG", "CATGC"]
        res = ExactHamiltonianAssemblerEngine.assemble_exact(reads, min_overlap=3)
        self.assertTrue('assembled_contig' in res)
        self.assertTrue(len(res['assembled_contig']) >= 5)

    def test_truncated_lindblad(self):
        res = TruncatedHilbertLindbladEngine.solve_master_equation(dimension=6)
        self.assertEqual(res['hilbert_space_dimension'], 6)
        self.assertTrue(0.0 <= res['quantum_state_purity'] <= 1.0)

    def test_stochastic_turing(self):
        res = StochasticTuringLatticeEngine.simulate_stochastic_pde(grid_size=10, steps=20)
        self.assertEqual(len(res['lattice_render']), 10)

    def test_open_space_origami(self):
        res = OpenSpaceDNAOrigamiEngine.calculate_open_torsion(7249, 190, axes=3)
        self.assertTrue(res['recommended_crossovers'] > 0)

if __name__ == '__main__':
    unittest.main()
