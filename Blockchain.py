from Block import Block

class Blockchain:
    def __init__(self):
        self.chain = []
        self.chain.append(Block.genesis())

    def get_block(self, index):
        return self.chain[index]

    def add_block(self, new_block):
        mined_block = Block.mine(new_block, self.chain[len(self.chain)-1])
        self.chain.append(mined_block)

    def __repr__(self):
        out = "Blockchain< "
        for b in range(len(self.chain)):
            out=out+repr(self.chain[b])+" "
        out=out+">"
        return out
