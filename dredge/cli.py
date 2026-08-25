import argparse
import sys
import unittest
from dredge.bio_kernel import (
    ExactMultiSequenceAlignmentEngine,
    AbInitioProteinPhysicsEngine,
    MultiScaleTissueMorphogenesisEngine,
    VectorizedNLSOptimizerEngine
)

def main():
    parser = argparse.ArgumentParser(prog='aquamarine-dredge', description='DREDGE Non-Deterministic Quantum NP-Hard Suite (v58.0.0)')
    parser.add_argument('--exact-msa', nargs='+', help='Solve Exact N-Dimensional MSA: --exact-msa GATTACA GATCA GCATCA')
    parser.add_argument('--ab-initio', type=str, help='Compute Ab-Initio Protein Energy Landscape: --ab-initio MKWVTFISL')
    parser.add_argument('--tissue-morpho', action='store_true', help='Run Coupled Multi-Scale Stochastic-PDE Tissue Simulation')
    parser.add_argument('--nls-vectorized', nargs=2, metavar=('X_DATA', 'Y_DATA'), help='Vectorized Levenberg-Marquardt Parameter Fit')
    parser.add_argument('--test', action='store_true', help='Run unit tests')

    args = parser.parse_args()

    if args.test:
        suite = unittest.defaultTestLoader.discover('tests')
        unittest.TextTestRunner(verbosity=2).run(suite)
        return

    if args.exact_msa:
        res = ExactMultiSequenceAlignmentEngine.align_exact_nd(args.exact_msa)
        if "error" in res:
            print(f"\n[Error] {res['error']}\n")
        else:
            print(f"\n • Exact Optimal MSA Score: {res['exact_optimal_score']} (Volume: {res['state_space_volume']} cells)\n • Guarantee: {res['algorithmic_guarantee']}\n")
        return

    if args.ab_initio:
        res = AbInitioProteinPhysicsEngine.compute_energy_landscape(args.ab_initio)
        print(f"\n • Ab-Initio Physics Energy: {res['total_conformational_energy']} (LJ: {res['lennard_jones_potential_kcal_mol']} kcal/mol, Torsion: {res['ramachandran_torsion_energy_kcal_mol']})\n • State: {res['folding_state']}\n")
        return

    if args.tissue_morpho:
        res = MultiScaleTissueMorphogenesisEngine.simulate_tissue_coupling(grid_size=16, time_steps=40)
        print(f"\n • Multi-Scale Morphogenesis: Field Mean={res['macro_activator_field_mean']} | Stochastic Jumps={res['micro_stochastic_jump_events']} | Viable Cells={res['total_viable_cells_in_tissue']}\n")
        return

    if args.nls_vectorized:
        x = [float(val.strip()) for val in args.nls_vectorized[0].split(',')]
        y = [float(val.strip()) for val in args.nls_vectorized[1].split(',')]
        res = VectorizedNLSOptimizerEngine.optimize_fit(x, y)
        print(f"\n • Vectorized Fit: {res['optimized_parameters']} | R^2 = {res['coefficient_of_determination_R2']} ({res['convergence_status']})\n")
        return

    parser.print_help()

if __name__ == '__main__':
    main()
