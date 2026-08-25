import argparse
import sys
import unittest
from dredge.bio_kernel import (
    PureThermodynamicsEngine,
    PureEnzymeKineticsEngine,
    PhylogeneticTreeEngine,
    AdvancedAlignmentEngine,
    InverseBwtDecoderEngine,
    SangerSlidingWindowQCEngine
)

def main():
    parser = argparse.ArgumentParser(prog='aquamarine-dredge', description='DREDGE Bio-Mathematical Core')
    parser.add_argument('--bwt-decode', type=str, default=None, help='Decode BWT String')
    parser.add_argument('--sw-affine', nargs=2, metavar=('SEQ1', 'SEQ2'), help='Affine Smith-Waterman')
    parser.add_argument('--nw-visual', nargs=2, metavar=('SEQ1', 'SEQ2'), help='Needleman-Wunsch Visual')
    parser.add_argument('--window-qc', nargs=2, metavar=('SEQ', 'QUAL'), help='Sliding Window QC')
    parser.add_argument('--upgma-matrix', type=str, help='UPGMA Tree')
    parser.add_argument('--kinetics-fit', nargs=2, metavar=('SUBSTRATES', 'VELOCITIES'), help='Kinetics Fit')
    parser.add_argument('--test', action='store_true', help='Run Tests')

    args = parser.parse_args()

    if args.test:
        suite = unittest.defaultTestLoader.discover('tests')
        unittest.TextTestRunner(verbosity=2).run(suite)
        return

    if args.kinetics_fit:
        subs = [float(x.strip()) for x in args.kinetics_fit[0].split(',')]
        vels = [float(x.strip()) for x in args.kinetics_fit[1].split(',')]
        res = PureEnzymeKineticsEngine.fit_lineweaver_burk(subs, vels)
        print(f"\n • Lineweaver-Burk Fit: Vmax = {res['v_max']} uM/min | Km = {res['k_m']} uM | R^2 = {res['r_squared']}\n")
        return

    if args.bwt_decode:
        res = InverseBwtDecoderEngine.decode_bwt(args.bwt_decode)
        if "error" in res:
            print(f"\n[Error] {res['error']}\n")
        else:
            print(f"\n • Decoded BWT: {res['decoded_sequence']} ({res['status']})\n")
        return

    if args.sw_affine:
        res = AdvancedAlignmentEngine.smith_waterman_affine(args.sw_affine[0], args.sw_affine[1])
        print(f"\n • Affine SW Score: {res['max_alignment_score']}\n")
        return

    if args.nw_visual:
        res = AdvancedAlignmentEngine.needleman_wunsch_visual(args.nw_visual[0], args.nw_visual[1])
        print(f"\n • Score: {res['score']}\n   Align1: {res['aligned_seq1']}\n   Align2: {res['aligned_seq2']}\n")
        return

    if args.window_qc:
        res = SangerSlidingWindowQCEngine.trim_sliding_window(args.window_qc[0], args.window_qc[1])
        print(f"\n • Trimmed ({res['original_length']} -> {res['trimmed_length']}): {res['trimmed_sequence']}\n")
        return

    if args.upgma_matrix:
        parts = args.upgma_matrix.split('|')
        taxa = [t.strip() for t in parts[0].split(',')]
        mat = [[float(x) for x in r.split(',')] for r in parts[1].split(';')]
        res = PhylogeneticTreeEngine.construct_upgma_tree(taxa, mat)
        print(f"\n • Newick Tree: {res['newick_tree_representation']}\n")
        return

    parser.print_help()

if __name__ == '__main__':
    main()
