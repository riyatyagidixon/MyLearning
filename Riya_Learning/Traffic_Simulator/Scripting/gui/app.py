import sys
import re
import requests
from qtpy.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QGroupBox,
    QMainWindow,
    QStackedWidget,
    QFormLayout,
    QApplication,
)
from qtpy.QtCore import Qt

BACKEND_URL = "http://localhost:5000"

class SSHApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SSH Connection App")
        self.setGeometry(200, 200, 600, 400)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.init_login_page()
        self.init_output_page()

        self.stack.addWidget(self.login_page)
        self.stack.addWidget(self.output_page)

        self.stack.setCurrentWidget(self.login_page)

    def init_login_page(self):
        self.login_page = QWidget()
        main_layout = QVBoxLayout()

        credentials_box = QGroupBox("Login Credentials")
        credentials_layout = QVBoxLayout()

        form_layout = QFormLayout()

        self.ip_input = QLineEdit()
        self.ip_input.setPlaceholderText("Enter IP Address")
        self.ip_input.setText("127.0.0.1")
        form_layout.addRow("IP Address:", self.ip_input)

        self.username_input = QLineEdit("admin")
        self.username_input.setPlaceholderText("Enter Username")
        self.username_input.setText("guest")
        form_layout.addRow("Username:", self.username_input)

        self.password_input = QLineEdit("password")
        self.password_input.setPlaceholderText("Enter Password")
        self.password_input.setText("guest123")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.eye_button = QPushButton("\U0001F441")  # Eye icon
        self.eye_button.setCheckable(True)
        self.eye_button.setFixedWidth(30)
        self.eye_button.clicked.connect(self.toggle_password)

        pass_layout = QHBoxLayout()
        pass_layout.addWidget(self.password_input)
        pass_layout.addWidget(self.eye_button)
        form_layout.addRow("Password:", pass_layout)

        credentials_layout.addLayout(form_layout)

        self.output_box = QTextEdit()
        self.output_box.setReadOnly(True)
        self.output_box.setPlaceholderText("Validation output will appear here...")
        credentials_layout.addWidget(self.output_box)

        button_layout = QHBoxLayout()
        self.disconnect_btn = QPushButton("Disconnect")
        self.status_btn = QPushButton("Status")
        self.connect_btn = QPushButton("Connect")

        self.disconnect_btn.clicked.connect(self.ssh_disconnect)
        self.status_btn.clicked.connect(self.ssh_status)
        self.connect_btn.clicked.connect(self.ssh_connect)

        button_layout.addWidget(self.disconnect_btn)
        button_layout.addWidget(self.status_btn)
        button_layout.addWidget(self.connect_btn)

        credentials_layout.addLayout(button_layout)
        credentials_box.setLayout(credentials_layout)

        main_layout.addWidget(credentials_box)

        control_button_layout = QHBoxLayout()

        self.next_button = QPushButton("Next →")
        self.next_button.setFixedSize(100, 30)
        self.next_button.setStyleSheet(
            """
            QPushButton {
                background-color: #A5D6A7;
                border: 2px solid #1e90ff;
                border-radius: 5px;
                color: white;
                font-weight: bold;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """
        )
        control_button_layout.addWidget(self.next_button, alignment=Qt.AlignRight)
        self.next_button.clicked.connect(self.go_to_next)
        main_layout.addLayout(control_button_layout)

        self.login_page.setLayout(main_layout)

    def init_output_page(self):
        self.output_page = QWidget()
        layout = QVBoxLayout()

        command_box = QGroupBox("Command Execution")
        command_box.setStyleSheet("QGroupBox { font-weight: bold; font-size: 14px; }")
        command_layout = QVBoxLayout()
        self.command_input = QTextEdit()
        self.command_input.setPlaceholderText("Enter the commands to run")
        command_layout.addWidget(self.command_input)

        self.run_command_btn = QPushButton("Run Command")
        self.run_command_btn.clicked.connect(self.run_ssh_command)
        command_layout.addWidget(self.run_command_btn)

        command_box.setLayout(command_layout)
        layout.addWidget(command_box)

        result_box = QGroupBox("Output")
        result_box.setStyleSheet("QGroupBox { font-weight: bold; font-size: 14px; }")
        result_layout = QVBoxLayout()
        self.command_output = QTextEdit()
        self.command_output.setPlaceholderText("Result will show here")
        self.command_output.setReadOnly(True)
        result_layout.addWidget(self.command_output)
        result_box.setLayout(result_layout)
        layout.addWidget(result_box)

        self.back_btn = QPushButton("\u2190Back")
        self.back_btn.setFixedSize(100, 30)
        self.back_btn.setStyleSheet(
            """
            QPushButton {
                background-color: #A5D6A7;
                border: 2px solid #1e90ff;
                border-radius: 5px;
                color: white;
                font-weight: bold;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """
        )
        self.back_btn.clicked.connect(self.go_back_to_login)
        layout.addWidget(self.back_btn)

        self.output_page.setLayout(layout)

    def toggle_password(self):
        if self.eye_button.isChecked():
            self.password_input.setEchoMode(QLineEdit.Normal)
        else:
            self.password_input.setEchoMode(QLineEdit.Password)

    def ssh_connect(self):
        ip = self.ip_input.text().strip()
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()

        self.output_box.clear()
        if not ip or not username or not password:
            self.output_box.setText("❌ All fields are required.")
            return

        ip_pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
        if not re.match(ip_pattern, ip):
            self.output_box.setText("❌ Invalid IP address format.")
            return

        self.output_box.setText("⏳ Connecting to SSH server via backend...")
        QApplication.processEvents()

        try:
            response = requests.post(f"{BACKEND_URL}/ssh_connect", json={
                "ip": ip,
                "username": username,
                "password": password
            })
            data = response.json()
            if data.get("status") == "connected":
                self.output_box.setText("✅ SSH connection successful via backend!")
                self.stack.setCurrentWidget(self.output_page)
            else:
                self.output_box.setText(f"❌ SSH connection failed: {data.get('error', 'Unknown error')}")
        except Exception as e:
            self.output_box.setText(f"❌ Backend error: {e}")

    def run_ssh_command(self):
        command = self.command_input.toPlainText().strip()
        if not command:
            self.command_output.setPlainText("⚠️ Please enter a command to execute.")
            return

        try:
            response = requests.post(f"{BACKEND_URL}/run_command", json={"command": command})
            data = response.json()
            if "output" in data:
                self.command_output.setPlainText(data["output"])
            elif "error" in data:
                self.command_output.setPlainText(f"❌ {data['error']}")
            else:
                self.command_output.setPlainText("⚠️ No output received.")
        except Exception as e:
            self.command_output.setPlainText(f"❌ Error running command: {e}")

    def ssh_status(self):
        try:
            response = requests.post(f"{BACKEND_URL}/ssh_status")
            data = response.json()
            if data.get("status") == "connected":
                self.output_box.setText("✅ SSH session is active.")
            else:
                self.output_box.setText("❌ SSH session is not connected.")
        except Exception as e:
            self.output_box.setText(f"❌ Error checking SSH status: {e}")

    def ssh_disconnect(self):
        try:
            response = requests.post(f"{BACKEND_URL}/ssh_disconnect")
            data = response.json()
            self.output_box.setText(data.get("message", "Disconnected."))
            self.stack.setCurrentWidget(self.login_page)
        except Exception as e:
            self.output_box.setText(f"❌ Error disconnecting: {e}")

    def go_back_to_login(self):
        self.stack.setCurrentWidget(self.login_page)

    def go_to_next(self):
        self.stack.setCurrentWidget(self.output_page)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SSHApp()
    window.show()
    sys.exit(app.exec_())
