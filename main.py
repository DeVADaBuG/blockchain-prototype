import hashlib
import time

class Block:
    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.timestamp = time.time()
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return hashlib.sha256(f"{self.data}{self.previous_hash}{self.timestamp}".encode()).hexdigest()

print("Genesis block linked.")
