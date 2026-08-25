import argparse
import sys
import unittest
from dredge.bio_kernel import (
    PureThermodynamicsEngine, 
    PureBiochemistryProteinEngine, 
    PureMolecularGenomicsEngine,
    PureEnzymeKineticsEngine,
    PureBufferEquilibriumEngine,
    PureSpectrophotometryEngine
)

def main():
    parser = argparse.ArgumentParser(
        prog="aquamarine-dredge",
        description="DREDGE Pure Sciences (v48.0.0): Analytical Biochemistry, Kinetics & Biophysics"
    )
    parser.add_argument("--version", action="version", version="aquamarine-dredge 48.0.0")
    
    # Pure Chemistry & Biophysics Commands
    parser.add_argument("--dna-tm", type=str, default=None, help="Calculate Nearest-Neighbor DNA Melting Temp (Tm)")
    parser.add_argument("--protein-pi", type=str, default=None, help="Calculate Isoelectric Point (pI) & Hydropathy")
    parser.add_argument("--translate", type=str, default=None, help="Exact In-Silico Translation to Peptide")
    parser.add_argument("--buffer", nargs=3, type=float, metavar=('pKa', '[A-]', '[HA]'), help="Calculate Buffer pH (Henderson-Hasselbalch)")
    parser.add_argument("--spec", nargs=2, type=float, metavar=('A260', 'A280'), help="Quantify DNA/RNA Concentration & Purity (A260/A280)")
    parser.add_argument("--test", action="store_true", help="Run automated test suite for all biophysical laws")
    parser.add_argument("--cite", action="store_true", help="Print official scientific BibTeX citation")

    args = parser.parse_args()

    if args.test:
        print("\n" + "="*70)
        print("  🧪 EXECUTING AUTOMATED BIOPHYSICAL UNIT-TEST SUITE")
        print("="*70)
        suite = unittest.defaultTestLoader.discover('tests')
        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(suite)
        print("="*70 + "\n")
        return

    if args.dna_tm:
        res = PureThermodynamicsEngine.calculate_melting_temp(args.dna_tm)
        print(f"\n • DNA Tm: {res['melting_temperature_Tm']} | ΔG (37°C): {res['gibbs_free_energy_dG_37C']}\n")
        return

    if args.protein_pi:
        res = PureBiochemistryProteinEngine.calculate_isoelectric_point(args.protein_pi)
        print(f"\n • Protein pI: {res['isoelectric_point_pI']} | Net Charge: {res['net_charge_physiological_pH7_4']} e\n")
        return

    if args.translate:
        res = PureMolecularGenomicsEngine.translate(args.translate)
        print(f"\n • Peptide: {res}\n")
        return

    if args.buffer:
        res = PureBufferEquilibriumEngine.calculate_buffer_ph(args.buffer[0], args.buffer[1], args.buffer[2])
        print("\n" + "="*70)
        print("  🧪 HENDERSON-HASSELBALCH BUFFER EQUILIBRIUM")
        print("="*70)
        print(f" • Input pKa         : {res['pka']}")
        print(f" • [A-] / [HA] Ratio : {res['base_to_acid_ratio']}")
        print(f" • Equilibrium pH    : {res['equilibrium_ph']}")
        print(f" • Buffer Status     : {res['buffer_capacity_status']}")
        print("="*70 + "\n")
        return

    if args.spec:
        res = PureSpectrophotometryEngine.quantify_nucleic_acid(args.spec[0], args.spec[1])
        print("\n" + "="*70)
        print("  🔬 NUCLEIC ACID SPECTROPHOTOMETRY & PURITY")
        print("="*70)
        print(f" • Concentration     : {res['concentration_ng_ul']} ng/uL")
        print(f" • A260 / A280 Ratio : {res['purity_ratio_A260_A280']}")
        print(f" • Quality Status    : {res['purity_assessment']}")
        print("="*70 + "\n")
        return

    if args.cite:
        print("""@article{santaluccia1998,
  title={A unified view of polymer, dumbbell, and oligonucleotide DNA nearest-neighbor thermodynamics},
  author={SantaLucia, John},
  journal={Proceedings of the National Academy of Sciences},
  volume={95},
  number={4},
  pages={1460--1465},
  year={1998}
}""")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
