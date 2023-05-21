import numpy as np
import pandas as pd

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.random import set_seed

set_seed(0)

model = Sequential()
model.add(Dense(4), input_shape=[1], activation="linear")
model.add(Dense(2, activation="linear"))
model.add(Dense(1))

