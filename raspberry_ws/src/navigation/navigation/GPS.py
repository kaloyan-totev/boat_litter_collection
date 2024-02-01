import serial
import time
import string
import pynmea2
import rclpy
from rclpy.node import Node
from custom_msgs.msg import Detection
from std_msgs.msg import String
from navigation.GPSUtil import GPSUtil


class Gps(Node):

    def __init__(self):
        super().__init__('gps')
        self.publisher_ = self.create_publisher(Detection, 'raspberry_gps', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

        port = "/dev/ttyAMA0"
        self.ser = serial.Serial(port, baudrate=9600, timeout=0.5)
        self.dataout = pynmea2.NMEAStreamReader()
        self.util = GPSUtil()
        # Set frame points
        top_left_point = (42.851781, 27.800468)
        top_right_point = (42.850520, 27.879634)
        bottom_right_point = (42.789835, 27.884055)
        bottom_left_point = (42.801670, 27.790202)
        trajectory_utility.update_frame(top_left_point, top_right_point, bottom_right_point, bottom_left_point)

    def timer_callback(self):
        msg = Detection()

        newdata = self.ser.readline()
        print(f"newdata[0:6] : {newdata[0:6]}")
        if newdata[0:6] == "$GPRMC":
            newmsg = pynmea2.parse(newdata)
            lat = newmsg.latitude
            lng = newmsg.longitude
            gps = "Latitude=" + str(lat) + "and Longitude=" + str(lng)
            self.util.update_current_location((lat, lng))
            print(gps)
        # self.publisher_.publish(msg)
        # self.get_logger().info('\n\r CENTRAL_PUB: "%s" \n\r' % msg)
        # self.i += 1


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
