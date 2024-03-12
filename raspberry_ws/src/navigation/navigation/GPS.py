import serial
import time
import string
import pynmea2
import rclpy
from rclpy.node import Node
from custom_msgs.msg import Detection
from std_msgs.msg import String
from navigation.GPSUtil import GPSUtil
from control.arduinoCommandCenter import Command
import os


class Gps(Node):

    def __init__(self):
        super().__init__('gps')
        self.publisher_ = self.create_publisher(String, 'raspberry_gps', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

        os.system("sudo chmod 666 /dev/ttyAMA0")
        port = "/dev/ttyAMA0"
        self.ser = serial.Serial(port, baudrate=9600, timeout=0.5)
        self.dataout = pynmea2.NMEAStreamReader()
        # Set frame points
        top_left_point = (42.727850, 27.608618)
        top_right_point = (42.725266, 27.612694)
        bottom_right_point = (42.722352, 27.608125)
        bottom_left_point = (42.725343, 27.602592)
        example_location = (42.725343, 27.602592)
        frame = (top_left_point, top_right_point, bottom_right_point, bottom_left_point)
        self.util = GPSUtil(current_location=example_location,frame=frame)
        #prevents trajectory from recalculating every cycle because this way the boat will
        # always be on the trajectory ( when recalculating the boat's current location
        # is almost always the start of the trajectory)
        self.trajectory_is_set = False

        # indicates to which direction the boat is moving
        self.direction_is_left = False
        self.is_moving_vertically = False
        self.last_movement_is_horizontal = False

        self.cmd = Command()


    #TODO: create action for when requested the map file is sent to the central node
    # and from there to a server
    def timer_callback(self):
        msg = String()
        newdata = ""
        try:
            newdata = self.ser.readline()
        except:
            os.system("sudo chmod 666 /dev/ttyAMA0")
        print(f"newdata[0:6] : {newdata[0:6]}")
        if newdata[0:6] == "$GPRMC":
            newmsg = pynmea2.parse(newdata)
            lat = newmsg.latitude
            lng = newmsg.longitude
            gps = "Latitude=" + str(lat) + "and Longitude=" + str(lng)
            print(gps)
            gps = str(lat) + "," + str(lng)

            self.util.update_current_location((lat, lng))
            msg.data = gps

        """
        #recalculate new target when arrived at ddestination
        if(util.has_reached_destination):
            distance_to_left = util.distance_between(util.current_location, util.left_boundary)
            distance_to_right = util.distance_between(util.current_location, util.right_boundary)
            #TODO: check if current destination is moving to the left/right or up/down

            # CHANGE DIRECTON
            #current location in near left boundary
            if(distance_to_left <= 5):
                self.direction_is_left = False

            #current location in near right boundary
            elif(distance_to_right <=5):
                self.direction_is_left = True

            # MOVE HORIZONTALLY OR VERTICALLY
            if(self.last_movement_is_horizontal):
                self.last_movement_is_horizontal = False
                util.adjust_trajectory_to_boundary()
            else:
                self.last_movement_is_horizontal = True
                if(self.direction_is_left):
                    util.move_destination_to_right()
                else:
                    util.move_destination_to_left()
        #following a line
        else:
            msg = util.point_position_relative_to_line()
            if(util.point_position_relative_to_line() == "left"):
                #go_left
                #self.cmd.go_left
                pass
            elif(util.point_position_relative_to_line() == "right"):
                #go_right
                #self.cmd.go_right
                pass
            elif(util.point_position_relative_to_line() == "forward"):
                #go_forward
                #self.cmd.go_forward
                pass
"""
        self.publisher_.publish(msg)
        self.get_logger().info('\n\r CENTRAL_PUB: "%s" \n\r' % msg)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = Gps()
    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
