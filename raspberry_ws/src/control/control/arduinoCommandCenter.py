import json
import serial
import time
import threading
import logging
from custom_msgs.msg import Detection


response = None
ser = serial.Serial("/dev/ttyACM0", 9600, timeout=0)
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
        self.currentCommand = b''
        pass

    def stop_motors(self):
        ser.write(b'0')
        self.currentCommand = b'0'
        #print(ser.read())
        pass


    def go_forward(self):
        self.stop_motors()
        self.currentCommand = b'1'
        ser.write(b'1')
        #print(ser.read())



    def go_right(self):
        self.stop_motors()
        self.currentCommand = b'2'
        ser.write(b'2')
        #print(ser.read())


    def go_left(self):
        self.stop_motors()
        self.currentCommand = b'3'
        ser.write(b'3')
        #print(ser.read())


    # decides which command to use, given the detection's location
    def decide(self,target, offset = 20):
        frame_x = float(target.screen_size_x.data)/2
        frame_y = float(target.screen_size_y.data)
        
        object_y = float(target.location_y.data)
        object_x = float(target.location_x.data)

        #is_centered = (object_x >= frame_x - offset) and (object_x <= frame_x + offset)
        is_left = object_x < frame_x - offset
        is_right = object_x > frame_x + offset
        is_centered = not is_left and not is_right
        
        print(f"OBJECT CENTER: {object_x} \n FRAME CENTER {frame_x} \n CURRENT COMMAND {self.currentCommand} \n")
        print(f"is_centered: {is_centered} \n is_right {is_right} \n is_left {is_left} \n")

        if( is_centered and self.currentCommand != b'1'):
            print("GO FORWARD \n")
            self.go_forward()
        elif(is_left and self.currentCommand != b'3'):
            print("GO LEFT \n")
            self.go_left()
        elif(is_right and self.currentCommand != b'2'):
            print("GO RIGHT \n")
            self.go_right()
        elif(target == None or target == [] and self.currentCommand != b'0'):
            print("STOP_MOTORS \n")
            self.stop_motors
          
          
