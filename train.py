print('[Train] Starting...')

# Import the necessary libraries
from sklearn.model_selection import train_test_split
# Import Random Forest Model
from sklearn.linear_model import LinearRegression
from sklearn.kernel_ridge import KernelRidge
# Import scikit-learn metrics module for accuracy calculation
from os import listdir, getcwd
from os.path import isfile, join

import pickle, os
import pandas as pd
import numpy as np

# Get model name
name = input("Set model name:")

# Check and create all folder

# Pre create values
x = [[],[],[]]
y = []

print("[Train] Getting all files for " + name)

# Get all files
path = getcwd() + "/workspace/src/" + name + "/"

# Check for path or create path
if not os.path.exists(path):
    os.makedirs(path)

files = onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

for file in files:
    history = []
    outcome = []

    df = pd.read_csv(path + file, sep=',')
    history = df.iloc[-34:-24]['close']

    y.append(history)
    x[0].append(df.iloc[-24:]['low'])
    x[1].append(df.iloc[-24:]['high'])
    x[2].append(df.iloc[-24:]['close'])

print("[Train] Retrieved and parsed all files.")

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(np.array(x[2]), np.array(y), test_size=0.3) # 70% training and 30% test

print("[Train] Training KernelRidge.")
krr = KernelRidge(alpha=0.2) # Alpha can still be changed. 0.2 showed moderate results. We can use LS to validate.
krr.fit(X_train, y_train)
print("[Train] Score:", krr.score(X_test, y_test))

print("[Train] Training LinearRegression.")
reg_close = LinearRegression().fit(X_train, y_train)
print("[Train] Score close:", reg_close.score(X_test, y_test))

X_train, X_test, y_train, y_test = train_test_split(np.array(x[0]), y, test_size=0.3) # 70% training and 30% test
reg_low = LinearRegression().fit(X_train, y_train)
print("[Train] Score low:", reg_low.score(X_test, y_test))

X_train, X_test, y_train, y_test = train_test_split(np.array(x[1]), y, test_size=0.3) # 70% training and 30% test
reg_high = LinearRegression().fit(X_train, y_train)
print("[Train] Score high:", reg_high.score(X_test, y_test))

print("[Train] Saving models.")

path = getcwd() + "/workspace/saved/" + name + "/"
# Check for path or create path
if not os.path.exists(path):
    os.makedirs(path)

# Dump / save models.
pickle.dump(krr, open(path + "kernelridge.dat", 'wb'))
pickle.dump(reg_close, open(path + "linearregression.dat", 'wb'))

pickle.dump(reg_low, open(path + "linearregression_low.dat", 'wb'))
pickle.dump(reg_high, open(path + "linearregression_high.dat", 'wb'))