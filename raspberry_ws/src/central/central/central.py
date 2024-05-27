import rclpy
from rclpy.node import Node
from custom_msgs.msg import DetectionsArray
from custom_msgs.msg import Detection
from enum import Enum
from std_msgs.msg import String
from std_msgs.msg import Bool


class CentralRaspberrySubscriber(Node):

    def __init__(self):
        super().__init__('central_raspberry_subscriber')
        self.subscription = self.create_subscription(
            DetectionsArray,
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
        
        # the node is continuously sending the follow_trajectory to the trajectory follower.
        # if the value is true, the robot will be controlled byh trajectoryFollower, otherwise the camera.
        self.gps_switch_publisher = self.create_publisher(Bool, 'raspberry_gps_follower', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.line_follow_callback)
        self.i = 0
        self.follow_trajectory = False

        self.JOBS = Enum('JOBS',['FOLLOW_LINE','FOLLOW_OBJECT'])
        self.job = self.JOBS.FOLLOW_LINE
        
    def listener_callback(self, msg):
        self.detection_msg = msg

        #trying to check if detections is empty string (NOT TRIED)
        if(msg == DetectionsArray()):
            self.job = self.JOBS.FOLLOW_OBJECT #FOLLOW_LINE
        else:
            self.job = self.JOBS.FOLLOW_OBJECT
        #self.get_logger().info('I heard: "%s"' % msg)

    def timer_callback(self):
        print(f"TIMER CALLBACK JOB = {self.job}")
        if(self.job == self.JOBS.FOLLOW_OBJECT):
            msg = DetectionsArray()
            self.follow_trajectory = False
            print("MESSAGE TYPE: " + str(type(self.detection_msg)))
            if (self.detection_msg != None):
                msg = self.detection_msg

            # msg.data = 'CENTRAL_PUB: %d' % self.i
            self.publisher_.publish(msg)
            self.get_logger().info('\n\r CENTRAL_PUB CAMERA FOLLOW: "%s" \n\r' % msg)
            self.i += 1
        elif(self.job == self.JOBS.FOLLOW_LINE):
            self.follow_trajectory = True

    def line_follow_callback(self):
        print("LINE FOLLOW")
        msg = Bool()
        msg.data = self.follow_trajectory
        self.gps_switch_publisher.publish(msg)
        self.get_logger().info('\n\r CENTRAL_PUB LINE FOLLOW: "%s" \n\r' % msg)
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
