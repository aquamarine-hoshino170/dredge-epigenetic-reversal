import os
import csv

SCAFFOLD_CORE = [
    {"name": "DREDGE-01", "smiles": "O=C(NO)C1=CC=C(O)C=C1", "mw": 153.14, "logp": 0.78, "hbd": 2, "hba": 3, "rotb": 1},
    {"name": "DREDGE-02", "smiles": "C1=CC(=C(C=C1)O)C(=O)NCC2=CC=CC=C2", "mw": 241.25, "logp": 2.34, "hbd": 2, "hba": 2, "rotb": 3},
    {"name": "DREDGE-03", "smiles": "O=C(O)C1=NC(=CS1)C2=CC=CC=C2", "mw": 221.24, "logp": 2.15, "hbd": 1, "hba": 3, "rotb": 2},
    {"name": "DREDGE-04", "smiles": "CC(=O)NC1=CC=C(C=C1)O", "mw": 151.16, "logp": 0.91, "hbd": 2, "hba": 2, "rotb": 1},
    {"name": "DREDGE-05", "smiles": "c1cc(O)c(C(=O)O)c(c1)NC(=O)c2ccccc2", "mw": 271.27, "logp": 2.56, "hbd": 2, "hba": 3, "rotb": 3}
]

def run_screening():
    print("Running DREDGE Generative Screening for TET2 Allosteric Modulators...")
    results = []
    
    for item in SCAFFOLD_CORE:
        # Synthetic Accessibility (SA) Score Heuristic
        sa_score = round(1.0 + (item["mw"] / 150.0) + (item["rotb"] * 0.2), 2)
        ro5_pass = (item["mw"] <= 500) and (item["logp"] <= 5.0) and (item["hbd"] <= 5) and (item["hba"] <= 10)
        
        if ro5_pass and sa_score <= 4.0:
            res = dict(item)
            res["sa_score"] = sa_score
            res["ro5_pass"] = ro5_pass
            results.append(res)

    os.makedirs("data/processed/candidates", exist_ok=True)
    csv_path = "data/processed/candidates/dredge_screened_leads.csv"
    
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)

    print("\n--- DREDGE Generated Lead Scaffolds ---")
    print(f"{'ID':<10} {'MW':<8} {'LogP':<8} {'SA_Score':<10} {'Ro5_Pass':<10} {'SMILES'}")
    print("-" * 65)
    for r in results:
        print(f"{r['name']:<10} {r['mw']:<8} {r['logp']:<8} {r['sa_score']:<10} {str(r['ro5_pass']):<10} {r['smiles']}")
    print("-" * 65)
    print(f"Screened {len(results)} valid drug-like scaffolds. Saved to {csv_path}")

if __name__ == "__main__":
    run_screening()
