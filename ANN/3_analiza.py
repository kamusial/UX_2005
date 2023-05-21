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

#####Analiza danych#######

X, y = load_breast_cancer(return_X_y=True, as_frame=True)
# print(X.head())
# print(X.shape)
# print(X.info())
# # print(X.describe())
# print(y.head())
# print(y.shape)
# print(Counter(y))

######   MLP, sklearn    #####
scores = []

kfold = RepeatedStratifiedKFold(n_splits=3, n_repeats=1, random_state=123)
for train, test in kfold.split(X, y):
    clf = MLPClassifier(max_iter=1000, random_state=123)
    X_train, X_test = X.iloc[train, :], X.iloc[test, :]
    y_train, y_test = y.iloc[train], y.iloc[test]
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    scores.append(accuracy_score(y_test, y_pred))
print(scores)


