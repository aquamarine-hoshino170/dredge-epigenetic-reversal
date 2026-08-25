import argparse
import sys
from dredge.bio_kernel import (
    UniversalBioKernel, 
    SequenceAlignmentEngine, 
    GenIntelBioinformaticsEngine, 
    UnifiedPsiEMAMasterEngine, 
    AutonomousCodeSynthesizerEngine
)

def main():
    parser = argparse.ArgumentParser(
        prog="aquamarine-dredge",
        description="DREDGE Pure Scientific (v46.0.0): Computational Genomics & Algorithmic Bio-Engine"
    )
    parser.add_argument("--version", action="version", version="aquamarine-dredge 46.0.0")
    
    # Real Scientific Flags
    parser.add_argument("--transcribe", type=str, default=None, help="Transcribe DNA sequence to mRNA")
    parser.add_argument("--translate", type=str, default=None, help="Translate nucleotide sequence into Amino Acid Peptide")
    parser.add_argument("--align", nargs=2, metavar=('SEQ1', 'SEQ2'), help="Run Smith-Waterman Local Sequence Alignment")
    parser.add_argument("--genintel", "-gi", type=str, default=None, help="Fetch real gene data and analyze from NCBI (e.g. BRCA1, TP53)")
    parser.add_argument("--psi-ema", type=str, default=None, help="Compute Unified Psi_EMA Master Invariant on DNA sequence")
    parser.add_argument("--code", type=str, default=None, help="Synthesize clean scientific algorithm code")
    parser.add_argument("--sandbox", type=str, default=None, help="Execute Python script in isolated runtime sandbox")
    parser.add_argument("--cite", action="store_true", help="Print official scientific BibTeX citation")

    args = parser.parse_args()

    if args.transcribe:
        res = UniversalBioKernel.transcribe(args.transcribe)
        print(f"\n • mRNA: {res}\n")
        return

    if args.translate:
        res = UniversalBioKernel.translate(args.translate)
        print(f"\n • Peptide: {res}\n")
        return

    if args.align:
        res = SequenceAlignmentEngine.local_align(args.align[0], args.align[1])
        print("\n" + "="*70)
        print("  🧬 SMITH-WATERMAN LOCAL SEQUENCE ALIGNMENT")
        print("="*70)
        print(f" • Score       : {res['alignment_score']}")
        print(f" • Max Identity: {res['max_identity_pct']}%")
        print("="*70 + "\n")
        return

    if args.genintel:
        res = GenIntelBioinformaticsEngine.analyze_gene(args.genintel)
        print("\n" + "="*70)
        print("  🧬 GENINTEL: NCBI GENOME DATA ANALYSIS")
        print("="*70)
        print(f" • Gene Symbol   : {res['gene_symbol']}")
        print(f" • Entrez ID     : {res['ncbi_gene_id']}")
        print(f" • Sequence Len  : {res['sequence_length_bp']} bp")
        print(f" • GC Content    : {res['gc_content']}")
        print(f" • Peptide Sample: {res['synthesized_peptide']}")
        print("="*70 + "\n")
        return

    if args.psi_ema:
        res = UnifiedPsiEMAMasterEngine.compute_psi_ema(args.psi_ema)
        print("\n" + "="*70)
        print("  ♾️ UNIFIED Ψ_EMA MASTER INVARIANT ENGINE")
        print("="*70)
        print(f" • Formula        : {res['mathematical_formula']}")
        print(f" • Input Sequence : {res['input_length']}")
        print(f" • Minimizer Seeds: {res['minimizer_seeds']}")
        print(f" • Polar Bias     : {res['polar_phase_bias']}")
        print(f" • Latent Tensor  : {res['tensor_shape']}")
        print(f" • Convergence    : {res['convergence_confidence']}")
        print("="*70 + "\n")
        return

    if args.code:
        res = AutonomousCodeSynthesizerEngine.synthesize_code(args.code)
        print(f"\n[Synthesized {res['language']} Code]:\n{res['code']}\n")
        return

    if args.sandbox:
        res = AutonomousCodeSynthesizerEngine.run_sandbox(args.sandbox)
        print(f"\n[Sandbox Output]:\n{res['output']}\n")
        return

    if args.cite:
        print("""@software{aquamarine_dredge_2026,
  author = {Hoshino, Aquamarine},
  title = {DREDGE: High-Performance Computational Genomics & Invariant Bio-Framework},
  year = {2026},
  url = {https://pypi.org/project/aquamarine-dredge/}
}""")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
