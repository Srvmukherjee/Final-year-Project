from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template("services.html")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    nodeNo = float(data['nodeNo'])
    kValue = float(data['kValue'])
    frequency = float(data['frequency'])
    signalPower = float(data['signalPower'])
    delay = float(data['delay'])
    packetLoss = float(data['packetLoss'])

    # Prepare the input data for prediction
    input_data = np.array([[nodeNo, kValue, frequency, signalPower, delay, packetLoss]])

    # Predict pathloss
    prediction = model.predict(input_data)
    predicted_pathloss = prediction[0]

    # Return the prediction as JSON
    return jsonify({'prediction': predicted_pathloss})

if __name__ == '__main__':
    app.run(debug=True)
