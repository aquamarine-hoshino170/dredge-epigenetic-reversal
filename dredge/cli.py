import argparse
import sys
import unittest
from dredge.bio_kernel import (
    GrandFinaleBioEngine,
    FMIndexBwtEngine,
    AdaptivePhredTrimmerEngine,
    NonLinearKineticsEngine,
    ExactTreeBranchEngine,
    PureThermodynamicsEngine
)

def main():
    parser = argparse.ArgumentParser(prog='aquamarine-dredge', description='DREDGE Grand Finale Scientific CLI (v53.0.0)')
    parser.add_argument('--sw-full', nargs=2, metavar=('SEQ1', 'SEQ2'), help='Smith-Waterman Full 3-State Affine Matrices')
    parser.add_argument('--fm-search', nargs=2, metavar=('PATTERN', 'TEXT'), help='FM-Index Exact Pattern Search')
    parser.add_argument('--adaptive-qc', nargs=2, metavar=('SEQ', 'QUAL'), help='Adaptive Variance-Aware FastQ Trimmer')
    parser.add_argument('--nls-kinetics', nargs=2, metavar=('SUBS', 'VELS'), help='Direct Non-Linear Michaelis-Menten Fit')
    parser.add_argument('--upgma-exact', type=str, help='UPGMA Tree with Branch Verification')
    parser.add_argument('--test', action='store_true', help='Run Tests')

    args = parser.parse_args()

    if args.test:
        suite = unittest.defaultTestLoader.discover('tests')
        unittest.TextTestRunner(verbosity=2).run(suite)
        return

    if args.sw_full:
        res = GrandFinaleBioEngine.smith_waterman_full_affine(args.sw_full[0], args.sw_full[1])
        print("\n" + "="*50)
        print("  SMITH-WATERMAN FULL AFFINE GAP MATRICES")
        print("="*50)
        print(f" • Max Score: {res['max_score']} at Peak {res['peak_coordinate']}")
        print(f" • Aligned Strand 1: {res['local_align_seq1']}")
        print(f" • Aligned Strand 2: {res['local_align_seq2']}\n" + "="*50 + "\n")
        return

    if args.fm_search:
        res = FMIndexBwtEngine.count_pattern(args.fm_search[0], args.fm_search[1])
        print(f"\n • FM-Index Search '{res['pattern']}': {res['occurrences']} Matches | Status: {res['status']}\n")
        return

    if args.adaptive_qc:
        res = AdaptivePhredTrimmerEngine.adaptive_trim(args.adaptive_qc[0], args.adaptive_qc[1])
        print(f"\n • Adaptive QC: {res['original_length']}bp -> {res['trimmed_length']}bp (Dropped: {res['data_drop_pct']}) | Mean Phred: Q{res['overall_phred_mean']} ± {res['overall_phred_std']}\n")
        return

    if args.nls_kinetics:
        subs = [float(x.strip()) for x in args.nls_kinetics[0].split(',')]
        vels = [float(x.strip()) for x in args.nls_kinetics[1].split(',')]
        res = NonLinearKineticsEngine.fit_direct_nls(subs, vels)
        print(f"\n • Direct NLS Fit: Vmax = {res['v_max']} uM/min | Km = {res['k_m']} uM (R^2 = {res['r_squared']})\n")
        return

    if args.upgma_exact:
        parts = args.upgma_exact.split('|')
        taxa = [t.strip() for t in parts[0].split(',')]
        mat = [[float(x) for x in r.split(',')] for r in parts[1].split(';')]
        res = ExactTreeBranchEngine.construct_verified_upgma(taxa, mat)
        print(f"\n • Exact Branch Tree: {res['newick_tree']} (Root Height: {res['root_tree_height']})\n")
        return

    parser.print_help()

if __name__ == '__main__':
    main()
