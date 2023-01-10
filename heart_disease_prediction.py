# import libraries

import pandas as pd
import pickle

dataset = pd.read_csv('https://raw.githubusercontent.com/nessasunjaya/KNN-to-Predict-Heart-Failure/main/heart.csv', on_bad_lines='skip')

# handling categorical data

columns = dataset.columns

for column in columns:
  if dataset[column].dtype == 'object':
    dataset[column] = dataset[column].astype('category')
    dataset[column] = dataset[column].cat.codes

# Separating X (contributing value) and Y (predicted value)

Y = dataset['HeartDisease']
X = dataset.drop(['HeartDisease', 'RestingECG'], axis=1)

# Standardizing Numerical Data

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X[['Age','RestingBP','Cholesterol','MaxHR','Oldpeak']] = scaler.fit_transform(X[['Age','RestingBP','Cholesterol','MaxHR','Oldpeak']])

# Separating data to Training and Testing Data

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X ,Y, test_size=0.3, random_state=42)

# Using KNN to Build Model

from sklearn.neighbors import KNeighborsClassifier
KNN_model = KNeighborsClassifier(n_neighbors=5)

KNN_model.fit(X_train,y_train)
KNN_predictions = KNN_model.predict(X_test)

pickle.dump(KNN_model, open('model.pkl', 'wb'))