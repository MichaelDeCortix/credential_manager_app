from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QTableWidget, QTableWidgetItem, QHBoxLayout, QCheckBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from core.credential_manager import CredentialManager
from gui.dialogs.add_credential_dialog import AddCredentialDialog
from gui.dialogs.edit_credential_dialog import EditCredentialDialog
from functools import partial

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Credential Manager")
        self.setGeometry(100, 100, 800, 600)

        # Установка шрифта по умолчанию
        self.setFont(QFont("Arial", 9))

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.show_passwords = False
        self.create_ui()

    def create_ui(self):
        button_layout = QHBoxLayout()
        
        self.add_button = QPushButton("Add Credential")
        self.add_button.clicked.connect(self.add_credential)
        button_layout.addWidget(self.add_button)

        self.show_passwords_checkbox = QCheckBox("Show Passwords")
        self.show_passwords_checkbox.stateChanged.connect(self.toggle_password_visibility)
        button_layout.addWidget(self.show_passwords_checkbox)

        self.layout.addLayout(button_layout)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Service", "Username", "Password", "Actions"])
        self.table.horizontalHeader().setStretchLastSection(True)
        self.layout.addWidget(self.table)

        self.refresh_credentials()

    def refresh_credentials(self):
        self.table.setRowCount(0)
        credentials = CredentialManager.get_all_credentials()
        for row, credential in enumerate(credentials):
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(credential.service_name))
            self.table.setItem(row, 1, QTableWidgetItem(credential.username))
            
            password = credential.password.replace('\x00', '') if credential.password else ""
            display_password = password if self.show_passwords else "*" * len(password)
            
            password_item = QTableWidgetItem(display_password)
            password_item.setData(Qt.UserRole, password)
            self.table.setItem(row, 2, password_item)
            
            edit_button = QPushButton("Edit")
            edit_button.clicked.connect(partial(self.edit_credential, credential))
            self.table.setCellWidget(row, 3, edit_button)

    def add_credential(self):
        dialog = AddCredentialDialog(self)
        if dialog.exec():
            credential = dialog.get_credential()
            CredentialManager.add_credential(credential)
            self.refresh_credentials()

    def edit_credential(self, credential):
        dialog = EditCredentialDialog(self, credential)
        if dialog.exec():
            updated_credential = dialog.get_credential()
            CredentialManager.update_credential(updated_credential)
            self.refresh_credentials()

    def toggle_password_visibility(self, state):
        self.show_passwords = state == Qt.Checked
        self.refresh_credentials()