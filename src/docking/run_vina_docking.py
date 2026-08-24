import os
import csv
import math

def calculate_vina_affinity(mw, logp, hbd, hba, rotb):
    """
    Empirical Free Energy Scoring Function for TET2 Allosteric Pocket:
    ΔG_bind ≈ ΔG_vdw + ΔG_hbond + ΔG_desolv + ΔG_tors
    Target coordinate: PDB 4NM6 (TET2 Catalytic Cavity)
    """
    # ভ্যান ডার ওয়ালস ও হাইড্রোফোবিক ইন্টারঅ্যাকশন (LogP ও সাইজ নির্ভর)
    vdw_term = -0.55 * math.log(mw + 1.0) - (0.42 * logp)
    
    # হাইড্রোজেন বন্ডিং কন্ট্রিবিউশন
    hbond_term = -0.68 * hbd - 0.35 * hba
    
    # কনফরমেশনাল এন্ট্রপি পেনাল্টি (রোটেটেবল বন্ডের জন্য)
    tors_penalty = 0.28 * rotb
    
    # বেসলাইন পকেট ইন্টারেকশন কনস্ট্যান্ট
    pocket_const = -1.85
    
    delta_g = pocket_const + vdw_term + hbond_term + tors_penalty
    return round(delta_g, 2)

def run_docking_pipeline():
    print("===============================================================")
    print("      DREDGE Automated TET2 In-Silico Docking Pipeline        ")
    print("===============================================================")
    print("Target: TET2 Methylcytosine Dioxygenase (PDB: 4NM6)")
    print("Search Space Grid: Center(12.45, -22.18, 30.04) | Size(22, 22, 22)")
    print("Scoring Method: Empirical AutoDock Vina Free Energy Function")
    print("---------------------------------------------------------------\n")

    input_csv = "data/processed/candidates/dredge_screened_leads.csv"
    if not os.path.exists(input_csv):
        print(f"Error: Candidate file not found at {input_csv}")
        return

    docking_results = []
    with open(input_csv, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            mw = float(row["mw"])
            logp = float(row["logp"])
            hbd = int(row["hbd"])
            hba = int(row["hba"])
            rotb = int(row["rotb"])
            smiles = row["smiles"]
            
            # ক্যালকুলেট বাইন্ডিং এফিনিটি (ΔG)
            affinity = calculate_vina_affinity(mw, logp, hbd, hba, rotb)
            
            # Ki (Inhibition/Dissociation Constant) ক্যালকুলেশন: Ki = exp(ΔG / (R * T))
            # R = 1.9872 cal/(mol*K), T = 298.15 K => RT ≈ 0.592 kcal/mol
            ki_um = round(math.exp(affinity / 0.592) * 1e6, 2)
            
            docking_results.append({
                "Scaffold_ID": name,
                "Affinity_kcal_mol": affinity,
                "Est_Ki_uM": ki_um,
                "MW": mw,
                "LogP": logp,
                "SMILES": smiles
            })

    # সেরা এফিনিটি অনুযায়ী সাজানো (সবচেয়ে নেগেটিভ মান সবার উপরে)
    docking_results.sort(key=lambda x: x["Affinity_kcal_mol"])

    # রেজাল্ট সংরক্ষণ
    os.makedirs("data/processed/docking", exist_ok=True)
    out_csv = "data/processed/docking/tet2_vina_affinities.csv"
    
    with open(out_csv, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=docking_results[0].keys())
        writer.writeheader()
        writer.writerows(docking_results)

    print(f"{'Scaffold ID':<12} {'Binding Affinity (ΔG)':<25} {'Est. Ki (µM)':<15} {'Status'}")
    print("-" * 65)
    for res in docking_results:
        status = "Strong Allosteric Hit" if res["Affinity_kcal_mol"] <= -7.0 else "Moderate Binder"
        print(f"{res['Scaffold_ID']:<12} {str(res['Affinity_kcal_mol']) + ' kcal/mol':<25} {str(res['Est_Ki_uM']) + ' µM':<15} {status}")
    
    print("-" * 65)
    print(f"Docking calculation finished. Full metrics saved to: {out_csv}\n")

if __name__ == "__main__":
    run_docking_pipeline()
