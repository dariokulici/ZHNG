from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QFrame, QGroupBox

class Printers(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

class PrinterMenu(QFrame):
    def __init__(self):
        super().__init__()
        self.setFrameShape(QFrame.Shape.Box)
        self.setLineWidth(1)
        layout = QVBoxLayout(self)

        group = QLabel("Drucker")
        group.setStyleSheet("font-size: 18px")

        layout.addWidget(group)
        layout.addWidget(Printers())