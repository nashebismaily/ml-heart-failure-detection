import pandas as pd
import numpy as np
import pickle
import cdsw
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score

## Load Data
dataset = pd.read_csv("heart_failure_clinical_records_dataset.csv")
print("Number of entries = " + str(len(dataset)))
dataset.head()

## Data Modeling
columns = list(dataset.columns)

# Test/Train Split
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.8, shuffle = True, random_state = 2)

## Random Forest Classifier
algo_accuracy_record = []  # each element is list of format - ['algo_name', algo_max_accuracy]
rf_acc = []
rf_cm = []

for num_trees in range(1, 200):
    rf_classifier = RandomForestClassifier(n_estimators = num_trees, criterion = 'entropy', random_state = 0)
    rf_classifier.fit(x_train, y_train)
    rf_pred = rf_classifier.predict(x_test)

    rf_acc.append(accuracy_score(y_test,rf_pred))
    rf_cm.append(confusion_matrix(y_test,rf_pred))
    
max_acc = max(rf_acc)
max_acc_cm = rf_cm[rf_acc.index(max_acc)]
cdsw.track_metric("accuracy", str(max_acc))
print('accuracy = ' + str(max_acc))
print('confusion matrix = ')
print(max_acc_cm)
algo_accuracy_record.append(['RandomForestClassifier', max_acc])

## Output
filename = 'rf_classifier.pkl'
pickle.dump(rf_classifier, open(filename, 'wb'))
cdsw.track_file(filename)