from flask import Flask, request, jsonify
import telnetlib

app = Flask(__name__)

# Global session object
session = {
    "connection": None,
    "ip": None,
    "username": None,
    "password": None
}

@app.route("/telnet_connect", methods=["POST"])
def telnet_connect():
    data = request.json
    ip = data.get("ip")
    username = data.get("username")
    password = data.get("password")

    try:
        tn = telnetlib.Telnet(ip, timeout=10)
        tn.read_until(b"login: ")
        tn.write(username.encode("ascii") + b"\n")
        tn.read_until(b"Password: ")
        tn.write(password.encode("ascii") + b"\n")

        session["connection"] = tn
        session["ip"] = ip
        session["username"] = username
        session["password"] = password

        return jsonify({"status": "connected"})
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)}), 500

@app.route("/telnet_status", methods=["POST"])
def telnet_status():
    if session["connection"]:
        return jsonify({"status": "connected"})
    return jsonify({"status": "disconnected"})

@app.route("/telnet_disconnect", methods=["POST"])
def telnet_disconnect():
    if session["connection"]:
        try:
            session["connection"].write(b"exit\n")
            session["connection"].close()
        except Exception:
            pass
        session["connection"] = None
        return jsonify({"message": "Disconnected from Telnet session."})
    return jsonify({"message": "No active session."})

@app.route("/telnet_run_command", methods=["POST"])
def run_telnet_command():
    if not session["connection"]:
        return jsonify({"error": "No active Telnet session."}), 400

    data = request.json
    command = data.get("command")
    try:
        session["connection"].write(command.encode("ascii") + b"\n")
        output = session["connection"].read_until(b"$", timeout=5).decode("utf-8", errors="ignore")
        return jsonify({"output": output})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
