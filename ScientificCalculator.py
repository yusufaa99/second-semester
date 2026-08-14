import sys
import math
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class ScientificCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scientific Calculator")
        self.setGeometry(100, 100, 500, 720)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2d2d2d;
            }
            QPushButton {
                background-color: #3d3d3d;
                color: white;
                font-size: 14px;
                font-weight: bold;
                border: 1px solid #555;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #4d4d4d;
                border: 1px solid #777;
            }
            QPushButton:pressed {
                background-color: #5d5d5d;
            }
            QPushButton#operator {
                background-color: #f39c12;
                color: white;
            }
            QPushButton#operator:hover {
                background-color: #e67e22;
            }
            QPushButton#function {
                background-color: #2980b9;
                color: white;
            }
            QPushButton#function:hover {
                background-color: #2471a3;
            }
            QPushButton#clear {
                background-color: #e74c3c;
                color: white;
            }
            QPushButton#clear:hover {
                background-color: #c0392b;
            }
            QPushButton#equals_bar {
                background-color: #27ae60;
                color: white;
                font-size: 24px;
                font-weight: bold;
                min-height: 50px;
                border-radius: 8px;
            }
            QPushButton#equals_bar:hover {
                background-color: #229954;
            }
            QPushButton#trig {
                background-color: #8e44ad;
                color: white;
            }
            QPushButton#trig:hover {
                background-color: #7d3c98;
            }
            QLineEdit#display {
                background-color: #1a1a1a;
                color: #00ff00;
                font-size: 28px;
                font-weight: bold;
                border: 2px solid #555;
                border-radius: 5px;
                padding: 15px;
                font-family: 'Courier New', monospace;
                min-height: 60px;
            }
        """)
        
        self.expression = ""
        self.is_radian = True
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(10)
        
        # Title with ID at top
        title_layout = QHBoxLayout()
        title = QLabel("🧮 Scientific Calculator")
        title.setFont(QFont("Arial", 16, QFont.Bold))
        title.setStyleSheet("color: #00ff00; padding: 5px;")
        title_layout.addWidget(title)
        
        id_label = QLabel("U24CO2021")
        id_label.setFont(QFont("Arial", 12, QFont.Bold))
        id_label.setStyleSheet("color: #f39c12; padding: 5px; background-color: #1a1a1a; border-radius: 5px;")
        id_label.setAlignment(Qt.AlignRight)
        title_layout.addWidget(id_label)
        main_layout.addLayout(title_layout)
        
        # EQUALS BAR at the top (the "=" button)
        self.equals_bar = QPushButton("=")
        self.equals_bar.setObjectName("equals_bar")
        self.equals_bar.clicked.connect(self.calculate)
        main_layout.addWidget(self.equals_bar)
        
        # Mode selection
        mode_layout = QHBoxLayout()
        mode_label = QLabel("Angle Mode:")
        mode_label.setStyleSheet("color: white; font-size: 12px;")
        mode_layout.addWidget(mode_label)
        
        self.radian_btn = QPushButton("RAD")
        self.radian_btn.setStyleSheet("background-color: #27ae60; color: white; font-size: 12px; padding: 5px;")
        self.radian_btn.clicked.connect(lambda: self.set_mode(True))
        
        self.degree_btn = QPushButton("DEG")
        self.degree_btn.setStyleSheet("background-color: #555; color: white; font-size: 12px; padding: 5px;")
        self.degree_btn.clicked.connect(lambda: self.set_mode(False))
        
        mode_layout.addWidget(self.radian_btn)
        mode_layout.addWidget(self.degree_btn)
        mode_layout.addStretch()
        main_layout.addLayout(mode_layout)
        
        # Memory display
        self.memory_label = QLabel("Memory: 0")
        self.memory_label.setStyleSheet("color: #888; font-size: 10px;")
        self.memory_label.setAlignment(Qt.AlignRight)
        main_layout.addWidget(self.memory_label)
        
        # Button grid
        grid_layout = QGridLayout()
        grid_layout.setSpacing(5)
        
        # Row 1: Scientific functions
        buttons_row1 = [
            ("sin", "trig"), ("cos", "trig"), ("tan", "trig"),
            ("sec", "trig"), ("csc", "trig"), ("cot", "trig")
        ]
        for i, (text, btn_type) in enumerate(buttons_row1):
            btn = QPushButton(text)
            btn.setObjectName(btn_type)
            btn.clicked.connect(lambda checked, t=text: self.trig_function(t))
            grid_layout.addWidget(btn, 0, i, 1, 1)
        
        # Row 2: More functions
        buttons_row2 = [
            ("log", "function"), ("ln", "function"), ("√", "function"),
            ("x²", "function"), ("x³", "function"), ("1/x", "function")
        ]
        for i, (text, btn_type) in enumerate(buttons_row2):
            btn = QPushButton(text)
            btn.setObjectName(btn_type)
            btn.clicked.connect(lambda checked, t=text: self.function_button(t))
            grid_layout.addWidget(btn, 1, i, 1, 1)
        
        # Row 3: Memory and parentheses
        buttons_row3 = [
            ("MC", "function"), ("MR", "function"), ("M+", "function"),
            ("(", "operator"), (")", "operator"), ("π", "function")
        ]
        for i, (text, btn_type) in enumerate(buttons_row3):
            btn = QPushButton(text)
            btn.setObjectName(btn_type)
            btn.clicked.connect(lambda checked, t=text: self.special_button(t))
            grid_layout.addWidget(btn, 2, i, 1, 1)
        
        # Row 4: Standard calculator
        buttons_row4 = [
            ("C", "clear"), ("⌫", "clear"), ("%", "operator"),
            ("÷", "operator"), ("e", "function")
        ]
        for i, (text, btn_type) in enumerate(buttons_row4):
            btn = QPushButton(text)
            btn.setObjectName(btn_type)
            if text == "C":
                btn.clicked.connect(self.clear_all)
            elif text == "⌫":
                btn.clicked.connect(self.backspace)
            else:
                btn.clicked.connect(lambda checked, t=text: self.number_click(t))
            grid_layout.addWidget(btn, 3, i, 1, 1)
        
        # Row 5: Numbers 7-9
        for i, num in enumerate(["7", "8", "9"]):
            btn = QPushButton(num)
            btn.clicked.connect(lambda checked, n=num: self.number_click(n))
            grid_layout.addWidget(btn, 4, i, 1, 1)
        # Operators
        for i, op in enumerate(["×", "−", "+"]):
            btn = QPushButton(op)
            btn.setObjectName("operator")
            btn.clicked.connect(lambda checked, o=op: self.operator_click(o))
            grid_layout.addWidget(btn, 4, 3 + i, 1, 1)
        
        # Row 6: Numbers 4-6
        for i, num in enumerate(["4", "5", "6"]):
            btn = QPushButton(num)
            btn.clicked.connect(lambda checked, n=num: self.number_click(n))
            grid_layout.addWidget(btn, 5, i, 1, 1)
        # More operators
        for i, op in enumerate(["x^y", "!", "="]):
            if op == "=":
                btn = QPushButton(op)
                btn.setObjectName("equals")
                btn.clicked.connect(self.calculate)
                grid_layout.addWidget(btn, 5, 3 + i, 1, 1)
            elif op == "!":
                btn = QPushButton(op)
                btn.setObjectName("function")
                btn.clicked.connect(lambda: self.function_button("!"))
                grid_layout.addWidget(btn, 5, 3 + i, 1, 1)
            else:
                btn = QPushButton(op)
                btn.setObjectName("function")
                btn.clicked.connect(lambda checked, o="**": self.operator_click(o))
                grid_layout.addWidget(btn, 5, 3 + i, 1, 1)
        
        # Row 7: Numbers 1-3
        for i, num in enumerate(["1", "2", "3"]):
            btn = QPushButton(num)
            btn.clicked.connect(lambda checked, n=num: self.number_click(n))
            grid_layout.addWidget(btn, 6, i, 1, 1)
        # Empty cells
        for i in range(3):
            btn = QPushButton("")
            btn.setEnabled(False)
            btn.setStyleSheet("background-color: transparent; border: none;")
            grid_layout.addWidget(btn, 6, 3 + i, 1, 1)
        
        # Row 8: 0, ., ±
        btn0 = QPushButton("0")
        btn0.clicked.connect(lambda: self.number_click("0"))
        grid_layout.addWidget(btn0, 7, 0, 1, 3)
        
        btn_dot = QPushButton(".")
        btn_dot.clicked.connect(lambda: self.number_click("."))
        grid_layout.addWidget(btn_dot, 7, 3, 1, 1)
        
        btn_plusminus = QPushButton("±")
        btn_plusminus.setObjectName("operator")
        btn_plusminus.clicked.connect(self.toggle_sign)
        grid_layout.addWidget(btn_plusminus, 7, 4, 1, 1)
        
        main_layout.addLayout(grid_layout)
        
        # DISPLAY at the very bottom
        self.display = QLineEdit()
        self.display.setObjectName("display")
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setText("0")
        main_layout.addWidget(self.display)
        
        # Status bar
        self.statusBar().showMessage("Ready")
        self.statusBar().setStyleSheet("background-color: #1a1a1a; color: #888;")
        
        self.memory = 0
    
    def set_mode(self, is_radian):
        self.is_radian = is_radian
        if is_radian:
            self.radian_btn.setStyleSheet("background-color: #27ae60; color: white; font-size: 12px; padding: 5px;")
            self.degree_btn.setStyleSheet("background-color: #555; color: white; font-size: 12px; padding: 5px;")
            self.statusBar().showMessage("Mode: Radians")
        else:
            self.radian_btn.setStyleSheet("background-color: #555; color: white; font-size: 12px; padding: 5px;")
            self.degree_btn.setStyleSheet("background-color: #27ae60; color: white; font-size: 12px; padding: 5px;")
            self.statusBar().showMessage("Mode: Degrees")
    
    def number_click(self, value):
        current = self.display.text()
        if current == "0" and value != ".":
            self.display.setText(value)
        else:
            self.display.setText(current + value)
        self.statusBar().showMessage(f"Entered: {value}")
    
    def operator_click(self, operator):
        current = self.display.text()
        self.expression = current + " " + operator + " "
        self.display.setText(self.expression)
        self.statusBar().showMessage(f"Operator: {operator}")
    
    def function_button(self, func):
        current = self.display.text()
        try:
            # Clean the input to get only the number
            clean_current = current.strip()
            import re
            numbers = re.findall(r'-?\d+\.?\d*', clean_current)
            if numbers:
                value = float(numbers[-1])
            else:
                value = float(clean_current)
            
            result = 0
            if func == "√":
                if value >= 0:
                    result = math.sqrt(value)
                else:
                    QMessageBox.warning(self, "Error", "Cannot take square root of negative number!")
                    return
            elif func == "x²":
                result = value ** 2
            elif func == "x³":
                result = value ** 3
            elif func == "1/x":
                if value != 0:
                    result = 1 / value
                else:
                    QMessageBox.warning(self, "Error", "Cannot divide by zero!")
                    return
            elif func == "log":
                if value > 0:
                    result = math.log10(value)
                else:
                    QMessageBox.warning(self, "Error", "Logarithm requires positive number!")
                    return
            elif func == "ln":
                if value > 0:
                    result = math.log(value)
                else:
                    QMessageBox.warning(self, "Error", "Natural logarithm requires positive number!")
                    return
            elif func == "!":
                if value >= 0 and value.is_integer():
                    result = math.factorial(int(value))
                else:
                    QMessageBox.warning(self, "Error", "Factorial requires non-negative integer!")
                    return
            self.display.setText(str(result))
            self.statusBar().showMessage(f"{func}({value}) = {result}")
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid input!")
    
    def trig_function(self, func):
        current = self.display.text()
        try:
            # Clean the input to get only the number
            clean_current = current.strip()
            import re
            numbers = re.findall(r'-?\d+\.?\d*', clean_current)
            if numbers:
                value = float(numbers[-1])
            else:
                value = float(clean_current)
            
            # Convert to radians if in degree mode
            if not self.is_radian:
                value = math.radians(value)
            
            result = 0
            if func == "sin":
                result = math.sin(value)
            elif func == "cos":
                result = math.cos(value)
            elif func == "tan":
                if math.cos(value) != 0:
                    result = math.tan(value)
                else:
                    QMessageBox.warning(self, "Error", "Tan undefined for this angle!")
                    return
            elif func == "sec":
                cos_val = math.cos(value)
                if cos_val != 0:
                    result = 1 / cos_val
                else:
                    QMessageBox.warning(self, "Error", "Sec undefined for this angle!")
                    return
            elif func == "csc":
                sin_val = math.sin(value)
                if sin_val != 0:
                    result = 1 / sin_val
                else:
                    QMessageBox.warning(self, "Error", "Csc undefined for this angle!")
                    return
            elif func == "cot":
                tan_val = math.tan(value)
                if tan_val != 0:
                    result = 1 / tan_val
                else:
                    QMessageBox.warning(self, "Error", "Cot undefined for this angle!")
                    return
            self.display.setText(str(result))
            self.statusBar().showMessage(f"{func}({current}) = {result}")
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid input!")
    
    def special_button(self, button):
        if button == "π":
            self.display.setText(str(math.pi))
            self.statusBar().showMessage("π = 3.141592653589793")
        elif button == "(":
            current = self.display.text()
            self.display.setText(current + "(")
        elif button == ")":
            current = self.display.text()
            self.display.setText(current + ")")
        elif button == "MC":
            self.memory = 0
            self.memory_label.setText("Memory: 0")
            self.statusBar().showMessage("Memory cleared")
        elif button == "MR":
            self.display.setText(str(self.memory))
            self.statusBar().showMessage(f"Memory recalled: {self.memory}")
        elif button == "M+":
            try:
                value = float(self.display.text())
                self.memory += value
                self.memory_label.setText(f"Memory: {self.memory}")
                self.statusBar().showMessage(f"Added to memory: {value}")
            except ValueError:
                QMessageBox.warning(self, "Error", "Invalid input!")
    
    def toggle_sign(self):
        current = self.display.text()
        if current and current != "0":
            if current.startswith("-"):
                self.display.setText(current[1:])
            else:
                self.display.setText("-" + current)
    
    def clear_all(self):
        self.display.setText("0")
        self.expression = ""
        self.statusBar().showMessage("Cleared all")
    
    def backspace(self):
        current = self.display.text()
        if len(current) > 1:
            self.display.setText(current[:-1])
        else:
            self.display.setText("0")
        self.statusBar().showMessage("Backspace")
    
    def calculate(self):
        try:
            # Get the expression from display
            expr = self.display.text()
            # Replace display symbols with Python equivalents
            expr = expr.replace("×", "*")
            expr = expr.replace("÷", "/")
            expr = expr.replace("−", "-")
            expr = expr.replace("x^y", "**")
            
            # Handle exponentiation
            if "**" in expr:
                parts = expr.split("**")
                if len(parts) == 2:
                    base = float(parts[0].strip())
                    exp = float(parts[1].strip())
                    result = base ** exp
                    self.display.setText(str(result))
                    self.statusBar().showMessage(f"Result: {result}")
                    return
            
            # Evaluate expression
            result = eval(expr)
            self.display.setText(str(result))
            self.statusBar().showMessage(f"Result: {result}")
        except ZeroDivisionError:
            QMessageBox.warning(self, "Error", "Cannot divide by zero!")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Invalid expression: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    calculator = ScientificCalculator()
    calculator.show()
    sys.exit(app.exec_())