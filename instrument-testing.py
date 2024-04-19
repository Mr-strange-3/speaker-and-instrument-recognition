import numpy as np
import pickle 
from instrf import extract_features
import sys
from instr import X_train,X_test,y_train,y_test
from sklearn.metrics import precision_score, f1_score, fbeta_score,accuracy_score
with open('svm_model.pkl', 'rb') as f:
    svm_model = pickle.load(f)
paths=sys.argv[1]

# paths='/Users/tusharkumar/Desktop/project2/TinySOL/Keyboards/Accordion/ordinario/Acc-ord-A#2-mf-alt3-N.wav'

features = extract_features(paths)
features = np.array(features).reshape(1, -1)
predicted_instrument_family = svm_model.predict(features)[0]
detected_speaker=predicted_instrument_family
print("\tThe instrument in the given audio sample is detected as - ", detected_speaker)
   





                