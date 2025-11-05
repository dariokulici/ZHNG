from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QFrame

class PrinterMenu(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        self.eintrag = QLabel("Drucker 1")

        layout.addWidget(self.eintrag)

class BackgroundCard(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #444; border-radius: 8px;")

        layout = QVBoxLayout(self)

        self.title = QLabel("Drucker")
        text = QLabel("Text")

        layout.addWidget(text)
        layout.addWidget(self.title)
        layout.addWidget(PrinterMenu())