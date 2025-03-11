from PyQt5 import QtWidgets, QtCore
import sys
import requests


class AppWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Python PyQt GUI-Backend Communication")
        self.setGeometry(100, 100, 400, 250)

        # Main Layout (Vertical)
        layout = QtWidgets.QVBoxLayout()

        # Input Layout (Horizontal)
        input_layout = QtWidgets.QHBoxLayout()
        self.input_field = QtWidgets.QLineEdit()
        self.input_field.setPlaceholderText("IP Address")
        self.submit_button = QtWidgets.QPushButton("Submit")
        self.submit_button.clicked.connect(self.send_data)
        input_layout.addWidget(self.input_field)
        input_layout.addWidget(self.submit_button)

        # Output Layout (Horizontal)
        output_layout = QtWidgets.QHBoxLayout()
        self.output_label = QtWidgets.QTextEdit()
        self.output_label.setReadOnly(True)
        self.output_label.setStyleSheet("border: 1px solid black; min-height: 50px;")

        self.fetch_button = QtWidgets.QPushButton("Fetch Data")
        self.fetch_button.clicked.connect(self.fetch_data)

        output_layout.addWidget(self.output_label)
        output_layout.addWidget(self.fetch_button)

        # Add layouts to main layout
        layout.addLayout(input_layout)
        layout.addLayout(output_layout)

        self.setLayout(layout)

    def send_data(self):
        user_input = self.input_field.text()
        if not user_input:
            QtWidgets.QMessageBox.warning(self, "Error", "Input field cannot be empty!")
            return
        response = requests.post(
            "http://127.0.0.1:5000/process", json={"input_data": user_input}
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
            self.output_label.setText(response.json()["message"])
        else:
            QtWidgets.QMessageBox.critical(self, "Error", "Failed to fetch data!")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = AppWindow()
    window.show()
    sys.exit(app.exec_())
