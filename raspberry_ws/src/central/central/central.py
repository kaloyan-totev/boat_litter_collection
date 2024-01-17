import rclpy
import os
from rclpy.node import Node

from std_msgs.msg import String


class CentralRaspberrySubscriber(Node):

    def __init__(self):
        super().__init__('central_raspberry_subscriber')
        self.subscription = self.create_subscription(
            String,
            'central_jetson_pub',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        #os.system("nmcli device wifi hotspot ssid ros_network password 12345678")
        
    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = CentralRaspberrySubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
