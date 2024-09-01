import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

def calculate_hash(index, previous_hash, timestamp, data):
    value = str(index) + previous_hash + str(timestamp) + data
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

def create_genesis_block():
    return Block(0, "0", int(time.time()), "Genesis Block", calculate_hash(0, "0", int(time.time()), "Genesis Block"))

def create_new_block(previous_block, data):
    index = previous_block.index + 1
    timestamp = int(time.time())
    hash = calculate_hash(index, previous_block.hash, timestamp, data)
    return Block(index, previous_block.hash, timestamp, data, hash)

# Create blockchain and add genesis block
blockchain_chain = [create_genesis_block()]
previous_block = blockchain_chain[0]

# Example of adding a new block after every 100 images
def add_block_to_chain(data):
    global previous_block
    new_block = create_new_block(previous_block, data)
    blockchain_chain.append(new_block)
    previous_block = new_block
    print(f"Block {new_block.index} has been added with hash: {new_block.hash}")

# Function to check if an image is in the blockchain
def check_image_in_blockchain(image_hash):
    for block in blockchain_chain:
        if image_hash in block.data:
            return block.index
    return None

# Display the blockchain
for block in blockchain_chain:
    print(f"Index: {block.index}, Hash: {block.hash}, Previous Hash: {block.previous_hash}, Data: {block.data}")
