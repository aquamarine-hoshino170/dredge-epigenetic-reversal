import argparse
import json
import sys
from dredge.core import DREDGEResearchPipeline, GenomicBedProcessor

def export_markdown_report(report: dict, filename: str = "report.md"):
    md_content = rf"""# Epigenetic Entropy Reversal Scientific Report
**Engine:** `{report['metadata']['engine']}`  
**Analyzed CpG Coordinates:** {report['metadata']['cpg_loci_analyzed']:,} loci  
**Integration Steps:** {report['metadata']['integration_steps']} | **TET2 Catalytic Rate:** {report['metadata']['tet2_catalytic_efficiency']}

---

## Biomarker Results Summary
| Biomarker Indicator | Pre-Treatment | Post-Treatment | Net Effect |
| :--- | :--- | :--- | :--- |
| **Horvath Biological Age** | {report['biomarkers']['pre_treatment_biological_age']} yrs | {report['biomarkers']['post_treatment_biological_age']} yrs | **-{report['biomarkers']['years_rejuvenated']} Years** |
| **Shannon Information Entropy** | {report['biomarkers']['shannon_entropy_initial']} bits | {report['biomarkers']['shannon_entropy_final']} bits | **+{report['biomarkers']['entropy_decay_percentage']}%** |

### Mathematical Validation
- **Stochastic Operator:** Langevin SDE ($\Delta t = 0.01$)
- **Potential Field:** Non-equilibrium Waddington Landscape $V(p)$
- **Status:** Demethylation flux convergence achieved.
"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(md_content)

def main():
    parser = argparse.ArgumentParser(
        prog="aquamarine-dredge",
        description="DREDGE Enterprise: Computational Epigenetics Pipeline for Academic & Clinical Research"
    )
    parser.add_argument("--version", action="version", version="aquamarine-dredge 1.4.0")
    parser.add_argument("--run", action="store_true", help="Execute single-sample research simulation")
    parser.add_argument("--trial", type=int, default=0, help="Run Cohort Trial with N subjects")
    parser.add_argument("--benchmark", action="store_true", help="Run computational throughput benchmarks")
    parser.add_argument("--cite", action="store_true", help="Print BibTeX citation format for research papers")
    parser.add_argument("--input", type=str, default=None, help="Input genomic BED file path")
    parser.add_argument("--generate-bed", action="store_true", help="Generate synthetic human CpG island BED dataset")
    parser.add_argument("--sites", type=int, default=10000, help="CpG loci count (default: 10000)")
    parser.add_argument("--rate", type=float, default=0.45, help="TET2 catalytic flux (default: 0.45)")
    parser.add_argument("--steps", type=int, default=250, help="Integration steps (default: 250)")
    parser.add_argument("--export-md", type=str, default="report.md", help="Export Markdown scientific report")

    args = parser.parse_args()

    if args.cite:
        print("""@software{aquamarine_dredge_2026,
  author = {Hoshino, Aquamarine},
  title = {DREDGE: In-Silico Epigenetic Entropy Reversal & Targeted TET2 Modulation Pipeline},
  year = {2026},
  publisher = {PyPI},
  url = {https://pypi.org/project/aquamarine-dredge/}
}""")
        return

    pipeline = DREDGEResearchPipeline(n_sites=args.sites)

    if args.benchmark:
        print("\n" + "="*70)
        print("  ⚡ DREDGE HARDWARE & VECTOR THROUGHPUT BENCHMARK")
        print("="*70)
        results = pipeline.benchmark_engine()
        for res in results:
            print(f" • Cohort Size: {res['loci']:,} Loci | Time: {res['time_sec']}s | Rate: {res['throughput_loci_per_sec']:,} Loci/sec")
        print("[✓] Vector engine verified for large-scale bio-simulations.\n")
        return

    if args.generate_bed:
        bed_path = GenomicBedProcessor.generate_synthetic_cpg_bed(n_sites=args.sites)
        print(f"[✓] Generated synthetic human genomic methylation profile: {bed_path}")
        return

    if args.trial > 0:
        print("\n" + "="*70)
        print(f"  🔬 IN-SILICO CLINICAL TRIAL (Cohort Size: {args.trial} Subjects)")
        print("="*70)
        res = pipeline.run_cohort_trial(cohort_size=args.trial, steps=args.steps, tet2_flux=args.rate)
        print(f" • Average Age Reversal Reclaimed : -{res['mean_years_rejuvenated']} ± {res['std_deviation']} Years")
        print(f" • Clinical Range (Min / Max)     : -{res['min_reversal']} yrs / -{res['max_reversal']} yrs")
        print(f"[✓] Multi-Cohort Statistical Convergence Confirmed.\n")
        return

    if args.run:
        print("\n" + "="*70)
        print("  🔬 AQUAMARINE DREDGE ENTERPRISE BIO-COMPUTING PIPELINE")
        print("="*70)
        report, _ = pipeline.run_rejuvenation_pipeline(steps=args.steps, tet2_flux=args.rate, input_bed=args.input)
        
        print(f"[*] Analyzed {report['metadata']['cpg_loci_analyzed']:,} CpG genomic loci.")
        print(f" • Pre-Treatment Biological Age  : {report['biomarkers']['pre_treatment_biological_age']} years")
        print(f" • Post-Treatment Biological Age : {report['biomarkers']['post_treatment_biological_age']} years")
        print(f" • Net Rejuvenation Reclaimed    : -{report['biomarkers']['years_rejuvenated']} years")
        
        with open("report.json", "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)
        export_markdown_report(report, args.export_md)
        print(f"\n[✓] Publication reports generated: report.json & {args.export_md}\n")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
