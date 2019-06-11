from __future__ import absolute_import, division, print_function

import os
import tfcoreml as tf_converter
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
from tensorflow.python.tools import freeze_graph

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

#since the images have a pixel value between 0-255, we set the training and test images to a value between 0-1 by dividing by 2255
train_images = train_images / 255.0
test_images = test_images / 255.0

#create checkpoints for saving our model
checkpoint_path = "./fashion_training/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

# Create checkpoint callback
cp_callback = keras.callbacks.ModelCheckpoint(checkpoint_path,
                                              save_weights_only=False,
                                              verbose=1)

#time to train our model
########################################
model = keras.Sequential([
                          keras.layers.Flatten(input_shape=(28, 28)),
                          keras.layers.Dense(128, activation=tf.nn.relu),
                          keras.layers.Dense(10, activation=tf.nn.softmax)
                          ])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5, callbacks = [cp_callback])  #pass in the checkpoint we created

FASHION_SAVED_MODEL = './saved_models/fashion'
saved_model = tf.contrib.saved_model.save_keras_model(model, FASHION_SAVED_MODEL)

#convert to TensorFlow Lite for Android
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model)
tflite_model = converter.convert()
open('converted_fashion_model.tflite', 'wb').write(tflite_model)

#convert to CoreML for iOS
def frozen_graph_maker(export_dir,output_graph):
    with tf.Session(graph=tf.Graph()) as sess:
        tf.saved_model.loader.load(sess, [tf.saved_model.tag_constants.SERVING], export_dir)
        output_nodes = [n.name for n in tf.get_default_graph().as_graph_def().node]
        output_graph_def = tf.graph_util.convert_variables_to_constants(
                                                                    sess, # The session is used to retrieve the weights
                                                                    sess.graph_def,
                                                                    output_nodes# The output node names are used to select the usefull nodes
                                                                    )
        # Finally we serialize and dump the output graph to the filesystem
        with tf.gfile.GFile(output_graph, "wb") as f:
            f.write(output_graph_def.SerializeToString())

output_graph = "frozen_graph.pb"
frozen_graph_maker(saved_model,output_graph)

tf_converter.convert(tf_model_path=output_graph,
                     mlmodel_path='converted_fashion_model.mlmodel',
                     output_feature_names=['dense_1/Softmax:0'])

