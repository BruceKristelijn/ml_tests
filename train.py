# Import the necessary libraries
from sklearn.model_selection import train_test_split
# Import Random Forest Model
from sklearn.ensemble import RandomForestClassifier
# Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics
from os import listdir, getcwd
from os.path import isfile, join

import pandas as pd

# Pre create values
x = []
y = []

# Get all files
path = getcwd() + "/workspace/src/"
files = onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

for file in files:
    history = []
    outcome = []

    df = pd.read_csv(path + file, sep=',')
    for index in df.iloc[:-24].index:
        row = df.iloc[index]
        history += [float(row['close'])]

    for index in df.iloc[-24:].index:
        row = df.iloc[index]
        outcome += [float(row['close'])]

    # print(history)
    # print(outcome)
    # exit()
    y.append(history)
    x.append(outcome)

# print(type(y[0][0]))
# exit()

# print(x.shape())

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3) # 70% training and 30% test

#Create a Gaussian Classifier
clf=RandomForestClassifier(n_estimators=1000)

#Train the model using the training sets y_pred=clf.predict(X_test)
clf.fit(X_train,y_train)

y_pred=clf.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))