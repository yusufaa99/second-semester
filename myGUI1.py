# import sys
# from PyQt5.QtWidgets import QApplication, QWidget
# app = QApplication(sys.argv)
# gui = QWidget() # window
# gui.show()
# sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import QApplication, QPushButton

# app = QApplication(sys.argv)
# window = QPushButton("Next")  # Use straight quotes: " "
# window.show()
# sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QLabel

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("My PyQt App")
        self.setGeometry(100, 100, 300, 200)
        
        layout = QVBoxLayout()
        
        label = QLabel("Welcome to PyQt!")
        button = QPushButton("Next")
        button.clicked.connect(self.on_click)
        
        layout.addWidget(label)
        layout.addWidget(button)
        
        self.setLayout(layout)
    
    def on_click(self):
        print("Button clicked!")
        # Change button text
        self.sender().setText("Clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())