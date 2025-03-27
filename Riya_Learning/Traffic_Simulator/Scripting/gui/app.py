from PyQt5 import QtWidgets, QtCore
import sys
import requests
import re


class AppWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Python PyQt GUI-Backend Communication")
        self.setGeometry(100, 100, 400, 300)

        # Main Layout (Vertical)
        layout = QtWidgets.QVBoxLayout()

        # Input Field for IP Address
        self.input_field = QtWidgets.QLineEdit()
        self.input_field.setPlaceholderText("IP Address")
        self.input_field.setText("127.0.0.1")
        layout.addWidget(self.input_field)

        # Input Field for Username
        self.username_field = QtWidgets.QLineEdit()
        self.username_field.setPlaceholderText("Username")
        self.username_field.setText("guest")
        layout.addWidget(self.username_field)

        # Input Field for Password
        self.password_field = QtWidgets.QLineEdit()
        self.password_field.setPlaceholderText("Password")
        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_field.setText("guest123")
        layout.addWidget(self.password_field)

        # Submit Button (Below Password Field)
        self.submit_button = QtWidgets.QPushButton("Submit")
        self.submit_button.clicked.connect(self.send_data)
        layout.addWidget(self.submit_button)

        # Output Layout (Horizontal)
        output_layout = QtWidgets.QHBoxLayout()
        self.output_label = QtWidgets.QTextEdit()
        self.output_label.setReadOnly(True)
        self.output_label.setStyleSheet("border: 1px solid black; min-height: 50px;")

        self.fetch_button = QtWidgets.QPushButton("Fetch Data")
        self.fetch_button.clicked.connect(self.fetch_data)

        self.ssh_button = QtWidgets.QPushButton("SSH Connect")
        self.ssh_button.clicked.connect(self.ssh_connect)

        output_layout.addWidget(self.output_label)
        output_layout.addWidget(self.fetch_button)
        output_layout.addWidget(self.ssh_button)

        layout.addLayout(output_layout)

        self.setLayout(layout)

    def validate_ip(self, ip):
        pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
        if not re.match(pattern, ip):
            return False
        parts = ip.split(".")
        for part in parts:
            if int(part) < 0 or int(part) > 255:
                return False
        return True

    def send_data(self):
        user_input = self.input_field.text()
        username = self.username_field.text()
        password = self.password_field.text()

        if not user_input or not username or not password:
            QtWidgets.QMessageBox.warning(self, "Error", "All fields are required!")
            return

        if not self.validate_ip(user_input):
            QtWidgets.QMessageBox.warning(self, "Error", "Invalid IP address format!")
            return

        response = requests.post(
            "http://127.0.0.1:5000/process",
            json={"ip": user_input, "username": username, "password": password},
        )
        if response.status_code == 200:
            QtWidgets.QMessageBox.information(
                self, "Success", "Data submitted successfully!"
            )
        else:
            QtWidgets.QMessageBox.critical(
                self, "Error", "Failed to communicate with backend!"
            )

    def fetch_data(self):
        response = requests.get("http://127.0.0.1:5000/fetch")
        if response.status_code == 200:
            data = response.json()
            self.output_label.setText(
                f"IP: {data['ip']}\nUsername: {data['username']}\nPassword: {data['password']}"
            )
        else:
            QtWidgets.QMessageBox.critical(self, "Error", "Failed to fetch data!")

    def ssh_connect(self):
        user_input = self.input_field.text()
        username = self.username_field.text()
        password = self.password_field.text()

        if not user_input or not username or not password:
            QtWidgets.QMessageBox.warning(self, "Error", "All fields are required!")
            return

        response = requests.post(
            "http://127.0.0.1:5000/ssh_connect",
            json={"ip": user_input, "username": username, "password": password},
        )

        if response.status_code == 200:
            data = response.json()
            status = data["status"]
            output = data.get("output", "")

            self.output_label.setText(f"SSH Status: {status}\n\nOutput:\n{output}")
            QtWidgets.QMessageBox.information(self, "SSH Status", status)
        else:
            QtWidgets.QMessageBox.critical(self, "Error", "Failed to connect via SSH!")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = AppWindow()
    window.show()
    sys.exit(app.exec_())
