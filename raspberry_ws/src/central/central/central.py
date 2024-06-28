import rclpy
from rclpy.node import Node
from custom_msgs.msg import DetectionsArray
from enum import Enum
from std_msgs.msg import Bool


class CentralRaspberrySubscriber(Node):
    def __init__(self):
        super().__init__('central_raspberry_subscriber')

        # Subscriptions
        self.create_subscription(DetectionsArray, 'central_jetson_pub', self.detections_listener_callback, 10)

        # Publishers
        self.detections_publisher = self.create_publisher(DetectionsArray, 'raspberry_detections_array', 10)
        self.gps_switch_publisher = self.create_publisher(Bool, 'raspberry_gps_follower', 10)

        # Timers
        self.create_timer(0.5, self.timer_callback)
        self.create_timer(0.5, self.line_follow_callback)

        # State variables
        self.detections_msg = None
        self.follow_trajectory = False
        self.JOBS = Enum('JOBS', ['FOLLOW_LINE', 'FOLLOW_OBJECT'])
        self.job = self.JOBS.FOLLOW_LINE

    def detections_listener_callback(self, msg):
        self.detections_msg = msg
        self.job = self.JOBS.FOLLOW_LINE if len(msg.detections) == 0 else self.JOBS.FOLLOW_OBJECT

    # the node is continuously sending the follow_trajectory message to trajectory follower.
    # if the value is true, the robot will be controlled by trajectoryFollower, otherwise the camera.
    def timer_callback(self):
        self.get_logger().debug(f"TIMER CALLBACK JOB = {self.job}")
        if self.job == self.JOBS.FOLLOW_OBJECT and self.detections_msg.detections and len(self.detections_msg.detections) != 0:
            self.follow_trajectory = False
            self.detections_publisher.publish(self.detections_msg)
            self.get_logger().info(f'CENTRAL_PUB CAMERA FOLLOW:\n{len(self.detections_msg.detections) != 0}') #{self.detection_msg}')

        elif self.job == self.JOBS.FOLLOW_LINE:
            self.follow_trajectory = True

    def line_follow_callback(self):
        try:
            self.get_logger().debug("LINE FOLLOW")
            msg = Bool(data=self.follow_trajectory)
            self.gps_switch_publisher.publish(msg)
            self.get_logger().info(f'\nCENTRAL_PUB LINE FOLLOW: {msg.data}\nCENTRAL_PUB CAMERA FOLLOW: {len(self.detections_msg.detections) != 0 }')
        except:
            print("NO DATA")

def main(args=None):
    rclpy.init(args=args)
    node = CentralRaspberrySubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()