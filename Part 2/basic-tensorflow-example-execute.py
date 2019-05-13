import tensorflow as tf

first_string = tf.constant('Hello')
second_string = tf.constant(' World')
combined_string = (first_string + second_string)

with tf.Session() as sess:
    result = sess.run(combined_string)
    print (result)
