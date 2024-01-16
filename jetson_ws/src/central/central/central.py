import rclpy
from rclpy.node import Node

from std_msgs.msg import String

detection_msg = String()

# subscribes to the detections node and redirects the information to the central publisher
class DetectionsSubscriber(Node):

    def __init__(self):
        super().__init__('central_detection_subscriber')
        self.image_subscription = self.create_subscription(
            String,
            'detections',
            self.listener_callback,
            10)
        self.image_subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('IMAGE_SUB : "%s"' % msg.data)
        detection_msg = msg.data

        
class CentralJetsonPublisher(Node):

    def __init__(self):
        super().__init__('central_jetson_publisher')
        self.publisher_ = self.create_publisher(String, 'central_jetson_pub', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg = detection_msg
        msg.data = 'CENTRAL_PUB: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('CENTRAL_PUB: "%s"' % msg.data)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    detecton_subscriber = DetectionsSubscriber()
    central_publisher = CentralJetsonPublisher()
    rclpy.spin(detecton_subscriber)

    # Destroy the node explicitly
    detecton_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
