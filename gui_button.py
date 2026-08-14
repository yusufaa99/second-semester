import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QGridLayout

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        # self.setGeometry(0,0,500, 300)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.setGeometry(600, 300, 500, 350)
        self.label = QLabel("label")
        self.label.setStyleSheet("font: 30px")
        self.button = QPushButton("Click Me!", self)
        self.button.setFixedSize(150, 50)
        self.button.setStyleSheet("font: 30px;"
                                  "background-color: green")
        self.button.clicked.connect(self.on_cliked)

        grid = QGridLayout()
        
        grid.addWidget(self.button, 0, 0, 1, 1)  # Button in column 0
        grid.addWidget(self.label, 0, 1, 1, 1)   # Label in column 1
        

        central_widget.setLayout(grid)

    def on_cliked(self):
        print("Button is Clicked")
        self.button.setText("Clicked")
        self.button.setStyleSheet("font: 35px;" 
                                  "background-color: red;")
        self.label.setText("Button is clicked")
        self.label.setStyleSheet("font: 35px;" 
                                 "color: red;")

        self.button.setDisabled(True)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()