from gan_model import build_generator, build_discriminator, build_gan
from blockchain import blockchain_chain, add_block_to_chain
from traceability import hash_image, check_image_in_blockchain
import numpy as np
from tensorflow.keras.datasets import mnist

# Load dataset (using MNIST for example)
(train_images, _), (_, _) = mnist.load_data()
train_images = (train_images.reshape(train_images.shape[0], 28, 28, 1).astype('float32') - 127.5) / 127.5

# Define training parameters
batch_size = 32
epochs = 1
image_count = 0

# Build GAN model
generator = build_generator()
discriminator = build_discriminator()
discriminator.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
gan = build_gan(generator, discriminator)
gan.compile(optimizer="adam", loss="binary_crossentropy")

# Training loop
for epoch in range(epochs):
    for batch in range(int(train_images.shape[0] / batch_size)):
        # Select a random batch of images
        idx = np.random.randint(0, train_images.shape[0], batch_size)
        real_images = train_images[idx]

        # Generate fake images
        noise = np.random.normal(0, 1, (batch_size, 100))
        fake_images = generator.predict(noise)

        # Train Discriminator
        d_loss_real = discriminator.train_on_batch(real_images, np.ones((batch_size, 1)))
        d_loss_fake = discriminator.train_on_batch(fake_images, np.zeros((batch_size, 1)))
        d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)

        # Train Generator
        noise = np.random.normal(0, 1, (batch_size, 100))
        valid_y = np.array([1] * batch_size)
        g_loss = gan.train_on_batch(noise, valid_y)

        # Increment image count
        image_count += batch_size

        # Every 100 images, add a block to the blockchain
        if image_count % 100 == 0:
            # Hash the current batch of images (for simplicity, hashing the noise used to generate them)
            batch_hash = hash_image(noise.tobytes())
            add_block_to_chain(f"Trained on batch of images with hash: {batch_hash}")


        print(f"{epoch}/{epochs}, {batch}/{int(train_images.shape[0] / batch_size)}, D Loss: {d_loss[0]}, G Loss: {g_loss}")

# Traceability check example
user_image_hash = hash_image("C:/Users/WINDOWS 11 PRO/Pictures/Screenshots/Screenshot 2024-04-02 142858.jpg")
block_index = check_image_in_blockchain(user_image_hash)

if block_index is not None:
    print(f"Image was used in training, found in block {block_index}")
else:
    print("Image not found in training data")
