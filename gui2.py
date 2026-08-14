import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QPushButton, QAction, QMainWindow

class Gui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui()

        def ui(self):
            self.setWindowTitle("GUI Window")
            self.setFixedSize(800, 400)
            self.add_widgets()