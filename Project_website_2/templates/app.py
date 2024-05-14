# app.py

from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Define route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the form
    node_no = float(request.form['nodeNo'])
    k_value = float(request.form['kValue'])
    frequency = float(request.form['frequency'])
    signal_power = float(request.form['signalPower'])
    delay = float(request.form['delay'])
    packet_loss = float(request.form['packetLoss'])

    # Make prediction using the loaded model
    prediction = model.predict([[node_no, k_value, frequency, signal_power, delay, packet_loss]])

    # Return prediction result
    return render_template('result.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)
