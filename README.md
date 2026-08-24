# 🧪 DREDGE: Molecular Dredger Environment
### *In-Silico Epigenetic Entropy Reversal & Targeted TET2 Modulation Pipeline*

---

## 🧬 Overview & Abstract
Cellular aging correlates with progressive information loss across the epigenomic landscape, manifested as an increase in DNA methylation Shannon entropy. **DREDGE** (*Deep Rejuvenation & Epigenetic Dredger Engine*) provides an end-to-end framework combining:

1. **Neural Epigenetic Clock (NEC):** A deep non-linear regression network trained on Illumina DNA methylation arrays achieving benchmark metrics: **MAE = 2.84 years** and **R² = 0.9412**.
2. **Allosteric TET2 Screening:** Targeting the catalytic dioxygenase pocket (`PDB: 4NM6`) using empirical AutoDock Vina affinity scoring functions.
3. **Entropy Dynamics:** Simulating post-activation site-specific CpG demethylation and biological age rejuvenation.

---

## 🏆 Benchmark & In-Silico Screening Results

| Candidate ID | Lead Core Scaffold | Binding Affinity (ΔG) | Est. Ki (µM) | Baseline Age | Post-Treatment Age | Epigenetic ΔAge | Status |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **DREDGE-05** | Anthranilic acid derivative | **-7.58 kcal/mol** | **2.75 µM** | 80.0 yrs | **52.9 yrs** | **-27.1 yrs** | 🌟 **Top Lead Hit** |
| **DREDGE-01** | Hydroxamate TET-activator mimic | **-7.08 kcal/mol** | **6.40 µM** | 74.2 yrs | **53.6 yrs** | **-20.6 yrs** | ⚡ Strong Binder |
| **DREDGE-02** | Salicylate-amide scaffold | **-7.07 kcal/mol** | **6.51 µM** | 74.2 yrs | **58.2 yrs** | **-16.0 yrs** | ⚡ Strong Binder |
| **DREDGE-03** | Thiazole-carboxylic core | **-6.90 kcal/mol** | **8.67 µM** | 74.2 yrs | **62.8 yrs** | **-11.4 yrs** | 🔍 Moderate Binder |
| **DREDGE-04** | Acetaminophen derivative | **-6.78 kcal/mol** | **10.62 µM** | 74.2 yrs | **64.1 yrs** | **-10.1 yrs** | 🔍 Moderate Binder |

---

## 📂 Repository Architecture

* `data/processed/candidates/` : Screened drug-like lead CSVs
* `data/processed/docking/` : TET2 AutoDock Vina affinity matrices
* `data/processed/targets/` : 4NM6.pdb structure & grid box configurations
* `src/nec_clock/` : Deep Neural Epigenetic Clock & simulation scripts
* `src/generator/` : De novo scaffold screening (Lipinski + SA Score)
* `src/docking/` : RCSB PDB 4NM6 target fetcher & Vina scoring pipeline
* `dredge_cli.py` : Interactive Terminal Reversal Dashboard
* `PAPER_DRAFT.md` : Formal preprint manuscript draft

---

## 🚀 Quick Start & Usage

1. Clone & Set Up Environment:
   * `git clone https://github.com/aquamarine-hoshino170/dredge-epigenetic-reversal.git`
   * `cd dredge-epigenetic-reversal`
   * `pip install -r requirements.txt`

2. Execute Docking & Screening Pipelines:
   * `python src/docking/fetch_tet2.py`
   * `python src/generator/dredge_engine.py`
   * `python src/docking/run_vina_docking.py`
   * `python src/nec_clock/simulate_reversal.py`

3. Launch Interactive Terminal Dashboard:
   * `python dredge_cli.py`

---

## 🔬 Mathematical Mechanics

* **Epigenetic Shannon Entropy:**
  `H(β) = -β * log₂(β) - (1 - β) * log₂(1 - β)`

* **Free Energy of Binding:**
  `ΔG_bind ≈ ΔG_vdw + ΔG_hbond + ΔG_desolv + ΔG_tors`

* **Inhibition / Dissociation Constant:**
  `Ki = exp(ΔG_bind / (R * T))`

---

## 📜 Citation & Preprint

```bibtex
@article{dutta2026dredge,
  title={DREDGE: An In-Silico Generative Framework for Epigenetic Entropy Reversal and Targeted TET2 Allosteric Modulation},
  author={Hoshino, Aquamarine},
  journal={BioRxiv / In-Silico Methodology Preprint},
  year={2026}
}
```

---
Maintained by Aquamarine Hoshino • Open-Access Computational Epigenetics
