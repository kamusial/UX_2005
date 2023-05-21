import numpy as np
import pandas as pd

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.random import set_seed
import matplotlib.pyplot as plt
set_seed(0)
np.random.seed(0)

#model
model = Sequential()
model.add(Dense(1, input_shape=[1], activation="linear"))
model.add(Dense(4, activation="linear"))
model.add(Dense(4, activation="linear"))
model.add(Dense(4, activation="linear"))
model.add(Dense(1))

#kompilacja
model.compile(optimizer="rmsprop", loss="mse", metrics=["mae"])

df = pd.read_csv("f-c.csv", usecols=[1,2])


result = model.fit(df.F, df.C, epochs=500, verbose=1)
print(result.history.keys())

df1 = pd.DataFrame(result.history)
print(df1.head())
df1.plot()
plt.show()

C_pred = model.predict(df.F)

plt.scatter(df.F, df.C)
plt.plot(df.F, C_pred, c='r')
plt.show()

