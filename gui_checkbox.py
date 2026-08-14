import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QWidget, QCheckBox, QGridLayout, QGroupBox, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set window properties
        self.setWindowTitle("Programming Language Selector")
        self.setGeometry(500, 250, 500, 400)
        self.setStyleSheet("background-color: #f5f5f5;")
        
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Create main layout
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        # Create a group box for better organization
        group_box = QGroupBox("Programming Language Preferences")
        group_box.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 2px solid #cccccc;
                border-radius: 8px;
                margin-top: 10px;
                padding-top: 10px;
                font-size: 14px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
            }
        """)
        
        # Create grid layout inside group box
        grid = QGridLayout()
        group_box.setLayout(grid)
        
        # Title label with professional styling
        self.label = QLabel("Select Your Preferred Programming Language")
        self.label.setFont(QFont("Arial", 14, QFont.Bold))
        self.label.setStyleSheet("color: #2c3e50; padding: 5px;")
        self.label.setAlignment(Qt.AlignCenter)
        grid.addWidget(self.label, 0, 0, 1, 3)
        
        # Name label and text field - Using QLineEdit instead of QTextEdit
        self.label2 = QLabel("Name:")
        self.label2.setFont(QFont("Arial", 11))
        self.label2.setStyleSheet("color: #34495e;")
        grid.addWidget(self.label2, 1, 0, 1, 1)
        
        # QLineEdit is better for single-line text like names
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter your full name")
        self.name_input.setStyleSheet("""
            QLineEdit {
                border: 2px solid #bdc3c7;
                border-radius: 5px;
                padding: 8px;
                background-color: white;
                font-size: 12px;
            }
            QLineEdit:focus {
                border: 2px solid #3498db;
                background-color: #f7fbff;
            }
            QLineEdit:hover {
                border: 2px solid #95a5a6;
            }
        """)
        grid.addWidget(self.name_input, 1, 1, 1, 2)
        
        # Create checkboxes with consistent styling
        checkboxes = [
            ("Python", "Python"),
            ("Java", "Java"),
            ("C/C++", "C/C++"),
            ("JavaScript", "JavaScript"),
            ("C#", "C#"),
            ("Go Lang", "Go Lang"),
            ("PHP", "PHP")
        ]
        
        self.checkboxes = []
        row = 2
        col = 0
        
        for text, lang in checkboxes:
            checkbox = QCheckBox(text)
            checkbox.setStyleSheet("""
                QCheckBox {
                    font-size: 12px;
                    padding: 5px;
                    color: #2c3e50;
                }
                QCheckBox::indicator {
                    width: 18px;
                    height: 18px;
                }
                QCheckBox::indicator:unchecked {
                    border: 2px solid #bdc3c7;
                    border-radius: 4px;
                    background-color: white;
                }
                QCheckBox::indicator:checked {
                    border: 2px solid #27ae60;
                    border-radius: 4px;
                    background-color: #27ae60;
                }
                QCheckBox::indicator:hover {
                    border: 2px solid #3498db;
                }
            """)
            checkbox.setProperty("language", lang)
            checkbox.stateChanged.connect(self.checkStateChange)
            self.checkboxes.append(checkbox)
            grid.addWidget(checkbox, row, col, 1, 1)
            
            col += 1
            if col > 1:
                col = 0
                row += 1
        
        main_layout.addWidget(group_box)
        main_layout.addStretch()
        
        self.statusBar().showMessage("Ready - Select your preferred programming language")
        self.statusBar().setStyleSheet("background-color: #ecf0f1; color: #2c3e50;")
    
    def checkStateChange(self, state):
        checkbox = self.sender()
        language = checkbox.property("language")
        
        if state == Qt.Unchecked:
            print(f"{language} checkbox unchecked")
            self.statusBar().showMessage(f"Deselected: {language}")
        else:
            print(f"{language} checkbox checked")
            self.statusBar().showMessage(f"Selected: {language}")
            
        selected = [cb.text() for cb in self.checkboxes if cb.isChecked()]
        if selected:
            print(f"Currently selected: {', '.join(selected)}")
    
    def keyPressEvent(self, event):
        # Press Enter to submit
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            name = self.name_input.text().strip()
            if name:
                selected = [cb.text() for cb in self.checkboxes if cb.isChecked()]
                if selected:
                    print(f"\n=== Submission ===")
                    print(f"Name: {name}")
                    print(f"Selected Languages: {', '.join(selected)}")
                    print("===================\n")
                    self.statusBar().showMessage(f"Submitted: {name} - {', '.join(selected)}")
                    QMessageBox.information(self, "Submission", 
                        f"Name: {name}\nLanguages: {', '.join(selected)}")
                else:
                    self.statusBar().showMessage("Please select at least one language")
            else:
                self.statusBar().showMessage("Please enter your name")

def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()