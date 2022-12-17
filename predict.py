# Script will predict for ticker
from dotenv import load_dotenv

import pickle, os
import pandas as pd
import numpy as np

name = input("Model / ticker name: ")

data_path = os.getcwd() + "/workspace/dat/dat_" + name + ".csv"
model_path = os.getcwd() + "/workspace/saved/" + name + "/"

krr = pickle.load(open(model_path + 'kernelridge.dat', 'rb'))
reg = pickle.load(open(model_path + 'linearregression.dat', 'rb'))

df = pd.read_csv(data_path)
data = [df.iloc[-24:]['close']]

print(krr.predict(data))
print(reg.predict(data))