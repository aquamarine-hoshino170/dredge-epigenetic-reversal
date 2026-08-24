import os
import math

def test_shannon_entropy():
    beta = 0.5
    h = -(beta * math.log2(beta) + (1.0 - beta) * math.log2(1.0 - beta))
    assert round(h, 2) == 1.0

def test_files_exist():
    assert os.path.exists("data/processed/candidates/dredge_screened_leads.csv")
    assert os.path.exists("data/processed/docking/tet2_vina_affinities.csv")
    assert os.path.exists("data/processed/targets/4NM6.pdb")
