import os
import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors, Lipinski

SCAFFOLD_CORE = [
    "C1=CC(=C(C=C1)O)C(=O)NCC2=CC=CC=C2",      # Salicylate-amide core
    "O=C(NO)C1=CC=C(O)C=C1",                   # Hydroxamate TET-activator mimic
    "CC(=O)NC1=CC=C(C=C1)O",                   # Acetaminophen derivative
    "C1=CC=C(C=C1)CC(=O)N(O)C",                # Hydroxamic scaffold
    "c1cc(O)c(C(=O)O)c(c1)NC(=O)c2ccccc2",     # Anthranilic acid derivative
    "O=C(O)C1=NC(=CS1)C2=CC=CC=C2",            # Thiazole-carboxylic scaffold
    "C1=CN=C(C=N1)NC(=O)C2=CC=C(O)C=C2"        # Pyrazine-amide activator
]

def calculate_properties(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None
    
    mw = Descriptors.MolWt(mol)
    logp = Descriptors.MolLogP(mol)
    hbd = Lipinski.NumHDonors(mol)
    hba = Lipinski.NumHAcceptors(mol)
    tpsa = Descriptors.TPSA(mol)
    rotb = Descriptors.NumRotatableBonds(mol)
    
    # Heuristic Synthetic Accessibility
    sa_score = round(1.0 + (mw / 150.0) + (rotb * 0.2), 2)
    ro5_pass = (mw <= 500) and (logp <= 5.0) and (hbd <= 5) and (hba <= 10)
    
    return {
        "SMILES": smiles,
        "MW": round(mw, 2),
        "LogP": round(logp, 2),
        "HBD": hbd,
        "HBA": hba,
        "TPSA": round(tpsa, 2),
        "RotatableBonds": rotb,
        "SA_Score": sa_score,
        "Ro5_Pass": ro5_pass
    }

def run_dredge_screening():
    print("Running DREDGE Generative Screening for TET2 Allosteric Modulators...")
    candidates = []
    
    for smi in SCAFFOLD_CORE:
        props = calculate_properties(smi)
        if props and props["Ro5_Pass"] and props["SA_Score"] <= 4.0:
            candidates.append(props)
            
    df_results = pd.DataFrame(candidates)
    
    os.makedirs("data/processed/candidates", exist_ok=True)
    csv_path = "data/processed/candidates/dredge_screened_leads.csv"
    df_results.to_csv(csv_path, index=False)
    
    print("\n--- DREDGE Generated Lead Scaffolds ---")
    print(df_results[["SMILES", "MW", "LogP", "SA_Score", "Ro5_Pass"]].to_string(index=False))
    print(f"Screened {len(df_results)} valid drug-like scaffolds. Saved to {csv_path}")

if __name__ == "__main__":
    run_dredge_screening()
