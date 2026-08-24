import sys
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
from dredge.core import DREDGEResearchPipeline

def start_interactive_shell():
    print("\n" + "="*76)
    print("  🧬 AQUAMARINE DREDGE: INTERACTIVE BIO-SHELL (REPL v8.0.0)")
    print("  Type 'help' for command matrix or 'exit' / 'quit' to close.")
    print("="*76 + "\n")

    while True:
        try:
            cmd = input("dredge-bio> ").strip()
            if not cmd:
                continue
            if cmd in ["exit", "quit", "q"]:
                print("[*] Exiting DREDGE Bio-Kernel. Goodbye!\n")
                break
            elif cmd == "help":
                print("""
Available Shell Directives:
  • seq <DNA>              : Central Dogma Translation & Hydrophobicity
  • crispr <DNA>           : Design CRISPR gRNA Targets
  • align <SEQ1> <SEQ2>    : Needleman-Wunsch Alignment
  • drug <Compound>        : Lipinski RO5 & ADMET Screener
  • dock <Protein> <Drug>  : 3D Protein-Ligand Molecular Docking
  • diagnose <Gene>        : Clinical Pathology & Risk Profile
  • discover <Symptoms...> : Novel Syndrome & Biomarker Discovery
  • design <Function>      : De-Novo Therapeutic Peptide Synthesis
  • circuit <iptg> <atc>   : Synthetic Toggle Switch Simulation
  • run [sites] [flux]     : In-Silico Epigenetic Reversal SDE
                """)
            elif cmd.startswith("seq "):
                dna = cmd.split(" ", 1)[1].strip()
                print(f" -> mRNA: {UniversalBioKernel.transcribe(dna)}")
                print(f" -> Protein: {UniversalBioKernel.translate(dna)}")
                print(f" -> GC: {UniversalBioKernel.calculate_gc_content(dna)}%")
            elif cmd.startswith("drug "):
                name = cmd.split(" ", 1)[1].strip()
                res = PharmacologyScreener.analyze_molecule(name)
                print(f" -> {res['compound_name']} | MW: {res['molecular_weight']} | Lipinski: {res['lipinski_ro5_status']}")
            elif cmd.startswith("diagnose "):
                gene = cmd.split(" ", 1)[1].strip()
                res = ClinicalDiagnosticEngine.diagnose_variant(gene)
                print(f" -> [{gene.upper()}] Pathology: {res['associated_pathology']}")
                print(f" -> Prevention: {res['preventive_strategy']}")
            elif cmd.startswith("design "):
                target = cmd.split(" ", 1)[1].strip()
                res = GenerativeProteinDesigner.design_therapeutic_peptide(target)
                print(f" -> Peptide: {res['peptide_sequence']} (ΔG: {res['predicted_binding_potency']} kcal/mol)")
            elif cmd.startswith("run"):
                pipe = DREDGEResearchPipeline(n_sites=5000)
                rep, _ = pipe.run_rejuvenation_pipeline(steps=150)
                print(f" -> Reversal Reclaimed: -{rep['biomarkers']['years_rejuvenated']} Years | Entropy Delta: {rep['biomarkers']['entropy_decay_percentage']}%")
            else:
                print(f"[!] Unknown directive: '{cmd}'. Type 'help' for command list.")
        except KeyboardInterrupt:
            print("\n[*] Interrupted. Type 'exit' to quit.")
        except Exception as e:
            print(f"[Error] {e}")
