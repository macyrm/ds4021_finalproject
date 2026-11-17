# ds4021_finalproject

Predicting diabetes from self-reported health indicators

## Data

Source: Diabetes Health Indicators Dataset on Kaggle
(www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset),
a cleaned version/subset of the CDC's 2015 BRFSS survey

The reporting set in `data/` (`X_report.csv`, `y_report.csv`) was created from `diabetes_binary_health_indicators_BRFSS2015.csv` (the full 253,680 row file) using `split_data.py`, which is a 20% split stratified on `Diabetes_binary` with
`random_state=42` (50,736 rows). It needs to not be touched until the final phase of the project as per the guidelines/instructions for the project. To recreate the same 80% development set to work with, run the same split with the same
seed for consistent reproducibility.
