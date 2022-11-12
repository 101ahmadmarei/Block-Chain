from Blockchain import Blockchain
from Block import Block

# Create a new blockchain
bc = Blockchain() 
 
b1 = Block(0, 0, "lol", 1, "Mar", "Ahmad Marei", "COMP3800", "bc", 95, 3, 4) 

b2 = Block(0, 0, "test", 1, "eth", "Faris Ali", "COMP2222", "computer", 66, 1, 4)      

def valid_chain(bc):
    for i in range(1, bc.get_length()):
        if bc.get_block(i).prevHash != bc.get_block(i-1).currHash:
            return False
    return True


print(bc.get_block(0))
bc.add_block(b1)
print(bc.get_block(1))
bc.add_block(b2)
print(bc.get_block(2))

print()
# print(bc)
print(valid_chain(bc))
