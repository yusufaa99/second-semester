import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont, QPixmap
# import for alignment
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # adding properties of the mainwindow
        self.setWindowTitle("Gui 3 Application")
        self.setGeometry(500,250,500,300)
        self.setWindowIcon(QIcon("Anonymous.png"))

        #  styling a label
        label = QLabel("Hello, PyQt5 Devs", self)
        label.setFont(QFont("Arial", 30))
        label.setGeometry(0,0,0,0)
        label.setStyleSheet("color: blue;"
                            "background-color: black;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline")

        # label.setAlignment(Qt.AlignTop)
        # label.setAlignment(Qt.AlignBottom)
        # label.setAlignment(Qt.AlignCenter)
        label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        # adding image to a label
        label2 = QLabel(self)
        label2.setGeometry(0,0, 300, 200)
        # a simple trick to position the image at the center of the window
        label2.setGeometry((self.width()-label2.width())//2, 
                           (self.height()-label2.height())//2, 
                           label2.width(), 
                           label2.height())
        pixmap = QPixmap("Anonymous.png")
        label2.setPixmap(pixmap)
        label2.setScaledContents(True)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()