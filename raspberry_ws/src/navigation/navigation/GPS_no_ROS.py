from GPSUtil import GPSUtil
import pynmea2
import serial
import os

top_left_point = (42.65585256186259, 27.57744174007652)
top_right_point = (42.655882914489375, 27.577553290251092)
bottom_right_point = (42.655788810269485, 27.577632932122935)
bottom_left_point = (42.65574973707147, 27.577530671961426)
current = (42.65583022937629, 27.5775306523617)
frame = (top_left_point,top_right_point,bottom_right_point,bottom_left_point)

util = GPSUtil(current_location = current  ,frame=frame)

util.adjust_trajectory_to_boundary()
#util.plot_map()
port = "/dev/ttyAMA0"
os.system("sudo chmod 666 /dev/ttyAMA0")
ser = serial.Serial(port, baudrate=9600, timeout=1)
while(True):
    #os.system("sudo chmod 666 /dev/ttyAMA0")
    try:
        newdata = ser.readline()
    except:
        os.system("sudo chmod 666 /dev/ttyAMA0")
        ser = serial.Serial(port, baudrate=9600, timeout=1)
    #print(f"newdata[0:6] : {str(newdata[0:6])}")
    if (newdata[0:6] == b'$GPRMC'):
        print("here")
        msg = str(newdata)+ ""
        msg= str(msg[2:-5])
        try:
            newmsg = pynmea2.parse(str(msg))
            lat = newmsg.latitude
            lng = newmsg.longitude
            gps = f"Latitude= {str(lat)} Longitude= {str(lng)}"
            util.update_current_location((lat, lng))
            util.plot_map()
            print(gps)
        except pynmea2.nmea.ParseError as e:
            print(e)
        
