import argparse
import json
import sys
from dredge.core import DREDGEResearchPipeline, GenomicBedProcessor

def main():
    parser = argparse.ArgumentParser(
        prog="aquamarine-dredge",
        description="DREDGE Enterprise: Computational Epigenetics Pipeline for Academic & Clinical Research"
    )
    parser.add_argument("--version", action="version", version="aquamarine-dredge 1.2.2")
    parser.add_argument("--run", action="store_true", help="Execute research simulation pipeline")
    parser.add_argument("--input", type=str, default=None, help="Input genomic BED file path")
    parser.add_argument("--generate-bed", action="store_true", help="Generate synthetic human CpG island BED dataset")
    parser.add_argument("--sites", type=int, default=10000, help="CpG loci count (default: 10000)")
    parser.add_argument("--rate", type=float, default=0.45, help="TET2 catalytic flux (default: 0.45)")
    parser.add_argument("--steps", type=int, default=250, help="Integration steps (default: 250)")
    parser.add_argument("--export", type=str, default="report.json", help="Path to export report (default: report.json)")

    args = parser.parse_args()

    if args.generate_bed:
        bed_path = GenomicBedProcessor.generate_synthetic_cpg_bed(n_sites=args.sites)
        print(f"[✓] Generated synthetic human genomic methylation profile: {bed_path}")
        return

    if args.run:
        print("\n" + "="*70)
        print("  🔬 AQUAMARINE DREDGE ENTERPRISE BIO-COMPUTING PIPELINE")
        print("  In-Silico Waddington Potential Landscape & Horvath Reversal")
        print("="*70)
        
        pipeline = DREDGEResearchPipeline(n_sites=args.sites)
        report, _ = pipeline.run_rejuvenation_pipeline(steps=args.steps, tet2_flux=args.rate, input_bed=args.input)
        
        print(f"[*] Analyzed {report['metadata']['cpg_loci_analyzed']:,} high-density CpG genomic loci.")
        print("\n--- CLINICAL / RESEARCH BIOMARKER SUMMARY ---")
        print(f" • Pre-Treatment Biological Age  : {report['biomarkers']['pre_treatment_biological_age']} years")
        print(f" • Post-Treatment Biological Age : {report['biomarkers']['post_treatment_biological_age']} years")
        print(f" • Net Rejuvenation Reclaimed    : -{report['biomarkers']['years_rejuvenated']} years")
        print(f" • Shannon Information Entropy   : {report['biomarkers']['shannon_entropy_initial']} -> {report['biomarkers']['shannon_entropy_final']} bits")
        
        with open(args.export, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)
        print(f"\n[✓] Publication-ready report exported successfully to: {args.export}\n")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
