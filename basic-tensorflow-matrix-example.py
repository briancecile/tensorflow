import tensorflow as tf

matrix_1 = tf.constant([ [1,2],
                        [3,4]])
matrix_2 = tf.constant([ [5,6],
                        [7,8]])

print("The Shape of Matrix 1 is {} and of Matrix 2 is {}".format(matrix_1.get_shape(), matrix_2.get_shape()))

multiply_matrices = tf.matmul(matrix_1, matrix_2)

with tf.Session() as sess:
    result = sess.run(multiply_matrices)

print(">> Output")
print(result)
