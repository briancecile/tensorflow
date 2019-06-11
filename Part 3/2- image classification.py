from __future__ import absolute_import, division, print_function

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']


#what does our training data look like?
########################################
#print("Test Data...")
#print(train_images.shape)
#print(len(train_labels))
#print(train_labels)

#what does out testing data look like?
########################################
#print("\nTest Data...")
#print(test_images.shape)
#print(len(test_labels))
#print(test_labels)
#print("\n")

#let's inspect the data, specifically the first training image
########################################
#plt.figure()
#plt.imshow(train_images[0])
#plt.colorbar()
#plt.grid(False)
#plt.show()

#since the images have a pixel value between 0-255, we set the training and test images to a value between 0-1 by dividing by 2255
train_images = train_images / 255.0
test_images = test_images / 255.0

#lets see the first 25 training images.
########################################
#plt.figure(figsize=(10,10))
#for i in range(25):
#    plt.subplot(5,5,i+1)
#    plt.xticks([])
#    plt.yticks([])
#    plt.grid(False)
#    plt.imshow(train_images[i], cmap=plt.cm.binary)
#    plt.xlabel(class_names[train_labels[i]])
#plt.show()

#time to train our model
########################################
#model = keras.Sequential([
#                          keras.layers.Flatten(input_shape=(28, 28)),
#                          keras.layers.Dense(128, activation=tf.nn.relu),
#                          keras.layers.Dense(10, activation=tf.nn.softmax)
#                          ])
#
#model.compile(optimizer='adam',
#              loss='sparse_categorical_crossentropy',
#              metrics=['accuracy'])
#
#model.fit(train_images, train_labels, epochs=5)

#next, check to see how the model
#performs against the test data
########################################
#test_loss, test_acc = model.evaluate(test_images, test_labels)
#print('Test accuracy:', test_acc)

#time to make predictions!
########################################
#predictions = model.predict(test_images)
#print(predictions[0])
#print(np.argmax(predictions[0]))
#print(class_names[np.argmax(predictions[0])])
#print('\nIs othe prediction correct?')
#print('Expected integer value:')
#print(test_labels[0])
#print('Expected class name:')
#print(class_names[test_labels[0]])

#lets make a prediction on a single image
########################################
#print('\nSingle prediction')
#img = test_images[0]
#print('image shape:')
#print(img.shape)
#img = (np.expand_dims(img,0))
#predictions_single = model.predict(img)
#print('Predicted class name:')
#print(class_names[np.argmax(predictions_single[0])])
