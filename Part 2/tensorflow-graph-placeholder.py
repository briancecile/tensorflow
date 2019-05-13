### Placeholders are intially empty and are basic data storage mechanisms. For example:
#integer_placeholder = tf.placeholder(tf.int32)
#float_placeholder = tf.placeholder(tf.float64)

import tensorflow as tf
import numpy as np

random_data = np.random.uniform(0,100,(5,5))
random_weights = np.random.uniform(0,100,(5,1))

print(random_data)
print(random_weights)

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)

add_operation = a + b
multiply_operation = a * b

with tf.Session() as sess:
    add_result = sess.run(add_operation,
                          feed_dict= {a:random_data,
                          b:random_weights})

    mult_result = sess.run(multiply_operation,
                          feed_dict= {a:random_data,
                          b:random_weights})

    print(add_result)
    print('\n')
    print(mult_result.round())

