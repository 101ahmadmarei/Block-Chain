from Blockchain import Blockchain
from Block import Block


bc = Blockchain()
b1 = Block(0, 0, "lol", 0, 1, "smithe4", "ethan smith", "COMP3800", "bc", 95, 3, 4)
b2 = Block(0, 0, "test", 0, 1, "eth", "jeff g", "COMP2222", "computer", 66, 1, 4)

print(bc.get_block(0))
bc.add_block(b1)
print(bc.get_block(1))
bc.add_block(b2)
print(bc.get_block(2))

print()
print(bc)
