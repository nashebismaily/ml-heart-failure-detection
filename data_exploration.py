import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

## Data Load

dataset = pd.read_csv("heart_failure_clinical_records_dataset.csv")
print("Number of entries = " + str(len(dataset)))
dataset.head()

## Feature Distribution - Numerical
numerical_features = ["age", "creatinine_phosphokinase", "ejection_fraction", "platelets", "serum_creatinine", "serum_sodium"]
categorical_features = ["anaemia", "diabetes", "high_blood_pressure", "sex", "smoking"]

plt.figure(figsize=(18, 27))
for i, col in enumerate(numerical_features):
    plt.title(col)
    sns.kdeplot(dataset.loc[dataset["DEATH_EVENT"]==0, col], label="alive")
    sns.kdeplot(dataset.loc[dataset["DEATH_EVENT"]==1, col], label="dead")
    sns.boxplot(y = col, data = dataset, x="DEATH_EVENT") 
    plt.show()
    
## Feature Distribution - Categorical
plt.figure(figsize=(12, 8))
for i, col in enumerate(categorical_features):
    plt.title(col)
    sns.countplot(data=hf, x=col, hue="DEATH_EVENT")
    plt.show()

## Data Normalization
from sklearn.preprocessing import StandardScaler
import matplotlib.image as mpimg
from matplotlib import gridspec

dataset_norm = dataset.copy()
for i, col in enumerate(numerical_features):
    dataset_norm[[col]] = StandardScaler(with_mean=True, with_std=True).fit_transform(dataset_norm[[col]])
    
## Correlation Matrix
all_features = categorical_features.copy()
all_features.extend(numerical_features)
plt.figure(figsize=(8, 7))
sns.heatmap(dataset_norm[all_features].corr(method='pearson'), vmin=-1, vmax=1, cmap='viridis', annot=True, fmt='.2f');
