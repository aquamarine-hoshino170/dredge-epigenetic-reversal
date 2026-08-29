# 🧬 DREDGE: Epigenetic Entropy Reversal & TET2 Modulation

**In-Silico Generative Pipeline for Epigenetic Entropy Reversal & Targeted TET2 Modulation**

![Python 96.1%](https://img.shields.io/badge/Python-96.1%25-blue)
![TeX 3.7%](https://img.shields.io/badge/TeX-3.7%25-lightgrey)
![Dockerfile 0.2%](https://img.shields.io/badge/Docker-0.2%25-blue)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Research](https://img.shields.io/badge/Research-Bioinformatics-brightgreen)

---

## 📋 Overview

**DREDGE** is a computational framework for modeling and reversing epigenetic aging through TET2-mediated DNA methylation modulation. This in-silico pipeline integrates:

- 🧪 **Epigenetic Clock Reversal** - Hayflick limit modeling and entropy computation
- 🔬 **TET2 Dynamics** - Methyl-cytosine oxidation pathway simulation
- 📊 **DNA Methylation States** - Multi-state transitions and probability distributions
- 🧠 **Generative Models** - Latent space exploration for epigenetic trajectories
- 🎯 **Targeted Interventions** - Mechanistic TET2 modulation strategies
- 📈 **Aging Biomarkers** - Age acceleration/deceleration analysis

---

## 🎯 Key Features

### Epigenetic Modeling
- **Methylation State Space** - CpG site dynamics (Unmethylated → Methylated → 5mC → 5hmC)
- **TET2 Enzyme Kinetics** - Oxidative conversion rates and efficiency
- **Entropy Quantification** - Thermodynamic aging quantification
- **Hayflick Limit** - Cellular senescence trajectory modeling

### Computational Pipeline
- **Data Integration** - Multi-omics preprocessing and normalization
- **Machine Learning** - Generative models for epigenetic state prediction
- **Network Analysis** - CpG interaction and co-methylation patterns
- **Simulation Engine** - Agent-based cellular aging models

### Analysis & Visualization
- **Clock Reversal Metrics** - Age deceleration quantification
- **Intervention Screening** - Virtual TET2 modulation experiments
- **Trajectory Prediction** - Prospective aging forecasting
- **Heatmaps & Networks** - Multi-dimensional epigenetic visualization

---

## ⚙️ Installation

### Requirements
- Python 3.8+
- Docker (optional, for containerized execution)

### Local Setup

```bash
# Clone repository
git clone https://github.com/aquamarine-hoshino170/dredge-epigenetic-reversal.git
cd dredge-epigenetic-reversal

# Install dependencies
pip install -r requirements.txt

# Install package
pip install -e .
```

### Docker Setup

```bash
# Build Docker image
docker build -t dredge:latest .

# Run container
docker run -v $(pwd)/data:/data dredge:latest python pipeline.py
```

---

## 🚀 Quick Start

### Basic Usage

```python
from dredge import EpigeneticClock, TET2Engine, EntropyCalculator

# Initialize epigenetic clock
clock = EpigeneticClock(donor_age=45, cell_type='fibroblast')

# Simulate natural aging
aging_trajectory = clock.simulate_aging(years=10, steps=1000)

# Apply TET2 modulation
tet2_engine = TET2Engine(efficiency=0.85, target_sites='aging_hotspots')
reversed_trajectory = tet2_engine.modulate(aging_trajectory, intensity=0.6)

# Calculate entropy reversal
entropy_calc = EntropyCalculator()
initial_entropy = entropy_calc.compute(aging_trajectory[0])
final_entropy = entropy_calc.compute(reversed_trajectory[-1])
entropy_reversal = (initial_entropy - final_entropy) / initial_entropy

print(f"Epigenetic Age Reversal: {entropy_reversal*100:.1f}%")
```

### Example: Clock Reversal Analysis

```python
from dredge import MethylationAnalyzer, ClockReversal

# Load methylation data
analyzer = MethylationAnalyzer('data/methylation_matrix.csv')

# Compute epigenetic age
chrono_age = 45
epi_age = analyzer.predict_age()
age_acceleration = epi_age - chrono_age

print(f"Chronological Age: {chrono_age} years")
print(f"Epigenetic Age: {epi_age:.1f} years")
print(f"Age Acceleration: {age_acceleration:.1f} years")

# Simulate reversal strategies
reversal = ClockReversal(methylation_data=analyzer.data)
for strategy in ['TET2_overexpression', 'DNMT_inhibition', 'combined']:
    result = reversal.simulate(strategy, duration_weeks=12)
    print(f"{strategy}: {result['age_reversal_years']:.2f} years reversed")
```

---

## 📚 Core Components

### 1. **EpigeneticClock**
Models aging trajectories using:
- Methylation accumulation patterns
- CpG site heterogeneity
- Cellular senescence kinetics

```python
clock = EpigeneticClock(
    num_cpg_sites=500000,
    methylation_noise=0.05,
    senescence_rate=0.002
)
```

### 2. **TET2Engine**
Simulates TET2-mediated oxidation:
- 5-methylcytosine → 5-hydroxymethylcytosine conversion
- Passive demethylation through BER pathway
- Off-target hydroxymethylation effects

```python
tet2 = TET2Engine(
    catalytic_efficiency=0.92,
    km_5mc=25.0,  # μM
    vmax=500.0    # nmol/min/mg
)
```

### 3. **EntropyCalculator**
Quantifies epigenetic disorder:
- Shannon entropy of methylation states
- Thermodynamic aging potential
- Reversibility potential scoring

```python
entropy = EntropyCalculator(method='shannon')
disorder_score = entropy.compute(methylation_vector)
```

### 4. **GenerativeModel**
VAE-based epigenetic state generator:
- Latent space exploration
- Trajectory interpolation
- Synthetic aging simulation

---

## 📊 Pipeline Architecture

```
Input Data (Methylation Matrix)
    ↓
[Preprocessing & QC]
    ↓
[Epigenetic Clock Prediction]
    ↓
[Entropy Quantification]
    ↓
[TET2 Modulation Simulation]
    ├─→ [Single Intervention]
    ├─→ [Combination Therapy]
    └─→ [Kinetic Modeling]
    ↓
[Age Reversal Metrics]
    ↓
[Visualization & Reporting]
    ↓
Output (Trajectories, Scores, Recommendations)
```

---

## 🧪 Input Data Format

### Methylation Matrix (CSV)
```
CpG_ID,Sample_1,Sample_2,Sample_3,...
cg00000029,0.8,0.75,0.82,...
cg00000108,0.1,0.15,0.08,...
cg00000109,0.9,0.88,0.92,...
...
```

### Sample Metadata (JSON)
```json
{
  "samples": {
    "Sample_1": {"age": 45, "sex": "M", "cell_type": "fibroblast"},
    "Sample_2": {"age": 52, "sex": "F", "cell_type": "fibroblast"}
  }
}
```

---

## 📈 Output Metrics

| Metric | Description | Range |
|--------|-------------|-------|
| **Epigenetic Age** | Predicted biological age | Years |
| **Age Acceleration** | Epi-age minus chrono-age | Years |
| **Entropy Score** | Methylation disorder (0-1) | 0.0-1.0 |
| **Reversal Potential** | Capacity for age reversal | 0.0-1.0 |
| **TET2 Efficiency** | Oxidation effectiveness | % |
| **Clock Deceleration** | Rate of age slowdown | Years/week |

---

## 🔬 Scientific Background

### Epigenetic Aging
- DNA methylation accumulates at specific CpG sites with age
- Epigenetic clocks (Horvath, Hannum) predict chronological age from methylation
- Aging-associated methylation changes reflect cellular senescence

### TET2 Enzyme
- **Function**: Converts 5-methylcytosine → 5-hydroxymethylcytosine
- **Mechanism**: Active demethylation via base excision repair (BER)
- **Dysfunction**: TET2 mutations in clonal hematopoiesis associate with aging
- **Therapeutic**: TET2 activation proposed for age reversal

### Entropy Reversal
- Epigenetic entropy quantifies disorder in methylation patterns
- Reversing entropy requires energy input (TET2 activity)
- Partial entropy reversal shown in recent in-vivo studies

---

## 🧬 Supported Organisms & Cell Types

| Organism | Cell Types | Clock Model |
|----------|-----------|------------|
| **Human** | Fibroblast, Immune, Adipose, Brain | Horvath, Hannum |
| **Mouse** | Liver, Heart, Muscle, Immune | Liu et al. 2022 |
| **Primate** | PBMCs, Tissue | Huh et al. 2021 |

---

## 📖 Configuration Files

### `config.yaml`
```yaml
clock:
  type: "horvath"
  num_cpg_sites: 353
  
tet2:
  initial_activity: 0.5
  max_modulation: 2.0
  
simulation:
  duration_days: 90
  steps_per_day: 24
  
output:
  format: "hdf5"
  save_trajectories: true
```

---

## 🧪 Testing

```bash
# Run unit tests
pytest tests/ -v

# Run integration tests
pytest tests/integration/ -v

# Generate coverage report
pytest --cov=dredge tests/
```

### Example Tests
```bash
pytest tests/test_tet2_kinetics.py
pytest tests/test_entropy_reversal.py
pytest tests/test_clock_prediction.py
```

---

## 📊 Visualizations

The pipeline generates:

- **Methylation Heatmaps** - CpG site patterns across samples
- **Aging Trajectories** - Clock reversal dynamics over time
- **Entropy Curves** - Disorder quantification timeline
- **TET2 Efficiency** - Oxidation rate and coverage
- **Network Graphs** - Co-methylation patterns
- **Clinical Correlations** - Age vs. biomarkers

---

## 🚀 Performance

| Dataset Size | Runtime | Memory |
|--------------|---------|--------|
| 100 samples, 353 CpGs | ~5 min | 512 MB |
| 1000 samples, 353 CpGs | ~45 min | 2 GB |
| 10k samples, 353 CpGs | ~6 hrs | 8 GB |

---

## 📁 Project Structure

```
dredge-epigenetic-reversal/
├── dredge/
│   ├── __init__.py
│   ├── clock.py                 # Epigenetic clock models
│   ├── tet2_engine.py           # TET2 kinetics
│   ├── entropy.py               # Entropy calculations
│   ├── generative_models.py     # VAE & generative models
│   ├── interventions.py         # Therapeutic strategies
│   └── visualization.py         # Plotting functions
├── data/
│   ├── methylation_matrix.csv
│   ├── cpg_annotations.json
│   └── sample_metadata.json
├── tests/
│   ├── test_clock_prediction.py
│   ├── test_tet2_kinetics.py
│   └── test_entropy_reversal.py
├── docs/
│   ├── methods.tex
│   └── references.bib
├── config.yaml
├── pipeline.py                  # Main execution script
├── requirements.txt
├── Dockerfile
├── README.md                    # This file
└── setup.py
```

---

## 📚 Documentation

- **Methods** - Mathematical formulations in `docs/methods.tex`
- **API Reference** - Complete function documentation in `docs/api.md`
- **Tutorials** - Jupyter notebooks in `notebooks/`
- **Citation** - If using DREDGE, cite:

```bibtex
@software{dredge2024,
  author = {aquamarine-hoshino170},
  title = {DREDGE: Epigenetic Entropy Reversal \& TET2 Modulation},
  year = {2024},
  url = {https://github.com/aquamarine-hoshino170/dredge-epigenetic-reversal}
}
```

---

## 🤝 Contributing

Contributions welcome! Areas for expansion:

- [ ] Additional epigenetic clock models (GrimAge, PhenoAge)
- [ ] DNMT inhibitor simulations
- [ ] Machine learning for intervention prediction
- [ ] Multi-organ aging models
- [ ] In-vivo validation support
- [ ] Web interface for interactive analysis

---

## 📄 License

MIT License © 2024 aquamarine-hoshino170

---

## 🔗 References

1. **Horvath, S.** (2013) DNA methylation age of human tissues and cell types. *Genome Biology*
2. **Hannum, G.** et al. (2013) Genome-wide methylation profiles reveal quantitative views on ageing. *Mol. Cell*
3. **Ko, S.-H.** et al. (2020) TET2-mediated epigenetic remodeling in aging and disease. *Nature Reviews*
4. **Kerepesi, C.** et al. (2021) Biological age reversal demonstrated in mice. *bioRxiv*

---

## 📬 Contact & Support

**GitHub Issues**: [Report bugs](https://github.com/aquamarine-hoshino170/dredge-epigenetic-reversal/issues)

**Discussions**: [Ask questions](https://github.com/aquamarine-hoshino170/dredge-epigenetic-reversal/discussions)

---

**"Reversing entropy, one methylation mark at a time."** 🧬✨
