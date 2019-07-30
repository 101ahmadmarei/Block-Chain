import sys
import signal
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QDesktopWidget, QLineEdit, QFormLayout, QLabel, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AcademicChain")
        self.resize(640, 480)

        self.layout = QFormLayout()

        self.lblStudentID = QLabel("Student ID")
        self.layout.addWidget(self.lblStudentID)
        self.txtStudentID = QLineEdit()
        self.layout.addWidget(self.txtStudentID)

        self.lblStudentName = QLabel("Student Name")
        self.layout.addWidget(self.lblStudentName)
        self.txtStudentName = QLineEdit()
        self.layout.addWidget(self.txtStudentName)

        self.lblClassID = QLabel("Class ID")
        self.layout.addWidget(self.lblClassID)
        self.txtClassID = QLineEdit()
        self.layout.addWidget(self.txtClassID)

        self.lblGrade = QLabel("Grade")
        self.layout.addWidget(self.lblGrade)
        self.txtGrade = QLineEdit()
        self.layout.addWidget(self.txtGrade)

        self.lblAbsences = QLabel("Absences")
        self.layout.addWidget(self.lblAbsences)
        self.txtAbsences = QLineEdit()
        self.layout.addWidget(self.txtAbsences)

        self.lblCredits = QLabel("Credits")
        self.layout.addWidget(self.lblCredits)
        self.txtCredits = QLineEdit()
        self.layout.addWidget(self.txtCredits)


        def say_hello():                                                                                     
            print("Button clicked, Hello!")                                                                    
                                                                                                                                                                           
# Create a button, connect it and show it                                                           
        button = QPushButton("Submit data to chain")                                                                    
        button.clicked.connect(say_hello)
        self.layout.addWidget(button)

        

        central = QWidget()
        central.setLayout(self.layout)
        self.setCentralWidget(central)

        self.show()

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
