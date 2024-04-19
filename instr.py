import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import numpy as np
import pickle
from instrf import extract_features
data = pd.read_csv('instrument.csv')
X = []
for index, row in data.iterrows():
    file_path = 'TinySOL/' + row['Path']  
    features = extract_features(file_path)
    X.append(features)
X = np.array(X)
y = data['Instrument (in full)']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
svm_model = SVC(kernel='rbf', gamma='scale', C=1.0) 
svm_model.fit(X_train, y_train)
with open('svm_model.pkl', 'wb') as f:
    pickle.dump(svm_model, f)
