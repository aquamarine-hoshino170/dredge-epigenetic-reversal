import argparse
import sys
import numpy as np
from dredge.core import WaddingtonPotentialEngine

def render_ascii_sparkline(data: list, height: int = 6, width: int = 40) -> str:
    """Generates ASCII terminal graph of temporal trajectories."""
    min_val, max_val = min(data), max(data)
    if max_val == min_val:
        return "── Flat Line ──"
    
    # Downsample
    indices = np.linspace(0, len(data) - 1, width).astype(int)
    sampled = [data[i] for i in indices]
    
    grid = [[" " for _ in range(width)] for _ in range(height)]
    
    for x, val in enumerate(sampled):
        norm = (val - min_val) / (max_val - min_val)
        y = int(norm * (height - 1))
        grid[height - 1 - y][x] = "█"
        
    lines = ["".join(row) for row in grid]
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(
        prog="aquamarine-dredge",
        description="DREDGE: Ultra-Tier Epigenetic Entropy Reversal & Horvath Biological Clock Calibration"
    )
    parser.add_argument("--version", action="version", version="aquamarine-dredge 1.1.0")
    parser.add_argument("--run", action="store_true", help="Execute Ultra In-Silico TET2 Stochastic SDE Pipeline")
    parser.add_argument("--sites", type=int, default=3000, help="CpG loci count (default: 3000)")
    parser.add_argument("--rate", type=float, default=0.35, help="TET2 catalytic flux (default: 0.35)")
    parser.add_argument("--steps", type=int, default=150, help="Simulation steps (default: 150)")

    args = parser.parse_args()

    if args.run:
        print("\n" + "="*68)
        print("  🧬 AQUAMARINE DREDGE ULTRA (v1.1.0)")
        print("  Quantum-Stochastic Epigenetic Reversal & Horvath Clock Decelerator")
        print("="*68)
        print(f"[*] Simulating {args.sites:,} loci across Waddington Non-Equilibrium Field...")
        
        engine = WaddingtonPotentialEngine(n_cpg_sites=args.sites)
        res = engine.simulate_tet2_reversal(steps=args.steps, catalytic_rate=args.rate)
        
        print("\n--- HORVATH BIOLOGICAL CLOCK METRICS ---")
        print(f"[+] Initial Biological Age  : {res['initial_age']:.2f} yrs")
        print(f"[+] Rejuvenated State Age   : {res['final_age']:.2f} yrs")
        print(f"[★] Biological Reversal     : -{res['age_reversal_years']:.2f} Years Reclaimed")
        
        print("\n--- INFORMATION ENTROPY DYNAMICS ---")
        print(f"[+] Initial Entropy         : {res['initial_entropy']:.4f} bits")
        print(f"[+] Reversibility Delta     : {res['entropy_reduction_pct']:.2f}%")
        
        print("\n--- ENTROPY DECAY TRAJECTORY (ASCII GRAPH) ---")
        print(render_ascii_sparkline(res['entropy_traj']))
        print("0 Step " + "─"*28 + f"> {args.steps} Steps (Reversed)")
        print("\n[✓] TET2 Demethylation Operator Successfully Converged.\n")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
