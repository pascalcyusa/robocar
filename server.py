from flask import Flask, render_template, jsonify
import RPi.GPIO as GPIO
import logging

app = Flask(__name__)

# GPIO pin setup
# Motor A (left motor)
IN1 = 27
IN2 = 29
# Motor B (right motor)
IN3 = 20
IN4 = 16

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)  # Disable GPIO warnings
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# Motor control functions
def move_forward():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

def move_backward():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)

def stop():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)

def control_robot(action):
    if action == 'forward':
        move_forward()
    elif action == 'backward':
        move_backward()
    elif action == 'stop':
        stop()
    else:
        logging.error(f"Invalid action: {action}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<action>')
def action(action):
    control_robot(action)
    return jsonify({"status": "success", "action": action})

@app.route('/shutdown', methods=['POST'])
def shutdown():
    try:
        stop()
        GPIO.cleanup()
        return jsonify({"status": "success", "message": "GPIO cleaned up"}), 200
    except Exception as e:
        logging.error(f"Error during shutdown: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.INFO)
        logging.info("Starting Flask app")
        app.run(host='0.0.0.0', port=5001, debug=True)
    except KeyboardInterrupt:
        logging.info("Keyboard interrupt received, cleaning up GPIO")
        GPIO.cleanup()
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        GPIO.cleanup()
