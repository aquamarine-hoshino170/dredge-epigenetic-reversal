import unittest
from dredge.bio_kernel import (
    QuantumMolecularDockingEngine,
    DirectedEvolutionDAGEngine,
    NonNewtonianVascularEngine,
    XenobiologyCircuitCompilerEngine
)

class TestCosmicBioSuite(unittest.TestCase):
    def test_molecular_docking_affinity(self):
        res = QuantumMolecularDockingEngine.calculate_binding_affinity(num_heavy_atoms=18, rotatable_bonds=3, contact_distance_angstrom=2.8)
        self.assertTrue('total_binding_free_energy_dG' in res)
        self.assertIn('kcal/mol', res['total_binding_free_energy_dG'])

    def test_directed_evolution_dag(self):
        res = DirectedEvolutionDAGEngine.simulate_evolution(generations=3, population_size=2)
        self.assertEqual(len(res['lineage_dag_ascii']), 6)
        self.assertTrue(res['top_fitness_score'] > 0.0)

    def test_non_newtonian_vascular(self):
        res = NonNewtonianVascularEngine.calculate_hemodynamics(vessel_radius_um=12.0, flow_rate_nl_s=1.5, hematocrit=0.45)
        self.assertTrue(res['wall_shear_stress_Pa'] > 0.0)
        self.assertTrue(res['apparent_blood_viscosity_cP'] > 0.0)

    def test_xeno_circuit_compiler(self):
        # 'P' and 'Z' synthetic bases
        res = XenobiologyCircuitCompilerEngine.compile_xeno_circuit("ATGPZC", induction_level=1.2)
        self.assertEqual(res['synthetic_hachimoji_bases'], 2)
        self.assertEqual(res['complementary_xeno_strand'], "TACZPG")
        self.assertEqual(res['orthogonal_chassis_status'], "HIGHLY_ORTHOGONAL_SYNTHETIC_CELL")

if __name__ == '__main__':
    unittest.main()
