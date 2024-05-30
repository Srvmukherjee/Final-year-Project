from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template("services.html")

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return render_template("predict.html")
    elif request.method == 'POST':
        data = request.get_json()
        nodeNo = int(data['nodeNo'])
        kValue = int(data['kValue'])
        frequency = int(data['frequency'])
        signalPower = float(data['signalPower'])
        delay = float(data['delay'])
        packetLoss = int(data['packetLoss'])

        # Prepare the input data for prediction
        input_data = np.array([[nodeNo, kValue, frequency, signalPower, delay, packetLoss]])

        # Predict pathloss
        prediction = model.predict(input_data)
        predicted_pathloss = prediction[0]

        # Return the prediction as JSON
        return jsonify({'prediction': predicted_pathloss})

if __name__ == '__main__':
    app.run(debug=True)
