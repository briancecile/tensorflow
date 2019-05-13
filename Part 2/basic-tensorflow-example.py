import tensorflow as tf

first_string = tf.constant('Hello')
second_string = tf.constant(' World')

print('\nType of first_string')
print (type(first_string))

combined_string = (first_string + second_string)

print('\nType of combined_string')
print (type(combined_string))

print('\nCombined String is:')
print (combined_string)
