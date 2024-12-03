document.addEventListener('DOMContentLoaded', () => {
    const timeDisplay = document.getElementById('time-display');
    const forwardButton = document.getElementById('forward');
    const backwardButton = document.getElementById('backward');
    const stopButton = document.getElementById('stop');

    const updateTime = () => {
        timeDisplay.textContent = new Date().toLocaleTimeString();
    };

    setInterval(updateTime, 1000);
    updateTime(); // Initial call to set the time immediately

    const handleKeyDown = (e) => {
        switch (e.key.toLowerCase()) {
            case 'arrowup':
                moveRobot('forward');
                break;
            case 'arrowdown':
                moveRobot('backward');
                break;
            case 's':
                moveRobot('stop');
                break;
        }
    };

    const handleKeyUp = (e) => {
        if (['arrowup', 'arrowdown'].includes(e.key.toLowerCase())) {
            moveRobot('stop');
        }
    };

    const moveRobot = async (action) => {
        try {
            const response = await fetch(`/${action}`, {
                method: 'GET',
            });
            if (response.ok) {
                console.log(`Robot is moving ${action}`);
            } else {
                console.error('Failed to move robot');
            }
        } catch (error) {
            console.error('Error sending GET request:', error);
        }
    };

    forwardButton.addEventListener('click', () => moveRobot('forward'));
    backwardButton.addEventListener('click', () => moveRobot('backward'));
    stopButton.addEventListener('click', () => moveRobot('stop'));

    window.addEventListener('keydown', handleKeyDown);
    window.addEventListener('keyup', handleKeyUp);
});
