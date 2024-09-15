from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from core.models import Credential
from utils.validators import validate_service_name, validate_username, validate_password

class AddCredentialDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add Credential")
        self.layout = QVBoxLayout(self)

        self.service_name_input = QLineEdit()
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.layout.addWidget(QLabel("Service Name:"))
        self.layout.addWidget(self.service_name_input)
        self.layout.addWidget(QLabel("Username:"))
        self.layout.addWidget(self.username_input)
        self.layout.addWidget(QLabel("Password:"))
        self.layout.addWidget(self.password_input)

        self.submit_button = QPushButton("Add")
        self.submit_button.clicked.connect(self.validate_and_accept)
        self.layout.addWidget(self.submit_button)

    def validate_and_accept(self):
        service_name = self.service_name_input.text()
        username = self.username_input.text()
        password = self.password_input.text()

        if not validate_service_name(service_name):
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid service name.")
            return
        if not validate_username(username):
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid username.")
            return
        if not validate_password(password):
            QMessageBox.warning(self, "Invalid Input", "Password must be at least 8 characters long and contain uppercase, lowercase, and digits.")
            return

        self.accept()

    def get_credential(self):
        return Credential(
            self.service_name_input.text(),
            self.username_input.text(),
            self.password_input.text()
        )