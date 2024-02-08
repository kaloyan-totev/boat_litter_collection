import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image

class TrajectoryFollower(Node):

    def __init__(self):
        super().__init__('gps_commands')
        self.subscription = self.create_subscription(
            Image,
            'central_gps_commands',
            self.image_callback,
            10)
        self.subscription  # prevent unused variable warning

    def image_callback(self, msg):
        self.get_logger().info('Received image with height %d and width %d' % (msg.height, msg.width))


def main(args=None):
    rclpy.init(args=args)
    image_subscriber = ImageSubscriber()
    rclpy.spin(image_subscriber)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
