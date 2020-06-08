import tensorflow as tf
import tensorflow.keras.layers as layers
import numpy as np
import os
#os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

data = np.load("training_data.npy", allow_pickle=True)
X =[]
y =[]
for d in data:
	X.append(d[0])
	y.append(d[1])
del data
X = np.array(X).reshape(-1, 149, 250, 1)/255.0
y = np.array(y)

print(X.shape)
print(y.shape)


model = tf.keras.Sequential([
	layers.Conv2D(64, (5, 5), activation='relu', input_shape=(149, 250, 1)),
	layers.Conv2D(128, (5, 5), strides=(2,2), activation='relu'),
	layers.Conv2D(128, (5, 5), strides=(2,2), activation='relu'),
	#layers.MaxPooling2D(pool_size=(2,2)),
	layers.Flatten(),
	layers.Dense(256, activation='relu'),
	layers.Dense(19, activation='sigmoid')
])

adam = tf.keras.optimizers.Adam(learning_rate=0.001)
model.compile(optimizer=adam, loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()
#model.load_weights("model.h5")
model.fit(X, y, epochs=3)
#model.save_weights("model.h5")

