import sys
import signal
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QDesktopWidget, QLineEdit, QFormLayout, QLabel, QPushButton, QTabWidget

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
            print("Button clicked, Hello!")                                                                    
                                                                                                                                                                           
# Create a button, connect it and show it                                                           
        button = QPushButton("Submit data to chain")                                                                    
        button.clicked.connect(say_hello)
        self.submitLayout.addWidget(button)

        submit = QWidget()
        submit.setLayout(self.submitLayout)

        # Request tab
        self.requestLayout = QFormLayout()

        self.lblTest = QLabel("ethan")
        self.requestLayout.addWidget(self.lblTest)

        request = QWidget()
        request.setLayout(self.requestLayout)

        # Info tab
        self.infoLayout = QFormLayout()

        self.lblTest2 = QLabel("Test2")
        self.infoLayout.addWidget(self.lblTest2)

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
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
