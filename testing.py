
import numpy as np
import _pickle as cPickle
import os
import time
from features import feature_extraction
from scipy.io.wavfile import read
import sys


source   = "TestingAudio/"  
modelpath = "TrainedModels2/"
gmm_files = [os.path.join(modelpath,fname) for fname in 
                os.listdir(modelpath) if fname.endswith('.gmm')]
models    = [cPickle.load(open(fname,'rb')) for fname in gmm_files]
speakers   = [fname.split("/")[-1].split(".gmm")[0] for fname 
                in gmm_files]
error = 0
total_sample = 0.0
#paths='/Users/tusharkumar/Desktop/project2/TestingAudio/YogiAdityanath_6.wav'

paths=sys.argv[1]

likelihood_scores = {}
min_likelihoods = {}
max_likelihoods = {}
detected_speakers = []
sr,audio = read(paths)
vector   = feature_extraction(audio,sr)
log_likelihood = np.zeros(len(models)) 
for i in range(len(models)):
        gmm    = models[i]  
        scores = np.array(gmm.score(vector))
        log_likelihood[i] = scores.sum()
                
        winner = np.argmax(log_likelihood)
detected_speaker = speakers[winner]
            
print("\tThe person in the given audio sample is detected as - ", detected_speaker)
          
time.sleep(1.0)
