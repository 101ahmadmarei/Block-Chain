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

        self.lblStudentID = QLabel("Student ID")
        self.submitLayout.addWidget(self.lblStudentID)
        self.txtStudentID = QLineEdit()
        self.submitLayout.addWidget(self.txtStudentID)

        self.lblStudentName = QLabel("Student Name")
        self.submitLayout.addWidget(self.lblStudentName)
        self.txtStudentName = QLineEdit()
        self.submitLayout.addWidget(self.txtStudentName)

        self.lblClassID = QLabel("Class ID")
        self.submitLayout.addWidget(self.lblClassID)
        self.txtClassID = QLineEdit()
        self.submitLayout.addWidget(self.txtClassID)

        self.lblClassName = QLabel("Class Name")
        self.submitLayout.addWidget(self.lblClassName)
        self.txtClassName = QLineEdit()
        self.submitLayout.addWidget(self.txtClassName)

        self.lblGrade = QLabel("Grade")
        self.submitLayout.addWidget(self.lblGrade)
        self.txtGrade = QLineEdit()
        self.submitLayout.addWidget(self.txtGrade)

        self.lblAbsences = QLabel("Absences")
        self.submitLayout.addWidget(self.lblAbsences)
        self.txtAbsences = QLineEdit()
        self.submitLayout.addWidget(self.txtAbsences)

        self.lblCredits = QLabel("Credits")
        self.submitLayout.addWidget(self.lblCredits)
        self.txtCredits = QLineEdit()
        self.submitLayout.addWidget(self.txtCredits)

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

        self.lblStudentID = QLabel("Student ID")
        self.requestLayout.addWidget(self.lblStudentID)
        self.txtSID = QLineEdit()
        self.requestLayout.addWidget(self.txtStudentID)

        self.lblStudentName = QLabel("Student Name")
        self.requestLayout.addWidget(self.lblStudentName)
        self.txtStudentName = QLineEdit()
        self.requestLayout.addWidget(self.txtStudentName)

        self.lblClassID = QLabel("Class ID")
        self.requestLayout.addWidget(self.lblClassID)
        self.txtClassID = QLineEdit()
        self.requestLayout.addWidget(self.txtClassID)

        self.lblClassName = QLabel("Class Name")
        self.requestLayout.addWidget(self.lblClassName)
        self.txtClassName = QLineEdit()
        self.requestLayout.addWidget(self.txtClassName)

        self.lblGrade = QLabel("Grade")
        self.requestLayout.addWidget(self.lblGrade)
        self.txtGrade = QLineEdit()
        self.requestLayout.addWidget(self.txtGrade)

        self.lblAbsences = QLabel("Absences")
        self.requestLayout.addWidget(self.lblAbsences)
        self.txtAbsences = QLineEdit()
        self.requestLayout.addWidget(self.txtAbsences)

        self.lblCredits = QLabel("Credits")
        self.requestLayout.addWidget(self.lblCredits)
        self.txtCredits = QLineEdit()
        self.requestLayout.addWidget(self.txtCredits)


        # Info tab
        self.infoLayout = QFormLayout()

        self.lblStudentID = QLabel("Student ID")
        self.infoLayout.addWidget(self.lblStudentID)
        self.txtStudentID = QLineEdit()
        self.infoLayout.addWidget(self.txtStudentID)

        self.lblStudentName = QLabel("Student Name")
        self.infoLayout.addWidget(self.lblStudentName)
        self.txtStudentName = QLineEdit()
        self.infoLayout.addWidget(self.txtStudentName)

        self.lblClassID = QLabel("Class ID")
        self.infoLayout.addWidget(self.lblClassID)
        self.txtClassID = QLineEdit()
        self.infoLayout.addWidget(self.txtClassID)

        self.lblClassName = QLabel("Class Name")
        self.infoLayout.addWidget(self.lblClassName)
        self.txtClassName = QLineEdit()
        self.infoLayout.addWidget(self.txtClassName)

        self.lblGrade = QLabel("Grade")
        self.infoLayout.addWidget(self.lblGrade)
        self.txtGrade = QLineEdit()
        self.infoLayout.addWidget(self.txtGrade)

        self.lblAbsences = QLabel("Absences")
        self.infoLayout.addWidget(self.lblAbsences)
        self.txtAbsences = QLineEdit()
        self.infoLayout.addWidget(self.txtAbsences)

        self.lblCredits = QLabel("Credits")
        self.infoLayout.addWidget(self.lblCredits)
        self.txtCredits = QLineEdit()
        self.infoLayout.addWidget(self.txtCredits)


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
