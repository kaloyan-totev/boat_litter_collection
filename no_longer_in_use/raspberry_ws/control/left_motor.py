import RPi.GPIO as GPIO
import time

servo_pin = 13

zero_throttle = 90
max_throttle = 120
min_throttle = 60

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
servo_pwm = GPIO.PWM(servo_pin, 50)  # 50 Hz frequency for the servo

servo_pwm.start(0)

def set_throttle_left(throttle):
    duty = throttle / 18 + 2
    GPIO.output(servo_pin, True)
    servo_pwm.ChangeDutyCycle(duty)
    time.sleep(1)

try:
    print("Zero Throttle")
    set_throttle_left(zero_throttle)
    time.sleep(2)

    print("Max")
    set_throttle_left(max_throttle)
    time.sleep(200)

    print("Zero")
    set_throttle_left(zero_throttle)
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

    while True:
        for pos in range(zero_throttle, max_throttle + 1):
            set_throttle(pos)
            time.sleep(0.2)
            print(pos)

        set_throttle(max_throttle)
        time.sleep(2)

        set_throttle(zero_throttle)
        time.sleep(2)

        set_throttle(min_throttle)
        time.sleep(0.02)

        set_throttle(zero_throttle)
        time.sleep(0.02)

        for pos in range(zero_throttle, min_throttle - 1, -1):
            set_throttle(pos)
            time.sleep(0.2)
            print(pos)

        time.sleep(2)
        set_throttle(zero_throttle)
        time.sleep(2)

except KeyboardInterrupt:
    print("Stopped by User")
    servo_pwm.stop()
    GPIO.cleanup()

