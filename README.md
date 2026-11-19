# Predicting Diabetes from Self-Reported Health Indicators

DS 4021 final project. We train and compare machine learning models that predict diabetes from self-reported health, lifestyle and socioeconomic survey indicators, and identify which factors are most predictive.

## Repository Contents

### Software and Platform
- Python 3.x, Jupyter Notebook
- Packages: pandas, numpy, scikit-learn, matplotlib, seaborn, PyTorch
- Operating system: Ubuntu (WSL) on Windows 11

### Documentation Map
```
ds4021_finalproject/
├── README.md              This file
├── final_report.pdf       Final report (to be added)
├── split_data.py          Creates the train/reporting split
├── Data/
│   ├── X_train.csv        Training features (80%, 202,944 rows)
│   ├── y_train.csv        Training labels
│   ├── X_report.csv       Reporting-set features (20%, 50,736 rows), held out
│   └── y_report.csv       Reporting-set labels, held out
├── NOTEBOOKS/
│   ├── 01_descriptive_analysis.ipynb
│   └── (individual model notebooks and final evaluation)
└── OUTPUT/                Saved figures and tables
```

### Group Member Responsibilities
| Member | Individual modeling assignment | Group tasks |
|---|---|---|
| Nathaniel Horton | Penalized linear & SVM | Repo Formatting, Descriptive Analysis Notebook |
| Macy Moore | Bagging-type & boosting-type | TBD |
| Ava Lawless | Neural network | TBD |

## Data
Source: [Diabetes Health Indicators Dataset](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset) on Kaggle, a cleaned subset of the CDC's 2015 BRFSS survey. We use `diabetes_binary_health_indicators_BRFSS2015.csv` (253,680 rows, 21 features).

`split_data.py` makes an 80/20 split stratified on `Diabetes_binary` with `random_state=42`. The reporting set (`Data/X_report.csv`, `Data/y_report.csv`) was created in the prerequisite assignment and has not been opened or regenerated since. It is used only in the final evaluation notebook. All modeling uses `Data/X_train.csv` and `Data/y_train.csv`.
