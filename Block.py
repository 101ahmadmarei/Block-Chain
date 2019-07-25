from hashlib import sha256
import time


class Block:
    def __init__(self, timestamp, prevHash, data, nonce, difficulty, student_id, student_name, class_id, class_name, grade, absences, credits):
        self.height = 0
        self.timestamp = timestamp
        self.prevHash = prevHash
        self.currHash = 0
        self.data = data
        self.nonce = nonce
        self.difficulty = difficulty
        self.student_id=student_id
        self.student_name=student_name
        self.class_id=class_id
        self.class_name=class_name
        self.grade=grade
        self.absences=absences
        self.credits=credits

    def __repr__(self):
        return 'Block< height:{}, timestamp:{}, prevHash:{}, currHash:{}, data:{}, nonce:{}, difficulty:{}, student_id:{}, student_name:{}, class_id:{}, class_name:{}, grade:{}, absences:{}, credits:{} >'.format(self.height, self.timestamp, self.prevHash, self.currHash, self.data, self.nonce, self.difficulty, self.student_id, self.student_name, self.class_id, self.class_name, self.grade, self.absences, self.credits)

    @staticmethod
    def genesis():
        return Block(0, 0, "genesis", 0, 1, 0, "None", "COMP0000", "None", 0, 0, 0)

    @staticmethod
    def mine(block, last_block):
        #block.currHash = sha256(str(block).encode()).hexdigest()
        difficulty=last_block.difficulty
        block.height=last_block.height+1
        while True:
            block.nonce=block.nonce+1
            block.timestamp=int(time.time())
            tmp_hash=sha256(str(block).encode()).hexdigest()
            if tmp_hash[0:1] == '0':
                break
        block.currHash = tmp_hash
        return block

