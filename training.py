
import numpy as np
from sklearn.mixture import GaussianMixture as GMM
import _pickle as cPickle
from scipy.io.wavfile import read
import os
from features import feature_extraction
source='TrainingAudio/'
dest='TrainedModels2/'
train_file='Voice_Samples_Training_Path.txt'
file_path=open(train_file,'r')
count=1
features=np.asarray(())
for path in file_path:
    path.strip()
    print(path)
    sr,audio= read((source+path).rstrip())
      
    if(len(audio)>0):
      vector=feature_extraction(audio,sr)
      if features.size==0:
         features=vector
      else:
        
         features=np.vstack((features,vector))
      if count==5:
        gmm=GMM(n_components=2,covariance_type='spherical',n_init=3,reg_covar=1e-9)
        gmm.fit(features)
        path=path.split("-")[0]
        path=path.rstrip()
        p_file = os.path.splitext(path)[0] + ".gmm"
        print(dest+p_file)
        cPickle.dump(gmm,open(dest+p_file,'wb'))
        print('+ modeling compeleted for speaker: ' ,p_file,"with data point = ",features.shape)
        features=np.asarray(())
        count =0
      count=count+1

    else:
       print("file empty")   

