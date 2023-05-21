import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import shutil
import sys
import tensorflow as tf
from collections import Counter
from numpy.random import seed
from sklearn.datasets import load_breast_cancer, load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import accuracy_score as acc_score
from sklearn.model_selection import cross_val_score, RepeatedStratifiedKFold, train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from tensorflow.keras import Sequential
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.callbacks import *
from tensorflow.keras.datasets import mnist, cifar10
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator

pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 5000)
pd.set_option('display.width', 10000)
pd.set_option('display.max_colwidth', 10000)
np.set_printoptions(linewidth=2000)

X, y = load_wine(return_X_y=True, as_frame=True)
print(Counter(y))

scores = []

kfold = RepeatedStratifiedKFold(n_splits=5, n_repeats=3, random_state=666)
for train, test in kfold.split(X, y):
    clf = MLPClassifier(max_iter=2000, random_state=666)
    X_train, X_test = X.iloc[train, :], X.iloc[test, :]
    y_train, y_test = y.iloc[train], y.iloc[test]

    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.fit_transform(X_test)

    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    scores.append(accuracy_score(y_test, y_pred))
print(scores)

############   RandomForestClassifier()

# kfold = RepeatedStratifiedKFold(n_splits=5, n_repeats=3, random_state=123)
# for train, test in kfold.split(X, y):
#     clf = RandomForestClassifier()
#     X_train, X_test = X.iloc[train, :], X.iloc[test, :]
#     y_train, y_test = y.iloc[train], y.iloc[test]
#     clf.fit(X_train, y_train)
#     y_pred = clf.predict(X_test)
#     scores.append(accuracy_score(y_test, y_pred))
# print(scores)
