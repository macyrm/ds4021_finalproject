import pandas as pd
from sklearn.model_selection import train_test_split

# full binary dataset from Kaggle (253,680 rows)
df = pd.read_csv("/home/dacur/kaggle_diabetes/diabetes_binary_health_indicators_BRFSS2015.csv")
X = df.drop(columns="Diabetes_binary")
y = df["Diabetes_binary"]

# 80/20 split, stratified on target, fixed seed for reproducibility
X_dev, X_report, y_dev, y_report = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

# training set
X_dev.to_csv("Data/X_train.csv", index = False)
y_dev.to_csv("Data/y_train.csv", index = False)

# reporting set (20%, 50,736 rows) was written by the original run of this script, (Data/X_report.csv and Data/y_report.csv).
# It's not regenerated here and stays untouched until the final evaluation notebook as requested in the instructions.
print(len(X_dev), y_dev.mean())
