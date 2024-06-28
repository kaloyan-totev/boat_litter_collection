import rclpy
from rclpy.node import Node
from custom_msgs.msg import DetectionsArray
from enum import Enum
from std_msgs.msg import Bool, String


class CentralRaspberryNode(Node):
    def __init__(self):
        super().__init__('central_raspberry_subscriber')

        # Subscriptions
        self.create_subscription(DetectionsArray, 'central_jetson_pub', self.detections_listener_callback, 10)

        # Publishers
        self.detections_publisher = self.create_publisher(DetectionsArray, 'raspberry_detections_array', 10)
        self.gps_publisher = self.create_publisher(Bool, 'raspberry_gps_follower', 10)
        self.switch_publisher = self.create_publisher(String, 'follower_switch', 10)

        # Timers
        self.create_timer(0.2, self.timer_callback)
        self.create_timer(0.2, self.line_follow_callback)
        self.create_timer(0.2, self.switch_follower_callback)

        # State variables
        self.detections_msg = None
        self.follow_trajectory = False


    def detections_listener_callback(self, msg):
        self.detections_msg = msg




    # the node is continuously sending the follow_trajectory message to trajectory follower.
    # if the value is true, the robot will be controlled by trajectoryFollower, otherwise the camera.
    def timer_callback(self):

        if self.detections_msg and len(self.detections_msg.detections) != 0 and self.detections_msg.detections[0].name.data != "dummy":
            self.follow_trajectory = False
            self.detections_publisher.publish(self.detections_msg)
        else:
            self.follow_trajectory = True
        print(f"FOLLOW TRAJECTORY: {self.follow_trajectory}")

    def line_follow_callback(self):
        try:
            self.get_logger().debug("LINE FOLLOW")
            msg = Bool(data=self.follow_trajectory)
            self.gps_publisher.publish(msg)
            self.get_logger().info(f'\nCENTRAL_PUB LINE FOLLOW: {msg.data}'
                                   f'\nCENTRAL_PUB CAMERA FOLLOW: {len(self.detections_msg.detections) != 0 and self.detections_msg.detections[0].name.data != "dummy" }')
        except:
            print("NO DATA")

    def switch_follower_callback(self):
        msg = String()
        try:
            if self.follow_trajectory:
                msg.data = "gps"
            else:
                msg.data = "camera"

            self.switch_publisher.publish(msg)
        except:
            print("ERROR")
def main(args=None):
    rclpy.init(args=args)
    node = CentralRaspberryNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()