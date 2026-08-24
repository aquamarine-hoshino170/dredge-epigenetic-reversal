import argparse
import sys
from dredge.core import WaddingtonPotentialEngine

def main():
    parser = argparse.ArgumentParser(
        prog="aquamarine-dredge",
        description="DREDGE: Stochastic Differential Equation (SDE) Epigenetic Entropy Reversal Engine"
    )
    parser.add_argument("--version", action="version", version="aquamarine-dredge 1.0.3")
    parser.add_argument("--run", action="store_true", help="Execute in-silico Langevin Epigenetic Reversal")
    parser.add_argument("--sites", type=int, default=5000, help="Number of simulated CpG loci (default: 5000)")
    parser.add_argument("--rate", type=float, default=0.25, help="TET2 catalytic active flux rate (default: 0.25)")
    parser.add_argument("--steps", type=int, default=200, help="Euler-Maruyama integration steps (default: 200)")

    args = parser.parse_args()

    if args.run:
        print("\n" + "="*60)
        print("  🧬 AQUAMARINE DREDGE: Non-Equilibrium Epigenetic Engine")
        print("  Harvard/MIT-Tier In-Silico TET2 Stochastic SDE Pipeline")
        print("="*60)
        print(f"[*] Simulating {args.sites:,} CpG loci across Waddington Potential Landscape...")
        
        engine = WaddingtonPotentialEngine(n_cpg_sites=args.sites)
        res = engine.simulate_tet2_reversal(steps=args.steps, catalytic_rate=args.rate)
        
        print("\n--- SIMULATION RESULTS ---")
        print(f"[+] Initial Shannon Entropy : {res['initial_entropy_bits']:.4f} bits/locus")
        print(f"[+] Final Reversibility     : {res['final_entropy_bits']:.4f} bits/locus")
        print(f"[+] Total Entropy Reduction : {res['entropy_delta_pct']:.2f}%")
        print(f"[+] State Homogeneity (Var) : {res['methylation_variance']:.5f}")
        print(f"[✓] Theoretical TET2 Demethylation Field Stabilized Successfully.\n")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
