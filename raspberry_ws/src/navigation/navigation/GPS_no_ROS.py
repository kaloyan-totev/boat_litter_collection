from GPSUtil import GPSUtil
import pynmea2
import serial
import os
from getkey import getkey
import time

top_left_point = (42.65535256186259, 27.57724174007652)
top_right_point = (42.655682914489375, 27.577353290251092)
bottom_right_point = (42.655988810269485, 27.577932932122935)
bottom_left_point = (42.65594973707147, 27.577930671961426)
current = (42.65583022937629, 27.5775306523617)
frame = (top_left_point,top_right_point,bottom_right_point,bottom_left_point)
auto_current_location = False
follow_func_locked = False

util = GPSUtil.get_instance()
util = GPSUtil.get_instance2(current_location = current  ,frame=frame)

util.adjust_trajectory_to_boundary()
#util.plot_map()
port = "/dev/ttyAMA0"
os.system("sudo chmod 666 /dev/ttyAMA0")
ser = serial.Serial(port, baudrate=9600, timeout=1)

def follow():
        follow_func_locked = True
        # recalculate new target when arrived at destination
        if (util.has_reached_destination()):
            print("IF:")
            distance_to_left = util.distance_point_to_line(util.current_location, util.left_boundary.locations[0], util.left_boundary.locations[1])
            distance_to_right = self.util.distance_point_to_line(util.current_location, util.right_boundary.locations[0], util.right_boundary.locations[1])
            # TODO: check if current destination is moving to the left/right or up/down
            print(f"distance to left:{distance_to_left}, distance to right:{distance_to_right}")
            # CHANGE DIRECTON
            # current location in near left boundary
            if (distance_to_left <= 5):
                print("direction changed to right")
                direction_is_left = False

            # current location in near right boundary
            elif (distance_to_right <= 5):
                print("direction changed to left")
                direction_is_left = True

            # MOVE HORIZONTALLY OR VERTICALLY
            if (last_movement_is_horizontal):
                last_movement_is_horizontal = False
                util.adjust_trajectory_to_boundary()
            else:
                last_movement_is_horizontal = True
                if (direction_is_left):
                    util.move_destination_to_right()
                else:
                    util.move_destination_to_left()
        # following a line
        else:
            print("ELSE:")
            command = util.point_position_relative_to_line()
            if (command == "left"):
                print("go_right")
                # self.cmd.go_left

            elif (command == "right"):
                  print("go_left")
                # self.cmd.go_right

            elif (command == "forward"):(
                print("go_forward"))
                # self.cmd.go_forward

        follow_func_locked = False
while(True):
    key_pressed = getkey(blocking=False)
    try:
        
        time.sleep(0.1)
    except KeyboardInterrupt as e:
        option = int(input("choose an option:\n0. exit\n1. change current location\n2. change destinaton\n3. change start\n 4. activate auto current location \n"))
        
        match option:
        	case 0:
        		exit()
       		case 1:
       			new_lon = float(input("please enter the new longitute"))
       			new_lat = float(input("please enter the new latitude"))
       			util.update_current_location((new_lon,new_lat))
       			auto_current_location = False
       		case 4:
       			auto_current_location = True
    
    print("loop")
    if key_pressed == "q":
        option = int(input("choose an option:\n1. change current location\n2. change destinaton\n3. change start"))
    #os.system("sudo chmod 666 /dev/ttyAMA0")
    try:
        newdata = ser.readline()
    except:
        os.system("sudo chmod 666 /dev/ttyAMA0")
        ser = serial.Serial(port, baudrate=9600, timeout=1)
    print(f"newdata[0:6] : {str(newdata[0:6])}")
    if (newdata[0:6] == b'$GPRMC'):
        print("here")
        msg = str(newdata)+ ""
        msg= str(msg[2:-5])
        print(msg)
        try:
            newmsg = pynmea2.parse(str(msg))
            lat = newmsg.latitude
            lng = newmsg.longitude
            gps = f"Latitude= {str(lat)} Longitude= {str(lng)}"
            if(auto_current_location):
                util.update_current_location((lat, lng))
            util.plot_map()
            follow()
            print(gps)
        except pynmea2.nmea.ParseError as e:
            print(e)
            
    
       
        
