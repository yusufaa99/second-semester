import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QHBoxLayout, QGridLayout


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initui()

    def initui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.setGeometry(500, 250, 500, 300)
        self.setWindowTitle("Layout Window")

        label1 = QLabel("#1", self)
        label2 = QLabel("#2", self)
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)
        label5 = QLabel("#5", self)

        label1.setStyleSheet("background-color: blue;")
        label2.setStyleSheet("background-color: red;")
        label3.setStyleSheet("background-color: green;")
        label4.setStyleSheet("background-color: yellow;")
        label5.setStyleSheet("background-color: grey;")

        grid = QGridLayout()

        grid.addWidget(label1,0,0,1,2)
        grid.addWidget(label2,0,2)
        grid.addWidget(label3,1,0)
        grid.addWidget(label4,1,1,1,2)
        grid.addWidget(label5,2,0,1,3)

        central_widget.setLayout(grid)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
