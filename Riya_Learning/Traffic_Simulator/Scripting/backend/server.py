from flask import Flask, request, jsonify
from flask_cors import CORS
import paramiko

app = Flask(__name__)
CORS(app)

# Class to manage SSH connection
class SSHManager:
    def __init__(self):
        self.client = None

    def connect(self, ip, username, password, port=2222):
        try:
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(ip, port=port, username=username, password=password)
            return True, "Connected successfully"
        except Exception as e:
            self.client = None
            return False, str(e)

    def disconnect(self):
        if self.client and self.client.get_transport() and self.client.get_transport().is_active():
            self.client.close()
            self.client = None
            return True, "Disconnected successfully"
        else:
            return False, "No active SSH connection"

    def status(self):
        return self.client is not None and self.client.get_transport() and self.client.get_transport().is_active()

    def run_command(self, command):
        if self.status():
            stdin, stdout, stderr = self.client.exec_command(command)
            return stdout.read().decode(), stderr.read().decode()
        else:
            return None, "SSH connection not active"

# Create a single manager instance
ssh_manager = SSHManager()

@app.route("/ssh_connect", methods=["POST"])
def ssh_connect():
    ip = request.json.get("ip", "")
    username = request.json.get("username", "")
    password = request.json.get("password", "")

    print(f"Connecting to {ip} with username '{username}'")

    success, message = ssh_manager.connect(ip, username, password)
    if success:
        return jsonify({"status": "connected", "output": message})
    else:
        return jsonify({"status": "failed", "error": message})

@app.route("/ssh_disconnect", methods=["POST"])
def ssh_disconnect():
    success, message = ssh_manager.disconnect()
    return jsonify({"status": message})

@app.route("/ssh_status", methods=["GET"])
def ssh_status():
    if ssh_manager.status():
        return jsonify({"status": "connected"})
    else:
        return jsonify({"status": "disconnected"})

@app.route("/run_command", methods=["POST"])
def run_command():
    command = request.json.get("command", "")
    if not command:
        return jsonify({"error": "No command provided"})

    output, error = ssh_manager.run_command(command)
    if error:
        return jsonify({"error": error})
    return jsonify({"output": output})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
