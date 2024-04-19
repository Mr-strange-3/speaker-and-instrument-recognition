import librosa
import numpy as np
from sklearn import preprocessing
import python_speech_features as mfcc
def cal_delta(array):
    
    row,cols=array.shape
    deltas=np.zeros((row,20))
    n=2
    for i in range(row):
        index=[]
        j=1
        while(j<=n):
            if i-j<0:
                first=0
            else:
                first=i-j
            if i+j>row-1:
                second=row-1
            else:
                second=i+j
            index.append((second,first))
            j+=1
        deltas[i]=(array[index[0][0]]-array[index[0][1]]+ 2*(array[index[1][0]]- array[index[1][1]]))  /10
    return deltas
def feature_extraction(audio,rate):
   if len(audio) == 0:
        print("Empty audio signal. Skipping feature extraction.")
        return None
   audio_float = audio.astype(np.float32)

    # Apply preemphasis filter
   noise_reduced_audio = librosa.effects.preemphasis(audio_float)
   mfcc_feature=mfcc.mfcc(noise_reduced_audio,rate,0.025,0.01,20,nfft=1200,appendEnergy=True)
   mfcc_feature=preprocessing.scale(mfcc_feature)
   delta=cal_delta(mfcc_feature)
   comb=np.hstack((mfcc_feature,delta))
   return comb


