import sys
import math
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt, pyqtSignal, QObject
from pynput import keyboard

safe_dict = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}

def calculate(expression):
    expr = expression.replace("^", "**")
    
    try:
        result = eval(expr, {"__builtins__": {}}, safe_dict)
        return str(result)
    except Exception:
        return "Error"

class SignalBridge(QObject):
    toggle_signal = pyqtSignal()

class CalculatorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        self.setStyleSheet("""
            #MainContainer {
                background-color: #2d2d2d;
                border: 2px solid #555555;
                border-radius: 10px;
            }
            QLineEdit {
                background-color: transparent;
                color: white;
                padding: 10px;
                font-family: 'Segoe UI', Arial;
                font-size: 12pt;
                border: none;
            }
        """)

        screen = QApplication.primaryScreen().geometry()
        self.setGeometry(screen.width()//2 - 125, 100, 250, 56)

        self.central_widget = QWidget()
        self.central_widget.setObjectName("MainContainer")
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setContentsMargins(5, 5, 5, 5)

        self.entry = QLineEdit()
        self.entry.setPlaceholderText("Type math and press Enter...")
        self.entry.returnPressed.connect(self.on_enter)
        self.layout.addWidget(self.entry)

    def on_enter(self):
        expr = self.entry.text()
        if expr.strip():
            result = calculate(expr)
            self.entry.setText(result)
            self.entry.selectAll()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.hide()

    def toggle_visibility(self):
        if self.isVisible():
            self.hide()
        else:
            self.show()
            self.raise_()
            self.activateWindow()
            self.entry.setFocus()
            self.entry.selectAll()

app = QApplication(sys.argv)

window = CalculatorWindow()
bridge = SignalBridge()

bridge.toggle_signal.connect(window.toggle_visibility)

def trigger_signal():
    bridge.toggle_signal.emit()

hotkey_listener = keyboard.GlobalHotKeys({"<alt>+<ctrl>": trigger_signal})
hotkey_listener.start()

app.exec()