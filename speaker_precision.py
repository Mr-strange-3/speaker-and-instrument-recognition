import numpy as np
import _pickle as cPickle
import os
import time
from features import feature_extraction
from scipy.io.wavfile import read
from sklearn.metrics import silhouette_score
from sklearn.metrics import davies_bouldin_score
from sklearn.cluster import KMeans


true_labels = []
predicted_labels = []
source = "TestingAudio/"
modelpath = "TrainedModels2/"
gmm_files = [os.path.join(modelpath, fname) for fname in os.listdir(modelpath) if fname.endswith('.gmm')]
models = [cPickle.load(open(fname, 'rb')) for fname in gmm_files]
speakers = [fname.split("/")[-1].split(".gmm")[0] for fname in gmm_files]
error = 0
total_sample = 0.0
likelihoods = []
for root, dirs, files in os.walk(source):
    for file in files:
        total_sample += 1.0
        path = os.path.join(root, file)
        sr, audio = read(path)
        vector = feature_extraction(audio, sr)
        log_likelihood = np.zeros(len(models))
        for i in range(len(models)):
            gmm = models[i]
            scores = np.array(gmm.score(vector))
            log_likelihood[i] = scores.sum()
            likelihoods.append(np.exp(scores))
        winner = np.argmax(log_likelihood)
        true_label = path.split("_")[0].split("/")[-1]
        true_labels.append(true_label)
        predicted_label = speakers[winner]
        predicted_labels.append(predicted_label)
        if predicted_label != true_label:
            error += 1
        time.sleep(1.0)

accuracy = ((total_sample - error) / total_sample) * 100
print("Accuracy:", accuracy,"\n",)
kmeans = KMeans(n_clusters=10, random_state=0,n_init=10).fit(vector)
p= kmeans.labels_


davies_bouldin = davies_bouldin_score(vector, p)
print("Davies-Bouldin Index:", davies_bouldin)
silhouette_avg = silhouette_score(vector, p)
print("Silhouette Score:", silhouette_avg)

total_likelihood = np.sum(likelihoods, axis=0)
print("total likelihood:",total_likelihood)
