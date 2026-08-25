import argparse
import sys
import unittest
from dredge.bio_kernel import (
    QuantumMolecularDockingEngine,
    DirectedEvolutionDAGEngine,
    NonNewtonianVascularEngine,
    XenobiologyCircuitCompilerEngine
)

def main():
    parser = argparse.ArgumentParser(prog='aquamarine-dredge', description='DREDGE Cosmic Quantum Bio-Network Suite (v59.0.0)')
    parser.add_argument('--docking-affinity', nargs=3, type=float, metavar=('ATOMS', 'ROT_BONDS', 'DIST_A'), help='Compute Molecular Docking Binding Affinity')
    parser.add_argument('--directed-evolution', nargs=2, type=int, metavar=('GENS', 'POP_SIZE'), help='Run Directed Evolution Lineage DAG')
    parser.add_argument('--vascular-pde', nargs=3, type=float, metavar=('RADIUS_UM', 'FLOW_NL_S', 'HEMATOCRIT'), help='Non-Newtonian Vascular Biomechanics')
    parser.add_argument('--xeno-compiler', nargs=2, metavar=('XENO_SEQ', 'INDUCTION'), help='Compile Hachimoji Synthetic Genetic Circuit')
    parser.add_argument('--test', action='store_true', help='Run unit tests')

    args = parser.parse_args()

    if args.test:
        suite = unittest.defaultTestLoader.discover('tests')
        unittest.TextTestRunner(verbosity=2).run(suite)
        return

    if args.docking_affinity:
        res = QuantumMolecularDockingEngine.calculate_binding_affinity(int(args.docking_affinity[0]), int(args.docking_affinity[1]), args.docking_affinity[2])
        print(f"\n • Binding Free Energy (dG): {res['total_binding_free_energy_dG']} | Kd: {res['predicted_dissociation_constant_Kd']}\n   Potentials: vdW={res['vdw_potential_kcal_mol']} kcal/mol, Elec={res['electrostatic_potential_kcal_mol']} kcal/mol, H-Bond={res['hbond_energy_kcal_mol']} kcal/mol\n • Status: {res['affinity_class']}\n")
        return

    if args.directed_evolution:
        res = DirectedEvolutionDAGEngine.simulate_evolution(generations=args.directed_evolution[0], population_size=args.directed_evolution[1])
        print("\n" + "="*55)
        print("  DIRECTED EVOLUTION LINEAGE DAG")
        print("="*55)
        for line in res['lineage_dag_ascii']:
            print(line)
        print("="*55)
        print(f" • Top Fitness: {res['top_fitness_score']} | Best Variant: {res['top_evolved_sequence']}\n")
        return

    if args.vascular_pde:
        res = NonNewtonianVascularEngine.calculate_hemodynamics(args.vascular_pde[0], args.vascular_pde[1], args.vascular_pde[2])
        print(f"\n • Microvascular Biomechanics: Shear Stress = {res['wall_shear_stress_Pa']} Pa | Apparent Viscosity = {res['apparent_blood_viscosity_cP']} cP\n • Pressure Drop: {res['pressure_gradient_mmHg_mm']} mmHg/mm ({res['flow_regime']})\n")
        return

    if args.xeno_compiler:
        res = XenobiologyCircuitCompilerEngine.compile_xeno_circuit(args.xeno_compiler[0], float(args.xeno_compiler[1]))
        print(f"\n • Hachimoji Xeno-Circuit: {res['xeno_sequence_length']} (Synthetic Bases: {res['synthetic_hachimoji_bases']})\n • Complementary Strand: {res['complementary_xeno_strand']}\n • Transcription Efficiency: {res['promoter_transcription_efficiency']} | Delay: {res['circuit_propagation_delay_ms']} ms ({res['orthogonal_chassis_status']})\n")
        return

    parser.print_help()

if __name__ == '__main__':
    main()
