# OLT Configuration Script

## 🚀 Overview

This project demonstrates how to create an OLT telnet session and push and see configuration of OLT/ONT using `QtPy` for the GUI, which interacts with a `FastAPI` backend.

---

## 📂 Project Structure

```bash
OLT-Configuration/
├── gui/                     # Frontend (QtPy-based GUI)
│   ├── __init__.py
│   ├── main.py              # GUI Main Entry Point
│   ├── main_page.py         # Main GUI Page
│   ├── olt_page.py          # OLT Configuration Page
│   ├── ont_page.py          # ONT Configuration Page
│   ├── requirements.txt     # Frontend Dependencies
├── backend/                 # Backend (FastAPI)
│   ├── __init__.py
│   ├── main.py              # FastAPI Entry Point
│   ├── olt_telnet.py        # Handles OLT Telnet Connection
│   ├── olt_config.py        # OLT Configuration APIs
│   ├── ont_config.py        # ONT Configuration APIs
│   ├── requirements.txt     # Backend Dependencies
├── shared/                  # Shared Configuration
│   ├── config.py            # Stores Global Configurations
├── tests/                   # Test Cases
│   ├── test_backend.py
├── README.md                # Documentation
├── .gitignore               # Ignore Unwanted Files
```

## 🔧 **Installation**

### 🛠 1️⃣ **Clone the Repository**

```sh
git clone https://github.com/prashantpateldixoninfo/MyLearning.git
cd MyLearning/Traffic_Simulator/OLT-Configuration
```

### 🖥 2️⃣ **Set Up Backend**

```sh
cd backend
python -m venv venv   # Create Virtual Environment for one time
venv\Scripts\activate  # Activate (Windows)
pip install -r requirements.txt  # Install Dependencies
deactivate   # Deactivate Environment
```

### 🎨 3️⃣ **Set Up GUI**

```sh
cd gui
python -m venv venv   # Create Virtual Environment for one time
venv\Scripts\activate  # Activate (Windows)
pip install -r requirements.txt  # Install Dependencies
deactivate   # Deactivate Environment
```

---

## 🚀 **Running the Application**

### 🔹 1️⃣ **Start Backend Server**

```sh
python -m main
```

This will run the FastAPI backend on `http://127.0.0.1:8000`.

### 🔹 2️⃣ **Start GUI Application**

```sh
python -m main
```

---

## 🧪 **Running Tests**

```sh
cd tests
python -m unittest discover
```

---

## 📌 **Additional Notes**

-   The backend runs on **port 8000**.
-   The GUI interacts with the backend via API calls.
-   Ensure both environments (`gui/venv` and `backend/venv`) are activated while running respective parts.
-   Update dependencies using:
    ```sh
    pip install -r requirements.txt
    ```
