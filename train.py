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
x = []
y = []

print("[Train] Getting all files.")

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
    for index in df.iloc[-34:-24].index:
        row = df.iloc[index]
        history += [float(row['close'])]

    for index in df.iloc[-24:].index:
        row = df.iloc[index]
        outcome += [float(row['close'])]

    y.append(history)
    x.append(outcome)

X = np.array(x)
y = np.array(y)

print("[Train] Retrieved and parsed all files.")

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3) # 70% training and 30% test

print("[Train] Training KernelRidge.")
krr = KernelRidge(alpha=0.2) # Alpha can still be changed. 0.2 showed moderate results. We can use LS to validate.
krr.fit(X_train, y_train)
print("[Train] Score:", krr.score(X_test, y_test))

print("[Train] Training LinearRegression.")
reg = LinearRegression().fit(X_train, y_train)
print("[Train] Score:", reg.score(X_test, y_test))

print("[Train] Saving models.")

path = getcwd() + "/workspace/saved/" + name + "/"
# Check for path or create path
if not os.path.exists(path):
    os.makedirs(path)

# Dump / save models.
pickle.dump(krr, open(path + "kernelridge.dat", 'wb'))
pickle.dump(reg, open(path + "linearregression.dat", 'wb'))