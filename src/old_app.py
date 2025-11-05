from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QWidget, QFormLayout, QLineEdit, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import QSize, Qt
import os
from urllib.request import urlretrieve
from pathlib import Path
from openpyxl import load_workbook

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Vars
        self.data = []
        excel_vorlage_url = "https://github.com/dariokulici/ZHNG/raw/refs/heads/main/1.%20Lieferschein_Vorlage.xlsx"
        filename_location = "C:/Lieferscheine/Lieferschein_Vorlage.xlsx"

        folder_exists = os.path.isdir('C:/Lieferscheine/')
        if not folder_exists:
            os.mkdir('C:/Lieferscheine/')
            urlretrieve(excel_vorlage_url, filename_location)
        file_excel_vorlage = Path('C:/Lieferscheine/Lieferschein_Vorlage.xlsx')
        if not file_excel_vorlage.exists():
            urlretrieve(excel_vorlage_url, filename_location)

        # Windows Settings
        self.setWindowTitle("Lieferschein erstellen")
        self.setMinimumSize(QSize(300, 500))

        # App
        central_widget = QWidget()
        outer_layout = QVBoxLayout(central_widget)

        # Überschrift
        title = QLabel("Lieferschein Formular")
        title.setStyleSheet("font-size: 20px; font-weight: bold;")

        # Form
        form_layout = QFormLayout()

        self.line_name = QLineEdit()
        self.line_name.setFixedWidth(200)
        form_layout.addRow("Name:", self.line_name)

        self.line_firma = QLineEdit()
        self.line_firma.setFixedWidth(200)
        form_layout.addRow("Firma:", self.line_firma)

        self.line_adresse = QLineEdit()
        self.line_adresse.setFixedWidth(200)
        form_layout.addRow("Adresse:", self.line_adresse)

        self.line_plz = QLineEdit()
        self.line_plz.setFixedWidth(200)
        form_layout.addRow("PLZ:", self.line_plz)

        save_button = QPushButton("Speichern")
        save_button.clicked.connect(self.save_data)

        print_button = QPushButton("Drucken")
        print_button.clicked.connect(self.write_excel)

        outer_layout.addWidget(title)
        outer_layout.addLayout(form_layout)
        outer_layout.addWidget(save_button)
        outer_layout.addWidget(print_button)

        self.setCentralWidget(central_widget)
    def save_data(self):
        name = self.line_name.text()
        company = self.line_firma.text()
        address = self.line_adresse.text()
        plz = self.line_plz.text()

        self.data.append({
            "name": name,
            "company": company,
            "address": address,
            "plz": plz
        })
    def print_data(self):
        if not self.data:
            name = self.line_name.text()
            company = self.line_firma.text()
            address = self.line_adresse.text()
            plz = self.line_plz.text()
        else:
            name = self.data[0]
            company = self.data[1]
            address = self.data[2]
            plz = self.data[3]

    def write_excel(self):
        workbook = load_workbook(filename="C:/Lieferscheine/Lieferschein_Vorlage.xlsx")
        workbook.active = workbook['neu']
        

app = QApplication([])
window = MainWindow()
window.show()
app.exec()