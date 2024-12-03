from flask import Flask, render_template, jsonify
import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)   # use the BOARD pin-numbering system
GPIO.setup(19, GPIO.OUT)   # like digitalio.DigitalInOut(board.D16)
GPIO.setup(26, GPIO.OUT)   # like digitalio.DigitalInOut(board.D16)
                            # and digitalio.Direction.OUTPUT


# Motor control functions
def move_forward():
    GPIO.output(19, GPIO.HIGH)
    GPIO.output(26, GPIO.LOW)

def move_backward():
    GPIO.output(19, GPIO.LOW)
    GPIO.output(26, GPIO.HIGH)

def stop():
    GPIO.output(19, GPIO.LOW)
    GPIO.output(26, GPIO.LOW)

def control_robot(action):
    if action == 'forward':
        move_forward()
    elif action == 'backward':
        move_backward()
    elif action == 'stop':
        stop()

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
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5001, debug=True)
    except KeyboardInterrupt:
        GPIO.cleanup()
    except Exception:
        GPIO.cleanup()
