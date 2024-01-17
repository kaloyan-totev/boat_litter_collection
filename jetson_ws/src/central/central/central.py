import rclpy
from rclpy.node import Node

from std_msgs.msg import String

import json



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
        self.detection_msg = None

        self.image_subscription = self.create_subscription(
            String,
            'detections',
            self.listener_callback,
            10)


    def timer_callback(self):
        msg = String()
        print(type(self.detection_msg))
        if(self.detection_msg != None):
            msg.data = self.detection_msg

        #msg.data = 'CENTRAL_PUB: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('CENTRAL_PUB: "%s"' % msg.data)
        self.i += 1
        #what():  std::bad_alloc
        #2024-01-16 16:07:54.733 [SUBSCRIBER Error] Deserialization of data failed -> Function deserialize_change

#terminate called after throwing an instance of 'std::bad_alloc'
  #what():  std::bad_alloc


    def listener_callback(self, msg):
        self.get_logger().info('IMAGE_SUB : "%s"' % msg.data)
        self.detection_msg = msg.data



def main(args=None):
    rclpy.init(args=args)

    #detecton_subscriber = DetectionsSubscriber()
    central_publisher = CentralJetsonPublisher()
    #rclpy.spin(detecton_subscriber,)
    rclpy.spin(central_publisher)

    # Destroy the node explicitly
    detecton_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
