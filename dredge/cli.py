import argparse
import sys
import unittest
import numpy as np
from dredge.bio_kernel import (
    PureThermodynamicsEngine,
    PureBiochemistryProteinEngine,
    PureMolecularGenomicsEngine,
    PureEnzymeKineticsEngine,
    PureBufferEquilibriumEngine,
    PureSpectrophotometryEngine,
    BigDataGenomicsEngine,
    FastqQualityFilterEngine,
    PopulationGeneticsEngine,
    RNASecondaryStructureEngine,
    EnzymeInhibitionEngine,
    PhylogeneticTreeEngine,
    GeneticLinkageMappingEngine,
    AllostericCooperativityEngine,
    AdvancedAlignmentEngine,
    InverseBwtDecoderEngine,
    SangerSlidingWindowQCEngine
)

def main():
    parser = argparse.ArgumentParser(prog='aquamarine-dredge', description='DREDGE Bio-Mathematical & Genomics Challenge Core (v52.0.0)')
    parser.add_argument('--version', action='version', version='aquamarine-dredge 52.0.0')
    parser.add_argument('--sw-affine', nargs=2, metavar=('SEQ1', 'SEQ2'), help='Smith-Waterman with Affine Gap Penalty')
    parser.add_argument('--nw-visual', nargs=2, metavar=('SEQ1', 'SEQ2'), help='Needleman-Wunsch with Matrix & Backtrack')
    parser.add_argument('--bwt-decode', type=str, default=None, help='Decode BWT String via LF-Mapping')
    parser.add_argument('--window-qc', nargs=2, metavar=('SEQ', 'QUAL'), help='Sliding Window FastQ QC Trimming')
    parser.add_argument('--upgma-matrix', type=str, help='UPGMA Tree from CSV (Format: Taxa:A,B,C|Matrix:0,2,4;2,0,4;4,4,0)')
    parser.add_argument('--kinetics-fit', nargs=2, metavar=('SUBSTRATES', 'VELOCITIES'), help='CSV Substrates & Velocities Fit')
    parser.add_argument('--test', action='store_true', help='Run unit tests')

    args = parser.parse_args()

    if args.test:
        print('\n=== RUNNING SCIENTIFIC TEST SUITE ===')
        suite = unittest.defaultTestLoader.discover('tests')
        unittest.TextTestRunner(verbosity=2).run(suite)
        print('=====================================\n')
        return

    if args.sw_affine:
        res = AdvancedAlignmentEngine.smith_waterman_affine(args.sw_affine[0], args.sw_affine[1])
        print(f"\n • Affine SW Score: {res['max_alignment_score']} | Peak: {res['peak_position']} | Model: {res['gap_penalty_model']}\n")
        return

    if args.nw_visual:
        res = AdvancedAlignmentEngine.needleman_wunsch_visual(args.nw_visual[0], args.nw_visual[1])
        print("\n" + "="*50)
        print("  NEEDLEMAN-WUNSCH DYNAMIC PROGRAMMING MATRIX")
        print("="*50)
        print(res['matrix_ascii'])
        print("\n • Optimal Alignment:")
        print(f"   Seq1: {res['aligned_seq1']}")
        print(f"   Seq2: {res['aligned_seq2']}")
        print(f" • Score: {res['score']}\n" + "="*50 + "\n")
        return

    if args.bwt_decode:
        res = InverseBwtDecoderEngine.decode_bwt(args.bwt_decode)
        print(f"\n • Decoded BWT: {res['decoded_sequence']} ({res['status']})\n")
        return

    if args.window_qc:
        res = SangerSlidingWindowQCEngine.trim_sliding_window(args.window_qc[0], args.window_qc[1])
        print(f"\n • Sliding Window QC: {res['original_length']}bp -> {res['trimmed_length']}bp | Dropped: {res['bases_dropped']} bases\n   Trimmed: {res['trimmed_sequence']}\n")
        return

    if args.upgma_matrix:
        # Expected format: "A,B,C|0,2,4;2,0,4;4,4,0"
        parts = args.upgma_matrix.split('|')
        taxa = [t.strip() for t in parts[0].split(',')]
        rows = parts[1].split(';')
        mat = [[float(x) for x in r.split(',')] for r in rows]
        res = PhylogeneticTreeEngine.construct_upgma_tree(taxa, mat)
        print(f"\n • Parsed UPGMA Tree: {res['newick_tree_representation']}\n")
        return

    if args.kinetics_fit:
        subs = [float(x) for x in args.kinetics_fit[0].split(',')]
        vels = [float(x) for x in args.kinetics_fit[1].split(',')]
        res = PureEnzymeKineticsEngine.fit_lineweaver_burk(subs, vels)
        print(f"\n • Kinetics Fit: Vmax = {res['v_max']} uM/min | Km = {res['k_m']} uM | R^2 = {res['r_squared']}\n")
        return

    parser.print_help()

if __name__ == '__main__':
    main()
