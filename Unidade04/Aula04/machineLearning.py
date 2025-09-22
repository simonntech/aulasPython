import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

X_train = tf.constant([[1.0], [2.0], [3.0], [4.0]])
y_train = tf.constant([[2.0], [4.0], [6.0], [8.0]])

model = Sequential()
model.add(Dense(units=1, input_shape=(1,)))
model.compile(optimizer='sgd', loss='mean_squared_error')

model.fit(X_train, y_train, epochs=1000, verbose=0)

X_new = tf.constant([[5.0]])
prediction=model.predict(X_new)
print('Predição:', prediction[0][0])
plt.ylabel('Notas')
plt.show()