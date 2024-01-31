import serial
import time
import string
import pynmea2
import rclpy
from rclpy.node import Node
from custom_msgs.msg import Detection
from std_msgs.msg import String


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


    def timer_callback(self):
        msg = Detection()

        newdata = self.ser.readline()
        print(f"newdata[0:6] : {newdata[0:6]}")
        if newdata[0:6] == "$GPRMC":
            newmsg = pynmea2.parse(newdata)
            lat = newmsg.latitude
            lng = newmsg.longitude
            gps = "Latitude=" + str(lat) + "and Longitude=" + str(lng)
            print(gps)
        #self.publisher_.publish(msg)
        #self.get_logger().info('\n\r CENTRAL_PUB: "%s" \n\r' % msg)
        #self.i += 1




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
