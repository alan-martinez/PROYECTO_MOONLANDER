import tensorflow as tf
import numpy as np

n_inputs = 8
n_hidden1 = 32
n_hidden2 = 16
n_outputs = 1

X = tf.placeholder(tf.float32, shape=(None, n_inputs))
hidden1 = tf.layers.dense(X, n_hidden1, activation=tf.nn.relu)
hidden2 = tf.layers.dense(hidden1, n_hidden2, activation=tf.nn.relu)
outputs = tf.layers.dense(hidden2, n_outputs, activation=tf.nn.sigmoid)

y = tf.placeholder(tf.float32, shape=(None, n_outputs))
loss = tf.reduce_mean(tf.square(y - outputs))
optimizer = tf.train.AdamOptimizer()
training_op = optimizer.minimize(loss)

init = tf.global_variables_initializer()
n_epochs = 100
batch_size = 50

