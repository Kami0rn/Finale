import tensorflow as tf
from tensorflow.keras import layers

# Generator
def build_generator():
    model = tf.keras.Sequential()
    model.add(layers.Dense(128, activation="relu", input_dim=100))
    model.add(layers.Dense(784, activation="sigmoid"))
    model.add(layers.Reshape((28, 28, 1)))
    return model

# Discriminator
def build_discriminator():
    model = tf.keras.Sequential()
    model.add(layers.Flatten(input_shape=(28, 28, 1)))
    model.add(layers.Dense(128, activation="relu"))
    model.add(layers.Dense(1, activation="sigmoid"))
    return model

# Combine them into a GAN
def build_gan(generator, discriminator):
    model = tf.keras.Sequential()
    model.add(generator)
    model.add(discriminator)
    return model
#gg