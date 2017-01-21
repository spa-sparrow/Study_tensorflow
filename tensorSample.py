import tensorflow as tf;

x = tf.constant(1, name = 'x');
y = tf.Variable(x + 2, name = 'y');

print(y);