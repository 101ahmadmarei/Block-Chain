import sys
import signal
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QDesktopWidget, QGridLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AcademicChain")
        self.resize(640, 480)

        self.grid_layout = QGridLayout()
        central_widget = QWidget()
        central_widget.setLayout(self.grid_layout)
        self.setCentralWidget(central_widget)

        self.show()

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
