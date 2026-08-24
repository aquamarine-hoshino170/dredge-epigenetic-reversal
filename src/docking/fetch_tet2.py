import os
import requests

def prepare_tet2_target(pdb_id="4NM6", output_dir="data/processed/targets"):
    os.makedirs(output_dir, exist_ok=True)
    url = f"https://files.rcsb.org/download/{pdb_id}.pdb"
    dest_path = os.path.join(output_dir, f"{pdb_id}.pdb")
    
    print(f"Fetching TET2 structure {pdb_id} from RCSB PDB...")
    res = requests.get(url)
    if res.status_code == 200:
        with open(dest_path, "w", encoding="utf-8") as f:
            f.write(res.text)
        print(f"Successfully saved {pdb_id}.pdb to {dest_path}")
    else:
        print(f"Failed to fetch PDB: HTTP {res.status_code}")
        return

    # Allosteric Binding Grid Specification (TET2 Catalytic Core)
    grid_config = {
        "center_x": 12.45,
        "center_y": -22.18,
        "center_z": 30.04,
        "size_x": 22.0,
        "size_y": 22.0,
        "size_z": 22.0
    }
    
    config_path = os.path.join(output_dir, f"{pdb_id}_grid_box.txt")
    with open(config_path, "w") as f:
        for k, v in grid_config.items():
            f.write(f"{k} = {v}\n")
    print(f"Generated docking grid config: {config_path}")

if __name__ == "__main__":
    prepare_tet2_target()
