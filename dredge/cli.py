import argparse
import sys
from dredge.shell import start_interactive_shell
from dredge.core import DREDGEResearchPipeline
from dredge.bio_kernel import (
    UniversalBioKernel, 
    SequenceAlignmentEngine, 
    MolecularDockingEngine, 
    PharmacologyScreener, 
    ClinicalDiagnosticEngine,
    NovelDiseaseDiscoveryEngine,
    SyntheticBiologyCircuit,
    EpidemiologicalViralEngine,
    GenerativeProteinDesigner
)

def main():
    if len(sys.argv) == 1:
        start_interactive_shell()
        return

    parser = argparse.ArgumentParser(
        prog="aquamarine-dredge",
        description="DREDGE Singularity (v8.0.0): The Ultimate Universal Biological OS"
    )
    parser.add_argument("--version", action="version", version="aquamarine-dredge 8.0.0")
    parser.add_argument("--shell", action="store_true", help="Launch the Interactive Bio-Shell (REPL)")
    parser.add_argument("--design-protein", type=str, default=None, help="De-novo design therapeutic protein sequence")
    parser.add_argument("--circuit", action="store_true", help="Simulate Synthetic Genetic Toggle Switch")
    parser.add_argument("--outbreak", action="store_true", help="Simulate SEIR Viral Outbreak")
    parser.add_argument("--discover", nargs="+", help="Discover novel syndromes from symptoms")
    parser.add_argument("--diagnose", type=str, default=None, help="Diagnose disease risk via Gene Variant")
    parser.add_argument("--drug", type=str, default=None, help="Screen drug for Lipinski RO5 & ADMET")
    parser.add_argument("--dock", type=str, default=None, help="Simulate 3D Molecular Drug Docking")
    parser.add_argument("--crispr", type=str, default=None, help="Design CRISPR-Cas9 gRNA candidates")
    parser.add_argument("--align", nargs=2, metavar=('SEQ1', 'SEQ2'), help="Align DNA sequences")
    parser.add_argument("--analyze-seq", type=str, default=None, help="DNA Sequence Analysis")
    parser.add_argument("--run", action="store_true", help="Execute Epigenetic Reversal Simulation")
    parser.add_argument("--trial", type=int, default=0, help="Run Cohort Clinical Trial")
    parser.add_argument("--benchmark", action="store_true", help="Run Hardware Benchmarks")
    parser.add_argument("--cite", action="store_true", help="Print BibTeX citation")

    args = parser.parse_args()

    if args.shell:
        start_interactive_shell()
        return

    # Fallback to single command runs
    if args.drug:
        res = PharmacologyScreener.analyze_molecule(args.drug)
        print(f"\n • Compound: {res['compound_name']} | Status: {res['lipinski_ro5_status']}\n")
    elif args.diagnose:
        res = ClinicalDiagnosticEngine.diagnose_variant(args.diagnose)
        print(f"\n • Gene: {res['biomarker_gene']} | Pathology: {res['associated_pathology']}\n")
    elif args.cite:
        print("""@software{aquamarine_dredge_2026,
  author = {Hoshino, Aquamarine},
  title = {DREDGE Singularity: The Complete Universal Biological OS},
  year = {2026},
  url = {https://pypi.org/project/aquamarine-dredge/}
}""")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
