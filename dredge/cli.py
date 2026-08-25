import argparse
import sys
import unittest
from dredge.bio_kernel import (
    ExactHamiltonianAssemblerEngine,
    TruncatedHilbertLindbladEngine,
    StochasticTuringLatticeEngine,
    OpenSpaceDNAOrigamiEngine
)

def main():
    parser = argparse.ArgumentParser(prog='aquamarine-dredge', description='DREDGE Singular-Scale Theoretical Core (v62.0.0)')
    parser.add_argument('--infinite-assemble', nargs='+', help='Exact Hamiltonian Genome Assembly: --infinite-assemble ATGC TGCA GCAT CATA')
    parser.add_argument('--quantum-collapse', nargs=1, type=int, metavar=('DIMENSION',), help='High-Dimensional Lindblad Solver')
    parser.add_argument('--fractal-deadlock', action='store_true', help='Stochastic Reaction-Diffusion Lattice')
    parser.add_argument('--origami-shatter', nargs=3, type=int, metavar=('SCAFFOLD_BP', 'STAPLES', 'AXES'), help='Multi-Axis Origami Strain')
    parser.add_argument('--test', action='store_true', help='Run unit tests')

    args = parser.parse_args()

    if args.test:
        suite = unittest.defaultTestLoader.discover('tests')
        unittest.TextTestRunner(verbosity=2).run(suite)
        return

    if args.infinite_assemble:
        res = ExactHamiltonianAssemblerEngine.assemble_exact(args.infinite_assemble)
        print("\n" + "="*50)
        print("  EXACT HAMILTONIAN PATH GENOME ASSEMBLY")
        print("="*50)
        print(f" • Assembled Contig: {res['assembled_contig']}")
        print(f" • Contig Length: {res.get('contig_length', 'N/A')} bp | Path: {res.get('hamiltonian_path', 'N/A')}")
        print(f" • Optimality: {res.get('optimality', res.get('status', 'OK'))}\n" + "="*50 + "\n")
        return

    if args.quantum_collapse:
        res = TruncatedHilbertLindbladEngine.solve_master_equation(dimension=args.quantum_collapse[0])
        print(f"\n • High-Dim Lindblad Solver (Dim: {res['hilbert_space_dimension']}): State Purity = {res['quantum_state_purity']}\n • Fock Populations: {res['fock_level_populations']}\n • Model: {res['solver_model']}\n")
        return

    if args.fractal_deadlock:
        res = StochasticTuringLatticeEngine.simulate_stochastic_pde(grid_size=18, steps=50)
        print("\n" + "="*45)
        print("  STOCHASTIC TURING REACTION-DIFFUSION LATTICE")
        print("="*45)
        for r in res['lattice_render']:
            print("  " + r)
        print("="*45)
        print(f" • Field Density: {res['mean_field_density']} | Noise Variance: {res['variance_activator']}\n")
        return

    if args.origami_shatter:
        res = OpenSpaceDNAOrigamiEngine.calculate_open_torsion(args.origami_shatter[0], args.origami_shatter[1], args.origami_shatter[2])
        print(f"\n • Open-Space DNA Origami: {res['scaffold_length']} ({res['active_rotational_axes']} Axes)\n • Torsion Energy: {res['torsion_strain_energy_pN_nm']} pN·nm ({res['structural_verdict']})\n")
        return

    parser.print_help()

if __name__ == '__main__':
    main()
