from flask import Flask, request, jsonify
from flask_cors import CORS

import predictor

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return "Hello World!"

@app.route('/predict', methods=['POST'])
def predict():
  values = request.json['values']
  predicted = predictor.predict(values)
  quality = int(predicted[0])

  return jsonify({'predicted': quality}), 200
