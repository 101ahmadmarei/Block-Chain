

class Blockchain:
    def __init__(self):
        self.chain = []
        self.genesis()

    def genesis(self):
        b = Block()
        b.hash = b.hash_block()
        self.chain.append(b)

    @property
    def last_block(self):
        return self.chain[-1]

    def add_block(self, block):
        prevHash = self.last_block.hash
        self.chain.append(block)
