import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt, pyqtSignal, QObject
from pynput import keyboard
from logic import AppLogic

class SignalBridge(QObject):
    toggle_signal = pyqtSignal()

class CalculatorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.logic = AppLogic(self)
        self.font_size = 12
        self.colors = {
            "background": "#2d2d2d",
            "border": "#555555",
            "text": "#ffffff"
        }
        
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget()
        self.central_widget.setObjectName("MainContainer")
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setContentsMargins(5, 5, 5, 5)

        self.entry = QLineEdit()
        self.entry.setPlaceholderText("Math or /command...")
        self.entry.returnPressed.connect(self.handle_execution)
        self.layout.addWidget(self.entry)
        
        self.apply_styles()
        
        screen = QApplication.primaryScreen().geometry()
        self.setGeometry(screen.width()//2 - 125, 100, 250, 60)

    def apply_styles(self):
        self.setStyleSheet(f"""
            #MainContainer {{
                background-color: {self.colors['background']};
                border: 2px solid {self.colors['border']};
                border-radius: 10px;
            }}
            QLineEdit {{
                background-color: transparent;
                color: {self.colors['text']};
                padding: 10px;
                font-family: 'Segoe UI', Arial;
                font-size: {self.font_size}pt;
                border: none;
            }}
        """)

    def update_font_size(self, new_size):
        self.font_size = new_size
        self.apply_styles()
    
    def update_colors(self, bg=None, border=None, text=None):
        if bg: self.colors['background'] = bg
        if border: self.colors['border'] = border
        if text: self.colors['text'] = text
        self.apply_styles()

    def handle_execution(self):
        result = self.logic.process_input(self.entry.text())
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
hotkey_listener = keyboard.GlobalHotKeys({"<alt>+<ctrl>": bridge.toggle_signal.emit})
hotkey_listener.start()

app.exec()