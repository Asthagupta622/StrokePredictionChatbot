from flask_cors import CORS
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)


# Load the trained ML model
model = joblib.load('stroke_model.pkl')

@app.route('/')
def home():
    return "Stroke Prediction API is running."

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    try:
        input_data = np.array(list(data.values())).reshape(1, -1)
        prediction = model.predict(input_data)
        result = "High Risk of Stroke" if prediction[0] == 1 else "Low Risk of Stroke"
        return jsonify({"prediction": result})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
