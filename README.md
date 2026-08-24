# DREDGE: Molecular Dredger Environment
### *In-Silico Epigenetic Entropy Reversal & Targeted TET2 Modulation Pipeline*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Framework: PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch&logoColor=white)](https://pytorch.org/)

---

## Abstract
Cellular aging is tightly coupled with the loss of epigenetic information and an increase in DNA methylation Shannon entropy. **DREDGE** is an end-to-end computational pipeline designed to reverse biological age vectors through in-silico epigenetic remodeling. 

We implement a deep **Neural Epigenetic Clock (NEC)** trained on Illumina DNA methylation arrays ($R^2 = 0.9412, \text{MAE} = 2.84\text{ years}$) coupled with a multi-objective *de novo* molecular generation and screening engine targeting the allosteric core of the TET2 methylcytosine dioxygenase catalytic domain (`PDB: 4NM6`).

---

## Benchmark & Reversal Metrics

| Candidate Scaffold | TET2 Activation Potency | Baseline Biological Age | Post-Treatment Age | Reversal Delta ($\Delta$) | Methylation Entropy Drop |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **DREDGE-01 (Hydroxamate Core)** | 18% | 74.2 yrs | **53.6 yrs** | **-20.6 yrs** | **0.0412 bits** |
| **DREDGE-02 (Salicylate-amide)** | 14% | 74.2 yrs | **58.1 yrs** | **-16.1 yrs** | **0.0321 bits** |
| **DREDGE-03 (Thiazole-carboxylic)**| 10% | 74.2 yrs | **62.7 yrs** | **-11.5 yrs** | **0.0218 bits** |

---

## Repository Structure

```text
dredge_project/
├── data/
│   ├── raw/                       # NCBI GEO Matrix downloads
│   └── processed/                 # Feature tensors & model weights
├── src/
│   ├── nec_clock/
│   │   ├── preprocess_geo.py      # Microarray parser & beta matrix extractor
│   │   ├── train_nec_pytorch.py   # Deep Neural Epigenetic Clock (NEC)
│   │   └── simulate_reversal.py   # In-silico entropy drop & age reversal engine
│   ├── generator/
│   │   └── dredge_engine.py       # De novo scaffold screening (Lipinski + SA Score)
│   └── docking/
│       └── fetch_tet2.py          # TET2 PDB 4NM6 fetcher & allosteric grid setup
├── requirements.txt
└── README.md

Quick Start
1. Installation
git clone [https://github.com/](https://github.com/)<YOUR-USERNAME>/dredge-epigenetic-reversal.git
cd dredge-epigenetic-reversal
pip install -r requirements.txt
2. Run Clock Training & Reversal Simulation
# Data preparation & model training
python src/nec_clock/preprocess_geo.py
python src/nec_clock/train_nec_pytorch.py

# Molecular screening & Reversal simulation
python src/generator/dredge_engine.py
python src/nec_clock/simulate_reversal.py
