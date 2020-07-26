#Have to give the path of CSV or nomalized txt file to convert into numpy array
import pandas as pd
import numpy as np

files=pd.read_csv("Normalized_files_abir/5000_pos_PCKNC_nor.txt",sep=",",header=None)
a=files.values
b=np.delete(a,0,axis=1)
#print(b)
#print(a)
np.save("5000_pos_PCKNC_nor.npy",b)
#data=np.load("5000_pos_PCKNC_nor.npy")
#print(data)