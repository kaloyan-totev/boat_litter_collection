import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from custom_msgs.msg import DetectionsArray
from custom_msgs.msg import Detection
import json



# subscribes to the detections node and redirects the information to the central publisher

        
class CentralJetsonPublisher(Node):

    def __init__(self):
        super().__init__('central_jetson_publisher')
        
        # Detections PUBLISHER
        self.publisher_ = self.create_publisher(DetectionsArray, 'central_jetson_pub', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        self.detection_msg = None

	# Detections SUBSCRIBER
        self.image_subscription = self.create_subscription(
            DetectionsArray,
            'detections',
            self.listener_callback,
            10)


    def timer_callback(self):
        msg = DetectionsArray()
        print("MESSAGE TYPE: " + str(type(self.detection_msg)))
        if(self.detection_msg != None):
            msg.detections = self.detection_msg
        else:
            det = Detection()
            msg.detections.append(det)


        #msg.data = 'CENTRAL_PUB: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('CENTRAL_PUB: "%s"' % msg)
        self.i += 1



    def listener_callback(self, msg):
        self.get_logger().info('IMAGE_SUB : "%s"' % msg)
        self.detection_msg = msg.detections



def main(args=None):
    rclpy.init(args=args)

    central_publisher = CentralJetsonPublisher()
    rclpy.spin(central_publisher)

    # Destroy the node explicitly
    detecton_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
