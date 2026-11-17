import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("/home/dacur/kaggle_diabetes/diabetes_binary_health_indicators_BRFSS2015.csv")
X = df.drop(columns="Diabetes_binary")
y = df["Diabetes_binary"]

X_dev, X_report, y_dev, y_report = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

X_report.to_csv("data/X_report.csv", index=False)
y_report.to_csv("data/y_report.csv", index=False)
print(len(X_report), y_report.mean())
