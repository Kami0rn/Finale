from blockchain import add_block_to_chain, check_image_in_blockchain

import hashlib
from PIL import Image

def hash_image(image_data):
    # Check if the input is a path or raw bytes
    if isinstance(image_data, str):
        # If it's a file path, read the file
        with open(image_data, "rb") as f:
            image_bytes = f.read()
    else:
        # If it's raw bytes, use them directly
        image_bytes = image_data
    
    # Return the hash of the image data
    return hashlib.sha256(image_bytes).hexdigest()


# Example usage
if __name__ == "__main__":
    image_hash = hash_image("path/to/image.png")
    print(f"Image Hash: {image_hash}")

    # Add the image hash to the blockchain data
    add_block_to_chain(f"Trained on image with hash: {image_hash}")

    # Example traceability check
    user_image_hash = hash_image("path/to/user_image.png")
    block_index = check_image_in_blockchain(user_image_hash)

    if block_index is not None:
        print(f"Image was used in training, found in block {block_index}")
    else:
        print("Image not found in training data")
