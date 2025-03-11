from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

# Backend Flask Server
app = Flask(__name__)
CORS(app)  # Enable CORS to allow GUI to communicate with backend

data_storage = ""  # Variable to store input data

@app.route('/process', methods=['POST'])
def process_data():
    global data_storage
    data_storage = request.json.get('input_data', '')
    response = {"message": "Data stored successfully"}
    return jsonify(response)

@app.route('/fetch', methods=['GET'])
def fetch_data():
    return jsonify({"message": data_storage})

if __name__ == '__main__':
    app.run(debug=True, port=5000)