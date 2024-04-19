import pickle 
from sklearn.metrics import precision_score, f1_score, fbeta_score,accuracy_score
from instr import X_test,y_test
with open('svm_model.pkl', 'rb') as f:
    svm_model = pickle.load(f)
    y_pred = svm_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted', zero_division=0.0)
f1 = f1_score(y_test, y_pred, average='weighted')
f2 = fbeta_score(y_test, y_pred, beta=2, average='weighted')
print("accuracy :",accuracy,"\n","Precision:", precision,"\n","F1 score:", f1,"\n","F2 score:", f2)
