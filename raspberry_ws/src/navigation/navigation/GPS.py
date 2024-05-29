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

""" CONNECTING GPS TO RASPBERRY 

pi4              gps
5v               vcc
GND              GND
8(GPIO14)        RX
10(GPIO15)       TX

"""

class Gps(Node):

    def __init__(self):
        super().__init__('gps')
        self.publisher_ = self.create_publisher(String, 'raspberry_gps_stream', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

        self.port = "/dev/serial0"
        self.ser = serial.Serial(self.port, baudrate=9600, timeout=0.5)
        self.dataout = pynmea2.NMEAStreamReader()
        # Set frame points
        top_left_point = (42.727850, 27.608618)
        top_right_point = (42.725266, 27.612694)
        bottom_right_point = (42.722352, 27.608125)
        bottom_left_point = (42.725343, 27.602592)
        example_location = (42.725343, 27.602592)
        frame = (top_left_point, top_right_point, bottom_right_point, bottom_left_point)
        self.util = GPSUtil.get_instance()
        #self.util = GPSUtil.get_instance2(current_location=example_location,frame=frame)
        #prevents trajectory from recalculating every cycle because this way the boat will
        # always be on the trajectory ( when recalculating the boat's current location
        # is almost always the start of the trajectory)
        self.trajectory_is_set = False

        # indicates to which direction the boat is moving
        self.direction_is_left = False
        self.is_moving_vertically = False
        self.last_movement_is_horizontal = False

    #TODO: create action for when requested the map file is sent to the central node
    # and from there to a server
    def timer_callback(self):
        msg = String()

        try:
            if self.ser.in_waiting > 0:
                line = self.ser.readline().decode('ascii', errors='replace').strip()
                if line.startswith('$GPGGA'):
                    self.newmsg = pynmea2.parse(line)
                    lat = self.newmsg.latitude
                    lng = self.newmsg.longitude
                    gps = f"Latitude= {str(lat)} Longitude= {str(lng)}"
                    self.util.update_current_location((lat, lng))
                    self.util.plot_map()
                    print(gps)

                    print(
                        f"Latitude: {self.newmsg.latitude} {self.newmsg.lat_dir}, Longitude: {self.newmsg.longitude} {self.newmsg.lon_dir}, Altitude: {self.newmsg.altitude} {self.newmsg.altitude_units}")
        except pynmea2.ParseError as e:
            print(f"Parse error: {e}")
            gps = str(lat) + "," + str(lng)

            self.util.update_current_location((lat, lng))
            msg.data = gps
        except Exception as e:
            print(f"Error reading GPS data: {e}")

        time.sleep(0.5)

        #self.ser.close()

        self.publisher_.publish(msg)
        if(msg.data): self.get_logger().info('\n\r CENTRAL_PUB: "%s" \n\r' % msg)
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
