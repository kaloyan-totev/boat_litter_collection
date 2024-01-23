import rclpy
from rclpy.node import Node
from custom_msgs.msg import Detection
from std_msgs.msg import String

from control.arduinoCommandCenter import Command

class MotorControl(Node):

    def __init__(self):
        super().__init__('motor_control')
        self.subscription = self.create_subscription(
            Detection,
            'locked_target',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.cmd = Command()



    def listener_callback(self, msg):
        self.cmd.decide(Detection())
        self.get_logger().info('I heard: "%s"' % msg.name)




def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = MotorControl()
    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
