import argparse
import sys
import unittest
import numpy as np
from dredge.bio_kernel import (
    ParallelFMIndexEngine,
    Constrained3DRNAEngine,
    GillespieStochasticKineticsEngine,
    JukesCantorMLEngine,
    DeBruijnGraphCorrectionEngine,
    EpigeneticShannonEntropyEngine
)

def main():
    parser = argparse.ArgumentParser(prog='aquamarine-dredge', description='DREDGE Domain-Breaker Suite (v54.0.0)')
    parser.add_argument('--parallel-fm', nargs='+', help='Usage: --parallel-fm <TEXT> <PAT1> <PAT2> ...')
    parser.add_argument('--rna-3d', type=str, help='3D Constrained Nussinov Folding for sequence')
    parser.add_argument('--gillespie', action='store_true', help='Run Stochastic Gillespie Enzyme Simulation')
    parser.add_argument('--jc69-ml', nargs=2, metavar=('SEQ1', 'SEQ2'), help='Jukes-Cantor Maximum Likelihood Branch Estimation')
    parser.add_argument('--debruijn-correct', nargs='+', help='Correct reads via de Bruijn Graph: --debruijn-correct <READ1> <READ2> ...')
    parser.add_argument('--meth-entropy', nargs='+', help='Shannon Methylation Entropy: --meth-entropy 1100 1100 1010 1111')
    parser.add_argument('--test', action='store_true', help='Run Tests')

    args = parser.parse_args()

    if args.test:
        suite = unittest.defaultTestLoader.discover('tests')
        unittest.TextTestRunner(verbosity=2).run(suite)
        return

    if args.parallel_fm:
        text = args.parallel_fm[0]
        pats = args.parallel_fm[1:]
        res = ParallelFMIndexEngine.parallel_search(text, pats)
        print(f"\n • Multithreaded FM Results: {res['match_results']} | Model: {res['engine']}\n")
        return

    if args.rna_3d:
        n = len(args.rna_3d)
        dist_mat = [[abs(i - j) * 3.8 for j in range(n)] for i in range(n)]
        res = Constrained3DRNAEngine.fold_with_spatial_constraints(args.rna_3d, dist_mat)
        print(f"\n • 3D Constrained Nussinov Score: {res['max_constrained_energy_score']} | Model: {res['folding_model']}\n")
        return

    if args.gillespie:
        res = GillespieStochasticKineticsEngine.simulate_enzyme_system(s_init=500, e_init=50)
        print(f"\n • Gillespie Markov Chain: {res['total_reaction_events']} Events | Final Product: {res['final_product_formed']} | Remaining Substrate: {res['final_substrate_remaining']}\n")
        return

    if args.jc69-ml if False else args.jc69_ml:
        res = JukesCantorMLEngine.calculate_branch_ml(args.jc69_ml[0], args.jc69_ml[1])
        print(f"\n • JC69 ML Branch Length (t): {res['maximum_likelihood_branch_t']} | Log-Likelihood: {res['log_likelihood']} (p-dist: {res['p_distance']})\n")
        return

    if args.debruijn_correct:
        res = DeBruijnGraphCorrectionEngine.error_correct(args.debruijn_correct, k=3, min_coverage=2)
        print(f"\n • de Bruijn Correction: {res['corrections_made']} Fixes | Corrected: {res['corrected_reads']}\n")
        return

    if args.meth_entropy:
        res = EpigeneticShannonEntropyEngine.calculate_methylation_entropy(args.meth_entropy)
        print(f"\n • Shannon Epigenetic Entropy: {res['shannon_entropy_bits']} bits (Norm: {res['normalized_entropy']}) | Status: {res['epigenetic_status']}\n")
        return

    parser.print_help()

if __name__ == '__main__':
    main()
