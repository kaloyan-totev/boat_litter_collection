import RPi.GPIO as GPIO
import time

# Configure GPIO
servo_pin = 19
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Set PWM frequency
pwm_frequency = 50
pwm = GPIO.PWM(servo_pin, pwm_frequency)
pwm.start(0)
# Set throttle values
zero_throttle = 90  # Needs to be between 66 and 101.
max_throttle = 120  # Maximum throttle
min_throttle = 60   # Represents the "reverse" speed

# Function to set throttle
def set_throttle(throttle):
    duty = throttle / 18 + 2
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)

# Main setup
def setup():
    print("Zero Throttle")
    set_throttle(zero_throttle)
    time.sleep(5)

    print("Max")
    set_throttle(max_throttle)
    time.sleep(2)

    print("Zero")
    set_throttle(zero_throttle)
    time.sleep(2)

    print("Min")
    set_throttle(min_throttle)
    time.sleep(0.02)

    print("Zero")
    set_throttle(zero_throttle)
    time.sleep(0.02)

    print("Min")
    set_throttle(min_throttle)
    time.sleep(2)

    print("Setup Complete")

# Main loop
def loop():
    # Increasing throttle
    for pos in range(zero_throttle, max_throttle):
        set_throttle(pos)
        print(pos)
        time.sleep(0.2)

    set_throttle(max_throttle)
    time.sleep(2)

    set_throttle(zero_throttle)
    time.sleep(2)

    # Decreasing throttle
    for pos in range(zero_throttle, min_throttle, -1):
        set_throttle(pos)
        print(pos)
        time.sleep(0.2)

    time.sleep(2)
    set_throttle(zero_throttle)
    time.sleep(2)

try:
    setup()
    while True:
        loop()
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()

