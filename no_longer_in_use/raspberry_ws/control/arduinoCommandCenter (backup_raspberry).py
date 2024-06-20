import time
import serial
import RPi.GPIO as GPIO

class Command:
    def __init__(self):
        # Define servo pins
        self.left_motor_pin = 12
        self.right_motor_pin = 13

        # Set GPIO mode
        GPIO.setmode(GPIO.BCM)

        # Initialize GPIO pins
        GPIO.setup(self.left_motor_pin, GPIO.OUT)
        GPIO.setup(self.right_motor_pin, GPIO.OUT)

        # Initialize PWM
        self.left_pwm = GPIO.PWM(self.left_motor_pin, 100)  # 100 Hz frequency
        self.right_pwm = GPIO.PWM(self.right_motor_pin, 100)

        # Start PWM with 0% duty cycle (stopped)
        self.left_pwm.start(0)
        self.right_pwm.start(0)

        # Define servo angles
        self.zero_speed = 90
        self.max_speed = 120
        self.min_speed = 60
        
        self.currentCommand = 1

    def go_left(self):
        self.currentCommand = 3
        self.right_pwm.ChangeDutyCycle(50)  # Adjust the duty cycle based on the servo's rotation direction

    def go_right(self):
        self.currentCommand = 2
        self.left_pwm.ChangeDutyCycle(50)  # Adjust the duty cycle based on the servo's rotation direction

    def go_forward(self):
        self.currentCommand = 1
        self.left_pwm.ChangeDutyCycle(50)  # Adjust the duty cycle based on the servo's rotation direction
        self.right_pwm.ChangeDutyCycle(50)  # Adjust the duty cycle based on the servo's rotation direction

    def stop_left_motor(self):
        self.currentCommand = 6
        self.left_pwm.ChangeDutyCycle(0)

    def stop_right_motor(self):
        self.currentCommand = 5
        self.right_pwm.ChangeDutyCycle(0)

    def stop_motors(self):
        self.currentCommand = 0
        self.left_pwm.ChangeDutyCycle(0)
        self.right_pwm.ChangeDutyCycle(0)


    # decides which command to use, given the detection's location
    def decide(self, target, offset=20):
        frame_x = float(target.screen_size_x.data) / 2
        frame_y = float(target.screen_size_y.data)
        
        object_y = float(target.location_y.data)
        object_x = float(target.location_x.data)

        # is_centered = (object_x >= frame_x - offset) and (object_x <= frame_x + offset)
        is_left = object_x < frame_x - offset
        is_right = object_x > frame_x + offset
        is_centered = not is_left and not is_right
        
        print(f"OBJECT CENTER: {object_x} \n FRAME CENTER {frame_x} \n CURRENT COMMAND {self.currentCommand} \n")
        print(f"is_centered: {is_centered} \n is_right {is_right} \n is_left {is_left} \n")

        if is_centered and self.currentCommand != 1:
            print("GO FORWARD \n")
            self.go_forward()
        elif is_left and self.currentCommand != 3:
            print("GO LEFT \n")
            self.go_left()
        elif is_right and self.currentCommand != 2:
            print("GO RIGHT \n")
            self.go_right()
        elif target == None or target == [] and self.currentCommand != 0:
            print("STOP_MOTORS \n")
            self.stop_motors()



