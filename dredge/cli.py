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
    BigDataGenomicsEngine
)

def main():
    parser = argparse.ArgumentParser(prog='aquamarine-dredge', description='DREDGE Pure Sciences & Big Data (v49.0.0)')
    parser.add_argument('--version', action='version', version='aquamarine-dredge 49.0.0')
    parser.add_argument('--dna-tm', type=str, default=None, help='DNA Melting Temp')
    parser.add_argument('--protein-pi', type=str, default=None, help='Protein pI & Hydropathy')
    parser.add_argument('--translate', type=str, default=None, help='DNA Translation')
    parser.add_argument('--buffer', nargs=3, type=float, metavar=('pKa', '[A-]', '[HA]'), help='Buffer pH')
    parser.add_argument('--spec', nargs=2, type=float, metavar=('A260', 'A280'), help='Purity A260/A280')
    parser.add_argument('--bwt', type=str, default=None, help='Run Burrows-Wheeler Transform')
    parser.add_argument('--global-align', nargs=2, metavar=('SEQ1', 'SEQ2'), help='Needleman-Wunsch Global Alignment')
    parser.add_argument('--test', action='store_true', help='Run unit tests')

    args = parser.parse_args()

    if args.test:
        print('\n=== RUNNING SCIENTIFIC TEST SUITE ===')
        suite = unittest.defaultTestLoader.discover('tests')
        unittest.TextTestRunner(verbosity=2).run(suite)
        print('=====================================\n')
        return

    if args.bwt:
        res = BigDataGenomicsEngine.burrows_wheeler_transform(args.bwt)
        print(f"\n • BWT String: {res['bwt_transformed']} | Density: {res['compression_readiness']}\n")
        return

    if args.global_align:
        res = BigDataGenomicsEngine.needleman_wunsch_global_align(args.global_align[0], args.global_align[1])
        print(f"\n • Global Alignment Score: {res['global_alignment_score']} | Shape: {res['alignment_dimensions']}\n")
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
        print(f"\n • Buffer pH: {res['equilibrium_ph']} | Status: {res['buffer_capacity_status']}\n")
        return

    if args.spec:
        res = PureSpectrophotometryEngine.quantify_nucleic_acid(args.spec[0], args.spec[1])
        print(f"\n • Concentration: {res['concentration_ng_ul']} ng/uL | Ratio: {res['purity_ratio_A260_A280']} ({res['purity_assessment']})\n")
        return

    parser.print_help()

if __name__ == '__main__':
    main()
