import sys
import signal
import time
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QDesktopWidget, QLineEdit, QFormLayout, QLabel, QPushButton, QTabWidget
from Block import Block
from Blockchain import Blockchain


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AcademicChain")
        self.resize(640, 480)

        # Submit tab
        self.submitLayout = QFormLayout()

        self.slblStudentID = QLabel("Student ID")
        self.submitLayout.addWidget(self.slblStudentID)
        self.stxtStudentID = QLineEdit()
        self.submitLayout.addWidget(self.stxtStudentID)

        self.slblStudentName = QLabel("Student Name")
        self.submitLayout.addWidget(self.slblStudentName)
        self.stxtStudentName = QLineEdit()
        self.submitLayout.addWidget(self.stxtStudentName)

        self.slblClassID = QLabel("Class ID")
        self.submitLayout.addWidget(self.slblClassID)
        self.stxtClassID = QLineEdit()
        self.submitLayout.addWidget(self.stxtClassID)

        self.slblClassName = QLabel("Class Name")
        self.submitLayout.addWidget(self.slblClassName)
        self.stxtClassName = QLineEdit()
        self.submitLayout.addWidget(self.stxtClassName)

        self.slblGrade = QLabel("Grade")
        self.submitLayout.addWidget(self.slblGrade)
        self.stxtGrade = QLineEdit()
        self.submitLayout.addWidget(self.stxtGrade)

        self.slblAbsences = QLabel("Absences")
        self.submitLayout.addWidget(self.slblAbsences)
        self.stxtAbsences = QLineEdit()
        self.submitLayout.addWidget(self.stxtAbsences)

        self.slblCredits = QLabel("Credits")
        self.submitLayout.addWidget(self.slblCredits)
        self.stxtCredits = QLineEdit()
        self.submitLayout.addWidget(self.stxtCredits)

        def say_hello(): 
            prevBlock = bc.get_block(0)
            height = prevBlock.height+1
            timestamp = int(time.time())
            prevHash = prevBlock.currHash
            data = "tmp data"
            #nonce
            difficulty = prevBlock.difficulty
            # Data from QLineEdits
            student_id = self.txtStudentID.text()
            student_name = self.txtStudentName.text()
            class_id = self.txtClassID.text()
            class_name = self.txtClassName.text()
            grade = int(self.txtGrade.text())
            absences = int(self.txtAbsences.text())
            credits = int(self.txtCredits.text())
            
            block = Block(timestamp,prevHash,"lol",difficulty,student_id,student_name,class_id,class_name,grade,absences,credits)
            bc.add_block(block)
            print("Block added to chain")
            print(bc)


        button = QPushButton("Submit data to chain") 
        button.clicked.connect(say_hello)
        self.submitLayout.addWidget(button)

        submit = QWidget()
        submit.setLayout(self.submitLayout)

        # Request tab
        self.requestLayout = QFormLayout()

        request = QWidget()
        request.setLayout(self.requestLayout)

        self.rlblStudentID = QLabel("Student ID")
        self.requestLayout.addWidget(self.rlblStudentID)
        self.rtxtStudentID = QLineEdit()
        self.requestLayout.addWidget(self.rtxtStudentID)

        self.rlblStudentName = QLabel("Student Name")
        self.requestLayout.addWidget(self.rlblStudentName)
        self.rtxtStudentName = QLineEdit()
        self.requestLayout.addWidget(self.rtxtStudentName)

        self.rlblClassID = QLabel("Class ID")
        self.requestLayout.addWidget(self.rlblClassID)
        self.rtxtClassID = QLineEdit()
        self.requestLayout.addWidget(self.rtxtClassID)

        self.rlblClassName = QLabel("Class Name")
        self.requestLayout.addWidget(self.rlblClassName)
        self.rtxtClassName = QLineEdit()
        self.requestLayout.addWidget(self.rtxtClassName)

        self.rlblGrade = QLabel("Grade")
        self.requestLayout.addWidget(self.rlblGrade)
        self.rtxtGrade = QLineEdit()
        self.requestLayout.addWidget(self.rtxtGrade)

        self.rlblAbsences = QLabel("Absences")
        self.requestLayout.addWidget(self.rlblAbsences)
        self.rtxtAbsences = QLineEdit()
        self.requestLayout.addWidget(self.rtxtAbsences)

        self.rlblCredits = QLabel("Credits")
        self.requestLayout.addWidget(self.rlblCredits)
        self.rtxtCredits = QLineEdit()
        self.requestLayout.addWidget(self.rtxtCredits)

        # Info tab
        self.infoLayout = QFormLayout()

        self.ilblInfo = QLabel("Statistics")
        self.infoLayout.addWidget(self.ilblInfo)

        info = QWidget()
        info.setLayout(self.infoLayout)

        # Tabs init
        self.tab = QTabWidget()
        self.tab.addTab(submit, "Submit")
        self.tab.addTab(request, "Request")
        self.tab.addTab(info, "Stats")

        self.setCentralWidget(self.tab)

        self.show()

if __name__ == '__main__':

    bc = Blockchain()

    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
