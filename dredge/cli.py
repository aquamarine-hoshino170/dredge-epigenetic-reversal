import argparse
import sys
import unittest
from dredge.bio_kernel import (
    MultithreadedBWTEngine,
    Constrained3DRNAEngine,
    GillespieStochasticKineticsEngine,
    JukesCantorMLEngine,
    DeBruijnGraphCorrectionEngine
)

def main():
    parser = argparse.ArgumentParser(prog='aquamarine-dredge', description='DREDGE Ultimate Theoretical Core (v57.0.0)')
    parser.add_argument('--bwt-parallel', nargs='+', help='Parallel BWT Search: --bwt-parallel <TEXT> <PAT1> <PAT2> ...')
    parser.add_argument('--rna-3d', type=str, help='3D Nussinov Folding with Distance Matrix')
    parser.add_argument('--gillespie-sim', action='store_true', help='Run Gillespie Continuous-Time Stochastic Simulation')
    parser.add_argument('--jc69-ml', nargs=2, metavar=('SEQ1', 'SEQ2'), help='Jukes-Cantor ML Branch Estimation')
    parser.add_argument('--debruijn-repair', nargs='+', help='de Bruijn Graph Error Repair: --debruijn-repair <R1> <R2> ...')
    parser.add_argument('--test', action='store_true', help='Run unit tests')

    args = parser.parse_args()

    if args.test:
        suite = unittest.defaultTestLoader.discover('tests')
        unittest.TextTestRunner(verbosity=2).run(suite)
        return

    if args.bwt_parallel:
        text = args.bwt_parallel[0]
        pats = args.bwt_parallel[1:]
        res = MultithreadedBWTEngine.parallel_bwt_search(text, pats)
        print(f"\n • Multithreaded BWT Matches: {res['matches']} | Model: {res['engine']}\n")
        return

    if args.rna_3d:
        n = len(args.rna_3d)
        dist_mat = [[abs(i - j) * 3.8 for j in range(n)] for i in range(n)]
        res = Constrained3DRNAEngine.fold_3d_constrained(args.rna_3d, dist_mat)
        print(f"\n • 3D Constrained Nussinov Score: {res['max_constrained_energy_score']} | Model: {res['folding_model']}\n")
        return

    if args.gillespie_sim:
        res = GillespieStochasticKineticsEngine.simulate_trajectory(s_init=600, e_init=60)
        print(f"\n • Gillespie Simulation: {res['total_stochastic_events']} Events | Product Formed: {res['final_product']} | Substrate Remaining: {res['final_substrate']}\n")
        return

    if args.jc69_ml:
        res = JukesCantorMLEngine.calculate_ml_branch(args.jc69_ml[0], args.jc69_ml[1])
        print(f"\n • JC69 ML Branch Length (t): {res['max_likelihood_branch_t']} | Log-Likelihood: {res['log_likelihood']} (p-dist: {res['p_distance']})\n")
        return

    if args.debruijn_repair:
        res = DeBruijnGraphCorrectionEngine.repair_reads(args.debruijn_repair, k=3, min_cov=2)
        print(f"\n • de Bruijn Repair: {res['corrections_applied']} Fixes Applied | Repaired Reads: {res['repaired_sequences']}\n")
        return

    parser.print_help()

if __name__ == '__main__':
    main()
