from PyQt6.QtWidgets import QApplication, QWidget
from .password_manager import PasswordManager
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setGeometry(100,100,250,250)
        self.setWindowTitle("PASSword MANager")
        self.show()

def run_qt_app():
    app = QApplication(sys.argv)
    main_window = Window()
    sys.exit(app.exec())

if __name__ == '__main__':
    run_qt_app()