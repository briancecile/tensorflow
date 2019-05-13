import tensorflow as tf

random_var = tf.random_uniform((4,4),0,1)

init = tf.global_variables_initializer()
with tf.Session() as sess:
    init.run()
    print(random_var.eval())
