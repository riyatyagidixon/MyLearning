from flask import Flask, request, jsonify
from flask_cors import CORS
import paramiko

# Backend Flask Server
app = Flask(__name__)
CORS(app)  # Enable CORS to allow GUI to communicate with backend

data_storage = {
    "ip": "",
    "username": "",
    "password": "",
}  # Variable to store input data


@app.route("/process", methods=["POST"])
def process_data():
    global data_storage
    data_storage = {
        "ip": request.json.get("ip", ""),
        "username": request.json.get("username", ""),
        "password": request.json.get("password", ""),
    }
    response = {"message": "Data stored successfully"}
    return jsonify(response)


@app.route("/fetch", methods=["GET"])
def fetch_data():
    return jsonify(
        {
            "ip": data_storage["ip"],
            "username": data_storage["username"],
            "password": data_storage["password"],
        }
    )


@app.route("/ssh_connect", methods=["POST"])
def ssh_connect():
    ip = request.json.get("ip", "")
    username = request.json.get("username", "")
    password = request.json.get("password", "")

    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, port=2222, username=username, password=password)

        # Run 'ls' command
        stdin, stdout, stderr = client.exec_command("ls")
        output = stdout.read().decode()
        error = stderr.read().decode()
        client.close()

        if error:
            print(f"Command failed: {error}")  # Print error in VS Code terminal
            return jsonify({"status": "Command failed", "error": error})

        print(f"Command Output:\n{output}")  # Print output in VS Code terminal
        return jsonify({"status": "Connection successful", " output": output})

    except Exception as e:
        print(f"Connection failed: {str(e)}")  # Print error in VS Code terminal
        return jsonify({"status": f"Connection failed: {str(e)}"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
