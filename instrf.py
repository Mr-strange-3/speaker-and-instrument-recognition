import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import librosa
import numpy as np
import pickle 
def extract_features(file_path):
    audio, sr = librosa.load(file_path)
    audio_float = audio.astype(np.float32)
    noise_reduced_audio = librosa.effects.preemphasis(audio_float)
    mfccs = librosa.feature.mfcc(y=noise_reduced_audio, sr=sr, n_mfcc=13)
    mfccs_mean = np.mean(mfccs, axis=1)
    return mfccs_mean