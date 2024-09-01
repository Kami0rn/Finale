import hashlib
from PIL import Image
import numpy as np
import os

def hash_image(image_input):
    if isinstance(image_input, str):
        # If a file path is given, open the image and convert to array
        with Image.open(image_input) as img:
            img = img.convert("RGB")
            img_array = np.array(img)
    elif isinstance(image_input, np.ndarray):
        # If a NumPy array is given, use it directly
        img_array = image_input
    else:
        raise TypeError("Unsupported type for image input")

    # Convert the image array to bytes and then hash it
    img_bytes = img_array.tobytes()
    hash_object = hashlib.sha256(img_bytes)
    return hash_object.hexdigest()

def load_images_from_directory(directory):
    images = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        with Image.open(file_path) as img:
            img = img.convert("RGB")
            img_array = np.array(img)
            images.append(img_array)
    return images
