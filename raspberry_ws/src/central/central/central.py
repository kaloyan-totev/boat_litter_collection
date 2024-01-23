import rclpy
from rclpy.node import Node
from custom_msgs.msg import DetectionsArray
from custom_msgs.msg import Detection


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

        # Locked detection PUBLISHER
        self.publisher_ = self.create_publisher(DetectionsArray, 'raspberry_detections_array', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        self.detection_msg = None
        
    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)

    def timer_callback(self, msg):
        msg = DetectionsArray()
        print("MESSAGE TYPE: " + str(type(self.detection_msg)))
        if (self.detection_msg != None):
            msg.detections = self.detection_msg

        # msg.data = 'CENTRAL_PUB: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('CENTRAL_PUB: "%s"' % msg)
        self.i += 1


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
