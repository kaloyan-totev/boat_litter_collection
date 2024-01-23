import json
import serial
import time
import threading
import logging
from custom_msgs.msg import Detection
# TODO: decide wether to make the class static

response = None
ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
def flusfhDTR():
    ser.setDTR(False)
    time.sleep(1)
    ser.flushInput()
    ser.setDTR(True)
    time.sleep(2)
    
def read_serial():
    logging.info(f"ARDUINO SAID: {ser.read()}")

class Command:
    def __init__(self):
        flusfhDTR()
        serial_listener_thread = threading.Thread(target=read_serial)
        serial_listener_thread.start()
        pass

    def stop_motors(self):
        ser.write(b'0')
        print(ser.read())


    def go_forward(self):
        self.stop_motors()
        ser.write(b'1')



    def go_right(self):
        self.stop_motors()
        ser.write(b'2')


    def go_left(self):
        self.stop_motors()
        ser.write(b'3')


    # decides which command to use, given the detection's location
    def decide(self,target, offset = 50):

        frame_x = float(target.screen_size_x.data)
        frame_y = float(target.screen_size_y.data)
        
        object_y = float(target.location_y.data)
        object_x = float(target.location_x.data) 
        
        print(f"OBJECT CENTER: {object_x} \n FRAME CENTER {frame_x} \n")

        if(object_x < frame_x - offset):
            print("GO RIGHT \n")
            self.go_right()
        elif(object_x > frame_x + offset):
            print("GO LEFT \n")
            self.go_left()
        elif((object_x >= frame_x - offset) or (object_x <= frame_x + offset)):
            print("GO FORWARD \n")
            self.go_forward()
        else:
            print("STOP_MOTORS \n")
            self.stop_motors
          
          
