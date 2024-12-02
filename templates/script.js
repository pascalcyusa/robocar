document.addEventListener('DOMContentLoaded', () => {
    const timeDisplay = document.getElementById('time-display');
    const forwardButton = document.getElementById('forward');
    const backwardButton = document.getElementById('backward');
    const leftButton = document.getElementById('left');
    const rightButton = document.getElementById('right');
    const stopButton = document.getElementById('stop');
    const boostButton = document.getElementById('boost');

    let direction = null;
    let boost = false;

    const updateTime = () => {
        timeDisplay.textContent = new Date().toLocaleTimeString();
    };

    setInterval(updateTime, 1000);
    updateTime(); // Initial call to set the time immediately

    const handleKeyDown = (e) => {
        switch (e.key.toLowerCase()) {
            case 'arrowup':
                setDirection('forward');
                break;
            case 'arrowdown':
                setDirection('backward');
                break;
            case 'arrowleft':
                setDirection('left');
                break;
            case 'arrowright':
                setDirection('right');
                break;
            case 's':
                setDirection(null);
                break;
            case 'a':
                setBoost(true);
                handleBoost();
                break;
        }
    };

    const handleKeyUp = (e) => {
        if (e.key.toLowerCase() === 'a') {
            setBoost(false);
        }
        if (['arrowup', 'arrowdown', 'arrowleft', 'arrowright'].includes(e.key.toLowerCase())) {
            setDirection(null);
        }
    };

    const setDirection = (dir) => {
        direction = dir;
        updateButtonStyles();
    };

    const setBoost = (isBoost) => {
        boost = isBoost;
        boostButton.classList.toggle('bg-yellow-500', boost);
        boostButton.classList.toggle('hover:bg-yellow-600', boost);
    };

    const updateButtonStyles = () => {
        forwardButton.classList.toggle('bg-blue-500', direction === 'forward');
        forwardButton.classList.toggle('hover:bg-blue-600', direction === 'forward');
        backwardButton.classList.toggle('bg-blue-500', direction === 'backward');
        backwardButton.classList.toggle('hover:bg-blue-600', direction === 'backward');
        leftButton.classList.toggle('bg-blue-500', direction === 'left');
        leftButton.classList.toggle('hover:bg-blue-600', direction === 'left');
        rightButton.classList.toggle('bg-blue-500', direction === 'right');
        rightButton.classList.toggle('hover:bg-blue-600', direction === 'right');
    };

    const handleBoost = async () => {
        try {
            const response = await fetch('/drivefast', {
                method: 'GET',
            });
            if (response.ok) {
                console.log('GET request successful');
            } else {
                console.error('GET request failed');
            }
        } catch (error) {
            console.error('Error sending GET request:', error);
        }
    };

    forwardButton.addEventListener('click', () => setDirection('forward'));
    backwardButton.addEventListener('click', () => setDirection('backward'));
    leftButton.addEventListener('click', () => setDirection('left'));
    rightButton.addEventListener('click', () => setDirection('right'));
    stopButton.addEventListener('click', () => setDirection(null));

    boostButton.addEventListener('mousedown', () => {
        setBoost(true);
        handleBoost();
    });
    boostButton.addEventListener('mouseup', () => setBoost(false));
    boostButton.addEventListener('mouseleave', () => setBoost(false));

    window.addEventListener('keydown', handleKeyDown);
    window.addEventListener('keyup', handleKeyUp);
});
