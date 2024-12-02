from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

# Set up GPIO mode and pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)  # Example pin for forward
GPIO.setup(13, GPIO.OUT)  # Example pin for backward
GPIO.setup(15, GPIO.OUT)  # Example pin for left
GPIO.setup(16, GPIO.OUT)  # Example pin for right
GPIO.setup(18, GPIO.OUT)  # Example pin for stop
GPIO.setup(22, GPIO.OUT)  # Example pin for boost

# Function to control the robot's movement


def control_robot(action):
    if action == 'forward':
        GPIO.output(11, GPIO.HIGH)
        GPIO.output(13, GPIO.LOW)
    elif action == 'backward':
        GPIO.output(11, GPIO.LOW)
        GPIO.output(13, GPIO.HIGH)
    elif action == 'left':
        GPIO.output(15, GPIO.HIGH)
        GPIO.output(16, GPIO.LOW)
    elif action == 'right':
        GPIO.output(15, GPIO.LOW)
        GPIO.output(16, GPIO.HIGH)
    elif action == 'stop':
        GPIO.output(18, GPIO.HIGH)
    elif action == 'boost':
        GPIO.output(22, GPIO.HIGH)
    else:
        GPIO.output(11, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(15, GPIO.LOW)
        GPIO.output(16, GPIO.LOW)
        GPIO.output(18, GPIO.LOW)
        GPIO.output(22, GPIO.LOW)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<action>')
def action(action):
    control_robot(action)
    return f'Robot is moving {action}'


if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        GPIO.cleanup()
