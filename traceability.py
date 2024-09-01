import hashlib
from PIL import Image
import numpy as np

def hash_image(image_path):
    with Image.open(image_path) as img:
        img = img.convert("RGB")
        img_array = np.array(img)
        img_bytes = img_array.tobytes()
        hash_object = hashlib.sha256(img_bytes)
        return hash_object.hexdigest()
