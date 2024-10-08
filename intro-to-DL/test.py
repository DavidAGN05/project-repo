import tensorflow as tf

# Download and import the MIT Introduction to Deep Learning package
import mitdeeplearning as mdl

import numpy as np
import matplotlib.pyplot as plt

sport = tf.constant("Tennis", tf.string)
number = tf.constant(1.41421356237, tf.float64)

print("`sport` is a {}-d Tensor".format(tf.rank(sport).numpy()))
print("`number` is a {}-d Tensor".format(tf.rank(number).numpy()))