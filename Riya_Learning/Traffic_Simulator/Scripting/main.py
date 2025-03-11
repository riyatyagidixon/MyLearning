import subprocess


def start_server():
    subprocess.Popen(["python", "backend/server.py"])


def start_gui():
    subprocess.Popen(["python", "gui/app.py"])


if __name__ == "__main__":
    start_server()
    start_gui()
