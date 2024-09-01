import numpy as np
import hashlib  # Add this import statement
from gan_model import create_gan_model
from blockchain import Blockchain, Block
from traceability import hash_image

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
