import time
import RPi.GPIO as GPIO
#from control.right_motor import set_throttle_right
#from control.left_motor import set_throttle_left

class Command:
    def __init__(self):
        # Define servo pins
        self.left_motor_pin = 19
        self.right_motor_pin = 13
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.left_motor_pin, GPIO.OUT)
        GPIO.setup(self.right_motor_pin, GPIO.OUT)

        # Initialize PWM
        self.left_pwm = GPIO.PWM(self.left_motor_pin, 50)
        self.right_pwm = GPIO.PWM(self.right_motor_pin, 50)
        self.left_pwm.start(0)
        self.right_pwm.start(0)

        # Define servo angles
        self.zero_speed = 90  # 0 degree position for servo
        self.max_speed = 120  # Maximum duty cycle for maximum speed
        self.min_speed = 60  # Minimum duty cycle for minimum speed
        
        self.currentCommand = 0

    def set_throttle_left(self,throttle,pin=0):
        duty = throttle / 18 + 2
        #GPIO.output(pin, True)
        self.left_pwm.ChangeDutyCycle(duty)
        time.sleep(0.1)
    def set_throttle_right(self,throttle,pin=0):
        duty = throttle / 18 + 2
        #GPIO.output(pin, True)
        self.right_pwm.ChangeDutyCycle(duty)
        time.sleep(0.1)
        
    def go_left(self):
        self.currentCommand = 3
        self.set_throttle_right(self.max_speed)

    def go_right(self):
        self.currentCommand = 2
        self.set_throttle_left(self.max_speed)

    def go_forward(self):
        self.currentCommand = 1
        self.set_throttle_left(self.max_speed)
        self.set_throttle_right(self.max_speed)


    def stop_left_motor(self):
        self.currentCommand = 6
        self.set_throttle_left(self.zero_speed)

    def stop_right_motor(self):
        self.currentCommand = 5
        self.set_throttle_right(self.zero_speed)

    def stop_motors(self):
        self.currentCommand = 0
        self.set_throttle_left(self.zero_speed)
        self.set_throttle_right(self.zero_speed)


    # decides which command to use, given the detection's location
    def decide(self, target, offset=20):
    
        if target is None or target == []:
            print(f"STOP MOTORS target = {target}")
            time.sleep(10)
            self.stop_motors()
            return

        frame_x = float(target.screen_size_x.data) / 2
        object_x = float(target.location_x.data)

        is_left = object_x < frame_x - offset
        is_right = object_x > frame_x + offset
        is_centered = not is_left and not is_right
        
        print(f"OBJECT CENTER: {object_x} \n FRAME CENTER {frame_x} \n CURRENT COMMAND {self.currentCommand} \n")
        print(f"is_centered: {is_centered} \n is_right {is_right} \n is_left {is_left} \n")
        
        if is_centered and self.currentCommand != 1:
            print("GO FORWARD")
            self.go_forward()
        elif is_left and self.currentCommand != 3:
            print("GO LEFT")
            self.go_left()
        elif is_right and self.currentCommand != 2:
            print("GO RIGHT")
            self.go_right()
        elif self.currentCommand != 0 and not is_centered and not is_left and not is_right:
            print("STOP MOTORS")
            self.stop_motors()
        #del self.left_pwm
        #del self.right_pwm

