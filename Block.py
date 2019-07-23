from hashlib import sha256

class Block:
    def __init__(self, timestamp, prevHash, currHash, data, nonce, difficulty):
        self.timestamp = timestamp
        self.prevHash = prevHash
#        self.currHash = self.hash_block()
        self.data = data
        self.nonce = nonce
        self.difficulty = difficulty

#        return this
    def out(self):
        print(self.timestamp, self.prevHash, self.data, self.nonce, self.difficulty)

#    def hash_block(self):
#        return sha256(this).hexdigest()
