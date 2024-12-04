// Function to send motor control commands to the server
function controlMotor(action) {
    let baseUrl = 'http://10.243.86.94:5001'; // Base URL of your Flask server
    let url = '';

    // Define URLs for each action
    switch (action) {
        case 'forward':
            url = `${baseUrl}/forward`; // URL for moving forward
            break;
        case 'backward':
            url = `${baseUrl}/backward`; // URL for moving backward
            break;
        case 'stop':
            url = `${baseUrl}/stop`; // URL for stopping
            break;
        case 'increase-speed':
            url = `${baseUrl}/increase-speed`; // URL for increasing speed
            break;
        default:
            console.error('Unknown action:', action);
            return;
    }

    // Send request to the Flask server
    fetch(url)
        .then(response => {
            if (response.ok) {
                return response.text();
            }
            throw new Error('Request failed');
        })
        .then(data => {
            console.log('Server response:', data);
            alert(data); // Display server response as an alert
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred. Check the console for details.');
        });
}
