function predictPathloss() {
    // Get input values from the form
    var nodeNo = document.getElementById("nodeNo").value;
    var kValue = document.getElementById("kValue").value;
    var frequency = document.getElementById("frequency").value;
    var signalPower = document.getElementById("signalPower").value;
    var delay = document.getElementById("delay").value;
    var packetLoss = document.getElementById("packetLoss").value;

    // Create a data object to send to the server
    var data = {
        nodeNo: nodeNo,
        kValue: kValue,
        frequency: frequency,
        signalPower: signalPower,
        delay: delay,
        packetLoss: packetLoss
    };

    // Send an Ajax request to the server
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/predict", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                // Display the prediction result in the div
                document.getElementById("predictionResult").innerText = xhr.responseText;
            } else {
                // Display an error message if the request fails
                document.getElementById("predictionResult").innerText = "Prediction failed. Please try again later.";
            }
        }
    };
    xhr.send(JSON.stringify(data));
}
