from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__, static_folder="static", template_folder="templates")

# Setup GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)  # Left Motor Forward
GPIO.setup(32, GPIO.OUT)  # Left Motor Backward
GPIO.setup(33, GPIO.OUT)  # Right Motor Forward
GPIO.setup(35, GPIO.OUT)  # Right Motor Backward

# Set up PWM for motor speed control
left_pwm_fwd = GPIO.PWM(12, 500)
left_pwm_bwd = GPIO.PWM(32, 500)
right_pwm_fwd = GPIO.PWM(33, 500)
right_pwm_bwd = GPIO.PWM(35, 500)

left_pwm_fwd.start(0)
left_pwm_bwd.start(0)
right_pwm_fwd.start(0)
right_pwm_bwd.start(0)

# Function to control left motor
def control_left_motor(speed, direction):
    if direction == 1:  # Forward
        left_pwm_bwd.ChangeDutyCycle(0)
        left_pwm_fwd.ChangeDutyCycle(speed)
    elif direction == -1:  # Backward
        left_pwm_fwd.ChangeDutyCycle(0)
        left_pwm_bwd.ChangeDutyCycle(speed)

# Function to control right motor
def control_right_motor(speed, direction):
    if direction == 1:  # Forward
        right_pwm_bwd.ChangeDutyCycle(0)
        right_pwm_fwd.ChangeDutyCycle(speed)
    elif direction == -1:  # Backward
        right_pwm_fwd.ChangeDutyCycle(0)
        right_pwm_bwd.ChangeDutyCycle(speed)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/forward')
def forward():
    left_speed = 50
    right_speed = 50
    control_left_motor(left_speed, 1)
    control_right_motor(right_speed, 1)

@app.route('/backward')
def backward():
    left_speed = 50
    right_speed = 50
    control_left_motor(left_speed, -1)
    control_right_motor(right_speed, -1)

@app.route('/stop')
def stop():
    control_left_motor(0, 1)
    control_right_motor(0, 1)
    return "Stopped!"

@app.route('/increase-speed')
def increase_speed():
    left_speed = 80  # Increase speed
    right_speed = 80
    control_left_motor(left_speed, 1)
    control_right_motor(right_speed, 1)

@app.route('/shutdown')
def shutdown():
    left_pwm_fwd.stop()
    left_pwm_bwd.stop()
    right_pwm_fwd.stop()
    right_pwm_bwd.stop()
    GPIO.cleanup()
    return "System shutdown!"

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5001)
    except KeyboardInterrupt:
        GPIO.cleanup()
