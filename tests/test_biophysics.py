import unittest
from dredge.bio_kernel import (
    PolymorphicQuineEngine,
    ZeroKnowledgeLedgerEngine,
    ChaosReactionDiffusionEngine,
    MolecularMeshStrainEngine
)

class TestPolymorphicZKCore(unittest.TestCase):
    def test_polymorphic_quine(self):
        res = PolymorphicQuineEngine.generate_polymorphic_replica()
        self.assertTrue(res['generated_code_bytes'] > 0)
        self.assertIn("def execute():", res['source_code_replica'])

    def test_zk_ledger_proof(self):
        res = ZeroKnowledgeLedgerEngine.simulate_zk_transition(initial_balance=1000, transfer_amount=350)
        self.assertTrue(res['zk_proof_verified'])
        self.assertIn("0x", res['commitment_initial'])

    def test_chaos_rd_lattice(self):
        res = ChaosReactionDiffusionEngine.simulate_chaos_lattice(grid_size=10, steps=15)
        self.assertEqual(len(res['ascii_visual']), 10)

    def test_molecular_mesh_strain(self):
        res = MolecularMeshStrainEngine.calculate_mesh_strain(nodes=40, edge_density=2.0, applied_torque_n_m=10.0)
        self.assertEqual(res['scaffold_topological_nodes'], 40)
        self.assertTrue(res['total_strain_energy_J'] > 0.0)

if __name__ == '__main__':
    unittest.main()
