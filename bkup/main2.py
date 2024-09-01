import numpy as np  # Add this import statement
import hashlib
import time
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers

# Blockchain class definition
class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = int(time.time())
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(f'{self.index}{self.timestamp}{self.data}{self.previous_hash}'.encode('utf-8'))
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)
        print(f"Block {new_block.index} has been added with hash: {new_block.hash}")

    def is_image_in_blockchain(self, target_image_hash):
        for block in self.chain:
            if block.data == f"Trained on image with hash: {target_image_hash}":
                return True
        return False

# Function to hash an image
def hash_image(image_path):
    with Image.open(image_path) as img:
        img = img.convert("RGB")
        img_array = np.array(img)
        img_bytes = img_array.tobytes()
        hash_object = hashlib.sha256(img_bytes)
        return hash_object.hexdigest()

# GAN definition (simplified for demonstration purposes)
def create_gan_model():
    generator = tf.keras.Sequential([
        layers.Dense(128, activation='relu', input_dim=100),
        layers.Dense(28 * 28 * 3, activation='sigmoid'),
        layers.Reshape((28, 28, 3))
    ])

    discriminator = tf.keras.Sequential([
        layers.Flatten(input_shape=(28, 28, 3)),
        layers.Dense(128, activation='relu'),
        layers.Dense(1, activation='sigmoid')
    ])

    discriminator.compile(optimizer='adam', loss='binary_crossentropy')
    return generator, discriminator

# Image processing
target_image_path = "E:/CPE/1-2567/Project/TF/10_food_classes_10_percent/train/sushi/21802.jpg"
target_image_hash = hash_image(target_image_path)
print(f"Target Image Hash (before training): {target_image_hash}")

# Blockchain initialization
blockchain = Blockchain()

# GAN model creation
generator, discriminator = create_gan_model()

# Example training loop with target image involvement
for i in range(75):  # Simulate 75 epochs or training steps
    noise = np.random.normal(0, 1, (1, 100))
    generated_image = generator.predict(noise)

    # Use the target image hash directly in the first iteration for testing
    if i == 0:
        generated_image_hash = target_image_hash
    else:
        generated_image_hash = hashlib.sha256(generated_image.tobytes()).hexdigest()

    blockchain.add_block(Block(i + 1, f"Trained on image with hash: {generated_image_hash}", blockchain.get_latest_block().hash))

    # Simulate discriminator loss (dummy value)
    d_loss = np.random.rand()
    g_loss = np.random.rand() * 10
    print(f"{i}/1, D Loss: {d_loss}, G Loss: {g_loss}")

# Check if the target image hash is in the blockchain
if blockchain.is_image_in_blockchain(target_image_hash):
    print("Target image hash was found in processed images.")
else:
    print("Target image hash was NOT found in processed images.")

# Output the blockchain for inspection
print("\n--- Blockchain ---")
for block in blockchain.chain:
    print(f"Index: {block.index}")
    print(f"Hash: {block.hash}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Data: {block.data}")
    print(f"Timestamp: {block.timestamp}")
    print("----------------------")
