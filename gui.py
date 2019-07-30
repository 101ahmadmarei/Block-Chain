import sys
import signal
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QDesktopWidget, QLineEdit, QFormLayout, QLabel

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

        central = QWidget()
        central.setLayout(self.layout)
        self.setCentralWidget(central)

        self.show()

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
