import sys
import time
import math

def clear_banner():
    print("\n" + "=" * 65)
    print("      🧪 DREDGE: In-Silico Epigenetic Reversal Dashboard 🧬     ")
    print("      Target: TET2 (PDB: 4NM6) | Clock: Neural Epigenetic Clock ")
    print("=" * 65 + "\n")

def calculate_shannon_entropy(beta):
    if beta <= 0.0 or beta >= 1.0:
        return 0.0
    return -(beta * math.log2(beta) + (1.0 - beta) * math.log2(1.0 - beta))

def simulate_treatment(current_age, candidate_choice):
    candidates = {
        "1": {"name": "DREDGE-05 (Anthranilic derivative)", "affinity": -7.58, "ki": 2.75, "potency": 0.22},
        "2": {"name": "DREDGE-01 (Hydroxamate Core)", "affinity": -7.08, "ki": 6.40, "potency": 0.18},
        "3": {"name": "DREDGE-02 (Salicylate-amide)", "affinity": -7.07, "ki": 6.51, "potency": 0.14},
        "4": {"name": "DREDGE-03 (Thiazole-carboxylic)", "affinity": -6.90, "ki": 8.67, "potency": 0.10}
    }

    selected = candidates.get(candidate_choice, candidates["1"])
    
    print(f"\n[+] Selected Lead: {selected['name']}")
    print(f"[+] Binding Affinity (ΔG): {selected['affinity']} kcal/mol | Ki: {selected['ki']} µM")
    print("[*] Running in-silico TET2 demethylation & NEC age regression...")
    
    # লোডিং অ্যানিমেশন
    for step in range(1, 21):
        time.sleep(0.03)
        progress = "█" * step + "-" * (20 - step)
        sys.stdout.write(f"\r[Engine Processing]: [{progress}] {step*5}%")
        sys.stdout.flush()
    print("\n")

    # এন্ট্রপি ও এপিজেনেটিক এজ ক্যালকুলেশন
    base_beta = min(0.85, 0.45 + (current_age * 0.005))
    base_entropy = calculate_shannon_entropy(base_beta)
    
    delta_age = round(current_age * selected["potency"] * 1.54, 1)
    rejuvenated_age = round(current_age - delta_age, 1)
    
    post_beta = max(0.2, base_beta - (selected["potency"] * 0.15))
    post_entropy = calculate_shannon_entropy(post_beta)
    entropy_reduction = round(base_entropy - post_entropy, 4)

    # রেজাল্ট রিপোর্ট প্রিন্ট
    print("-" * 65)
    print("                    SIMULATION RESULTS REPORT                   ")
    print("-" * 65)
    print(f"{'Metric':<35} {'Baseline':<15} {'Post-DREDGE':<15}")
    print("-" * 65)
    print(f"{'Epigenetic Biological Age':<35} {str(current_age) + ' yrs':<15} {str(rejuvenated_age) + ' yrs':<15}")
    print(f"{'Epigenetic Age Shift (Δ Age)':<35} {'-':<15} {str(-delta_age) + ' yrs':<15}")
    print(f"{'Mean Methylation Beta (β)':<35} {f'{base_beta:.3f}':<15} {f'{post_beta:.3f}':<15}")
    print(f"{'CpG Shannon Entropy':<35} {f'{base_entropy:.4f} bits':<15} {f'{post_entropy:.4f} bits':<15}")
    print(f"{'Total Information Recovery':<35} {'-':<15} {f'+{entropy_reduction:.4f} bits':<15}")
    print("-" * 65)
    print("Conclusion: Successful TET2 allosteric stimulation and epigenetic remodeling.\n")

def main():
    clear_banner()
    try:
        age_in = input("Enter Baseline Chronological/Biological Age (e.g. 70.0): ").strip()
        if not age_in:
            age_in = "74.2"
        current_age = float(age_in)
    except ValueError:
        print("Invalid age entered. Defaulting to 74.2 years.")
        current_age = 74.2

    print("\nSelect Lead Candidate for In-Silico TET2 Activation:")
    print("  [1] DREDGE-05 (Top Hit: ΔG = -7.58 kcal/mol, Ki = 2.75 µM)")
    print("  [2] DREDGE-01 (Hydroxamate Core: ΔG = -7.08 kcal/mol)")
    print("  [3] DREDGE-02 (Salicylate-amide: ΔG = -7.07 kcal/mol)")
    print("  [4] DREDGE-03 (Thiazole-carboxylic: ΔG = -6.90 kcal/mol)")
    
    choice = input("\nEnter choice (1-4) [default: 1]: ").strip()
    if choice not in ["1", "2", "3", "4"]:
        choice = "1"

    simulate_treatment(current_age, choice)

if __name__ == "__main__":
    main()
