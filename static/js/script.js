function controlMotor(action) {
    // Define the URL for the action
    var url = "http://10.243.86.94:5001/control?command=" + action;

    // Create a new XMLHttpRequest object
    var xhr = new XMLHttpRequest();

    // Set up a callback function to handle the response
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            console.log("Command sent: " + action);
        } else if (xhr.readyState == 4) {
            console.error("Error sending command: " + xhr.status);
        }
    };

    // Send the GET request
    xhr.open("GET", url, true);
    xhr.send();
}
