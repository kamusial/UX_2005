import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
penguins = sns.load_dataset('penguins')
#penguins['species'] = penguins['species'].astype('category')
print(penguins)

penguins_filtered = penguins.drop(columns=['island', 'sex']).dropna()
penguins_features = penguins_filtered.drop(columns=['species'])

target = pd.get_dummies(penguins_filtered['species'])
print(target)
X_train, X_test, y_train, y_test = train_test_split(penguins_features, target, test_size=0.2, random_state=5)

from tensorflow import keras
from numpy.random import seed
seed(1)
from tensorflow.random import set_seed
set_seed(2)

print(X_train.shape)

inputs = keras.Input(shape=X_train.shape[1])
hidden_layer1 = keras.layers.Dense(20, activation="relu")(inputs)
hidden_layer2 = keras.layers.Dense(20, activation="relu")(hidden_layer1)
hidden_layer3 = keras.layers.Dense(20, activation="relu")(hidden_layer2)
output_layer = keras.layers.Dense(3, activation="softmax")(hidden_layer3)
model = keras.Model(inputs=inputs, outputs=output_layer)
#print(model.summary())

model.compile(optimizer='adam', loss=keras.losses.CategoricalCrossentropy())
history = model.fit(X_train, y_train, epochs=1000)
sns.lineplot(x=history.epoch, y=history.history['loss'])
plt.show()
y_pred = model.predict(X_test)
prediction = pd.DataFrame(y_pred, columns=target.columns)
print(prediction)
predicted_species = prediction.idxmax(axis='columns')
print(predicted_species)

from sklearn.metrics import confusion_matrix

true_species = y_test.idxmax(axis="columns")
matrix = confusion_matrix(true_species, predicted_species)
print(matrix)

confusion_df = pd.DataFrame(matrix, index=y_test.columns.values, columns=y_test.columns.values)
confusion_df.index.name = 'True Label'
confusion_df.columns.name = 'Predicted Label'

sns.heatmap(confusion_df, annot=True)
plt.show()
