from flask import Flask, request, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

# GPIO Pin Setup
MOTOR_PIN1 = 19  # Motor control pin 1
MOTOR_PIN2 = 26  # Motor control pin 2
PWM_PIN = 21     # PWM pin for speed control

GPIO.setmode(GPIO.BOARD)  # Use the BOARD pin numbering system
GPIO.setwarnings(False)  # Suppress GPIO warnings
GPIO.setup(MOTOR_PIN1, GPIO.OUT)
GPIO.setup(MOTOR_PIN2, GPIO.OUT)
GPIO.setup(PWM_PIN, GPIO.OUT)

# Set up PWM for speed control
pwm = GPIO.PWM(PWM_PIN, 500)  # Frequency = 500Hz
pwm.start(0)  # Start with 0% duty cycle (motor stopped)

# Variable to track speed
motor_speed = 25  # Initial speed (25% duty cycle)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/control")
def control():
    global motor_speed

    command = request.args.get("command")
    if command == "forward":
        print("Motor rotating forward.")
        GPIO.output(MOTOR_PIN1, GPIO.HIGH)
        GPIO.output(MOTOR_PIN2, GPIO.LOW)
        pwm.ChangeDutyCycle(motor_speed)  # Set speed

    elif command == "backward":
        print("Motor rotating backward.")
        GPIO.output(MOTOR_PIN1, GPIO.LOW)
        GPIO.output(MOTOR_PIN2, GPIO.HIGH)
        pwm.ChangeDutyCycle(motor_speed)  # Set speed

    elif command == "stop":
        print("Motor stopped.")
        GPIO.output(MOTOR_PIN1, GPIO.LOW)
        GPIO.output(MOTOR_PIN2, GPIO.LOW)
        pwm.ChangeDutyCycle(0)  # Stop PWM signal

    elif command == "increase-speed":
        motor_speed += 10  # Increase speed by 10%
        if motor_speed > 100:
            motor_speed = 100  # Cap speed at 100%
        print(f"Increasing motor speed to {motor_speed}%.")
        pwm.ChangeDutyCycle(motor_speed)

    else:
        print("Unknown command.")

    return "Command received: " + command, 200


# Cleanup GPIO on exit
@app.teardown_appcontext
def cleanup(exception=None):
    pwm.stop()
    GPIO.cleanup()


if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=5001, debug=True)
    except KeyboardInterrupt:
        print("Exiting program.")
        pwm.stop()
        GPIO.cleanup()
