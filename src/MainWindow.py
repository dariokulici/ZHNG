from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QLabel
from PySide6.QtCore import QSize
from PrinterMenu import PrinterMenu

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lieferschein Creator")
        self.setMinimumSize(QSize(800, 600))
        self.setMaximumSize(QSize(1000, 800))

        # Main Layout
        widget = QWidget()
        layout = QHBoxLayout(widget)

        layout.addWidget(PrinterMenu())
        self.setCentralWidget(widget)