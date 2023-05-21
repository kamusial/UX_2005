import numpy as np
import pandas as pd

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.random import set_seed
import matplotlib.pyplot as plt
set_seed(0)

#model
model = Sequential()
model.add(Dense(4, input_shape=[1], activation="linear"))
model.add(Dense(2, activation="linear"))
model.add(Dense(1))

#kompilacja
model.compile(optimizer="rmsprop", loss="mse")

df = pd.read_csv("f-c.csv", usecols=[1,2])

plt.scatter(df.F, df.C)
plt.show()




