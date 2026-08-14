import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QLabel, QButtonGroup, QWidget, QHBoxLayout, QGridLayout


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.setWindowTitle("Gender Selector")
        self.setGeometry(500, 250, 500, 400)

        self.label = QLabel("Gender")
        self.male = QRadioButton("Male")
        self.female = QRadioButton("FeMale")

        grid = QGridLayout()
        central_widget.setLayout(grid)
        
        self.label.setStyleSheet("font: 20px;"
                                 "padding: 0px")
        grid.addWidget(self.label, 0,0,1,1)
        grid.addWidget(self.male, 1,0,1,1)
        grid.addWidget(self.female, 2,0,1,1)

        # self.QRadioButton().set

        def radio_button(self):
            print("selected !")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()