import tensorflow as tf
import numpy as np
import config 

# this prepares the training data from the config.py file.

x_train = np.array([[0], [1], [2], [3], [4], [5], [6]], dtype=np.float32)
y_train = np.array([np.mean(config.cpuV), np.mean(config.ramV), np.mean(config.fansV), np.mean(config.boardV), np.mean(config.hddV), np.mean(config.opV), np.mean(config.memCrdV)], dtype=np.float32)

# this builds a very simple regression model.
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=16, activation='relu', input_shape=[1]), 
    tf.keras.layers.Dense(units=1)
])

model.compile(optimizer='adam', loss='mean_squared_error')

# This script right here allows the AI to be trained on my CPU, which has 8 cores.
print("The AI model is currently being trained.")
model.fit(x_train, y_train, epochs=500, verbose=0)

# This converts the file from a keras to a tflite file.
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# This script saves the file to my folder.
with open("voltage_model.tflite", "wb") as f:
    f.write(tflite_model)

print("Yay! Now you can use 'voltage_model.tflite' as it is now in your folder.")