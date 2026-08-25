import argparse
import sys
from dredge.bio_kernel import (
    PureThermodynamicsEngine, 
    PureBiochemistryProteinEngine, 
    PureMolecularGenomicsEngine
)

def main():
    parser = argparse.ArgumentParser(
        prog="aquamarine-dredge",
        description="DREDGE Pure Sciences (v47.0.0): Biophysical Thermodynamics, Protein Chemistry & Genomic Algorithms"
    )
    parser.add_argument("--version", action="version", version="aquamarine-dredge 47.0.0")
    
    # Pure Biophysics & Biochemistry
    parser.add_argument("--dna-tm", type=str, default=None, help="Calculate Nearest-Neighbor DNA Melting Temp (Tm) & Gibbs Free Energy (dG)")
    parser.add_argument("--protein-pi", type=str, default=None, help="Calculate Isoelectric Point (pI), Net Charge at pH 7.4 & Hydropathy")
    parser.add_argument("--translate", type=str, default=None, help="Exact Ribosomal In-Silico Translation to Peptide")
    parser.add_argument("--align", nargs=2, metavar=('SEQ1', 'SEQ2'), help="Run Smith-Waterman Local Sequence Alignment")
    parser.add_argument("--cite", action="store_true", help="Print official scientific BibTeX citation")

    args = parser.parse_args()

    if args.dna_tm:
        res = PureThermodynamicsEngine.calculate_melting_temp(args.dna_tm)
        print("\n" + "="*70)
        print("  🔬 DNA NEAREST-NEIGHBOR THERMODYNAMICS (SantaLucia 1998)")
        print("="*70)
        print(f" • Sequence Length : {res['sequence_length']}")
        print(f" • Enthalpy (ΔH)   : {res['enthalpy_dH_kcal_mol']} kcal/mol")
        print(f" • Entropy (ΔS)    : {res['entropy_dS_cal_K_mol']} cal/(K·mol)")
        print(f" • Free Energy (ΔG): {res['gibbs_free_energy_dG_37C']}")
        print(f" • Melting Temp Tm : {res['melting_temperature_Tm']}")
        print(f" • Thermodynamic   : {res['thermodynamic_state']}")
        print("="*70 + "\n")
        return

    if args.protein_pi:
        res = PureBiochemistryProteinEngine.calculate_isoelectric_point(args.protein_pi)
        print("\n" + "="*70)
        print("  🧪 PROTEIN BIOCHEMISTRY & TITRATION PROFILE")
        print("="*70)
        print(f" • Peptide Length  : {res['peptide_length']} aa")
        print(f" • Isoelectric pI  : {res['isoelectric_point_pI']}")
        print(f" • Net Charge pH7.4: {res['net_charge_physiological_pH7_4']} e")
        print(f" • GRAVY Hydropathy: {res['gravy_hydrophobicity_index']}")
        print(f" • Physical Nature : {res['biophysical_nature']}")
        print("="*70 + "\n")
        return

    if args.translate:
        res = PureMolecularGenomicsEngine.translate(args.translate)
        print(f"\n • Peptide: {res}\n")
        return

    if args.align:
        res = PureMolecularGenomicsEngine.smith_waterman_align(args.align[0], args.align[1])
        print("\n" + "="*70)
        print("  🧬 SMITH-WATERMAN DYNAMIC PROGRAMMING ALIGNMENT")
        print("="*70)
        print(f" • Alignment Score : {res['optimal_alignment_score']}")
        print(f" • Matrix Shape    : {res['sequence_matrix_shape']}")
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
