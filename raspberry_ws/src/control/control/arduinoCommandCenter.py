import json
import serial
import time



response = None
ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
def flusfhDTR():
    ser.setDTR(False)
    time.sleep(1)
    ser.flushInput()
    ser.setDTR(True)
    time.sleep(2)
class Command:
    def __init__(self):
        flusfhDTR()
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
    def decide(self,json_input, offset = 50):
        data = json.load(json_input)
        frame = data["screen_size"]
        object_centerpoint = data["location"]

        if(object_centerpoint[0] < frame[0] - offset):
            self.go_right()
        elif(object_centerpoint[0] > frame[0] + offset):
            self.go_left()
        else:
            self.go_forward()
