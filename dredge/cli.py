import argparse
import sys
import unittest
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
    EnzymeInhibitionEngine
)

def main():
    parser = argparse.ArgumentParser(prog='aquamarine-dredge', description='DREDGE Pure Sciences, Genetics & Biophysics (v50.0.0)')
    parser.add_argument('--version', action='version', version='aquamarine-dredge 50.0.0')
    parser.add_argument('--dna-tm', type=str, default=None, help='DNA Melting Temp')
    parser.add_argument('--protein-pi', type=str, default=None, help='Protein pI & Hydropathy')
    parser.add_argument('--translate', type=str, default=None, help='DNA Translation')
    parser.add_argument('--buffer', nargs=3, type=float, metavar=('pKa', '[A-]', '[HA]'), help='Buffer pH')
    parser.add_argument('--spec', nargs=2, type=float, metavar=('A260', 'A280'), help='Purity A260/A280')
    parser.add_argument('--bwt', type=str, default=None, help='Burrows-Wheeler Transform')
    parser.add_argument('--global-align', nargs=2, metavar=('SEQ1', 'SEQ2'), help='Needleman-Wunsch Global Alignment')
    parser.add_argument('--fastq-qc', nargs=2, metavar=('SEQUENCE', 'QUAL_STRING'), help='FastQ QC Phred Score')
    parser.add_argument('--hardy-weinberg', nargs=3, type=int, metavar=('AA', 'Aa', 'aa'), help='Hardy-Weinberg Genotypes')
    parser.add_argument('--rna-fold', type=str, default=None, help='Nussinov RNA Secondary Structure Fold')
    parser.add_argument('--inhibition', nargs=5, metavar=('Vmax', 'Km', '[I]', 'Ki', 'Mode'), help='Enzyme Inhibition Kinetics')
    parser.add_argument('--test', action='store_true', help='Run unit tests')

    args = parser.parse_args()

    if args.test:
        print('\n=== RUNNING SCIENTIFIC TEST SUITE ===')
        suite = unittest.defaultTestLoader.discover('tests')
        unittest.TextTestRunner(verbosity=2).run(suite)
        print('=====================================\n')
        return

    if args.hardy_weinberg:
        res = PopulationGeneticsEngine.calculate_hardy_weinberg(args.hardy_weinberg[0], args.hardy_weinberg[1], args.hardy_weinberg[2])
        print(f"\n • Alleles: p={res['allele_frequency_p']}, q={res['allele_frequency_q']} | Chi2: {res['chi_square_stat']} ({res['equilibrium_status']})\n")
        return

    if args.rna_fold:
        res = RNASecondaryStructureEngine.nussinov_fold(args.rna_fold)
        print(f"\n • RNA Max Pairs: {res['max_nested_base_pairs']} pairs ({res['paired_nucleotide_pct']}) | Shape: {res['structure_matrix_shape']}\n")
        return

    if args.inhibition:
        vmax, km, conc_i, ki = float(args.inhibition[0]), float(args.inhibition[1]), float(args.inhibition[2]), float(args.inhibition[3])
        mode = args.inhibition[4]
        res = EnzymeInhibitionEngine.calculate_inhibition(vmax, km, conc_i, ki, mode)
        print(f"\n • Apparent Vmax: {res['apparent_Vmax']} | Apparent Km: {res['apparent_Km']} | Eff. Loss: {res['efficiency_loss']}\n")
        return

    if args.fastq_qc:
        res = FastqQualityFilterEngine.filter_read(args.fastq_qc[0], args.fastq_qc[1])
        print(f"\n • FastQ QC Mean Phred: Q{res['mean_phred_score']} | Status: {res['quality_filter_status']}\n")
        return

    if args.bwt:
        res = BigDataGenomicsEngine.burrows_wheeler_transform(args.bwt)
        print(f"\n • BWT String: {res['bwt_transformed']}\n")
        return

    if args.global_align:
        res = BigDataGenomicsEngine.needleman_wunsch_global_align(args.global_align[0], args.global_align[1])
        print(f"\n • Global Score: {res['global_alignment_score']}\n")
        return

    if args.dna_tm:
        res = PureThermodynamicsEngine.calculate_melting_temp(args.dna_tm)
        print(f"\n • DNA Tm: {res['melting_temperature_Tm']} | dG: {res['gibbs_free_energy_dG_37C']}\n")
        return

    if args.protein_pi:
        res = PureBiochemistryProteinEngine.calculate_isoelectric_point(args.protein_pi)
        print(f"\n • Protein pI: {res['isoelectric_point_pI']} | Net Charge: {res['net_charge_physiological_pH7_4']} e\n")
        return

    if args.translate:
        print(f"\n • Peptide: {PureMolecularGenomicsEngine.translate(args.translate)}\n")
        return

    if args.buffer:
        res = PureBufferEquilibriumEngine.calculate_buffer_ph(args.buffer[0], args.buffer[1], args.buffer[2])
        print(f"\n • Buffer pH: {res['equilibrium_ph']}\n")
        return

    if args.spec:
        res = PureSpectrophotometryEngine.quantify_nucleic_acid(args.spec[0], args.spec[1])
        print(f"\n • Concentration: {res['concentration_ng_ul']} ng/uL\n")
        return

    parser.print_help()

if __name__ == '__main__':
    main()
