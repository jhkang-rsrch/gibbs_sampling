# Bayesian SSVS Gibbs Sampling 
## Reproducing Table 1 & Table 2

This repository reproduces **Table 1** and **Table 2** from the classical paper:

> George & McCulloch (1993),  
> *Variable Selection via Gibbs Sampling*,  
> Journal of the American Statistical Association (JASA).

---

## 🚀 Quick Start

```bash
git clone https://github.com/jhkang-rsrch/gibbs_sampling.git
cd gibbs_sampling

# (Optional) Create virtual environment
python3 -m venv gibbs
source gibbs/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run simulations
python main.py
```

---

## 📁 Folder Structure

```
.
├── main.py              # Table1 & Table2 full pipeline
├── requirements.txt
├── src/
│   ├── generate_data.py   # Example 4.1 & 4.2
│   ├── ssvs_core.py       # Gibbs sampler core
│   ├── run_ssvs.py        # SSVS + summary
│   ├── table1.py          # Reproduce Table 1
│   ├── table2.py          # Reproduce Table 2
│   ├── export_pdf.py      # Export CSV → PDF
├── results/               # CSV outputs
├── report/                # PDF outputs
└── data/                  # Raw datasets (.npz)
```

---

## 📊 Output Summary

| Table | CSV Output | PDF Output |
|-------|------------|------------|
| Table 1 | `results/table1.csv` | `report/table1.pdf` |
| Table 2 | `results/table2.csv` | `report/table2.pdf` |

---

## 📌 Citation

```bibtex
@article{george1993gibbs,
  title={{Variable Selection via Gibbs Sampling}},
  author={George, Edward I and McCulloch, Robert E},
  journal={Journal of the American Statistical Association},
  year={1993}
}
```

---

## ⚡ Tip for Faster Simulation

```
# In src/table2.py
# Change these parameters to reduce runtime

n_iter = 10000    # default: 30000  
burn_in = 3000    # default: 5000
```

---

## 🔜 Future Directions

- Jupyter Notebook for lecture/presentation  
- Multiple seed experiments / posterior stability  
- GitHub Actions (CI) for reproducibility  
- Single PDF research report  

---
