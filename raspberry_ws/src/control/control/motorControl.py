import rclpy
from rclpy.node import Node
from custom_msgs.msg import Detection
from std_msgs.msg import String
import RPi.GPIO as GPIO
from control.motorCommandCenter import Command

class MotorControl(Node):

    def __init__(self):
        super().__init__('camera_motor_controller')
        self.subscription = self.create_subscription(
            Detection,
            'locked_target',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.cmd = Command()

    def listener_callback(self, msg):
        if(msg != None and msg != [] and msg.id.data != 0.0):
            self.cmd.decide(msg)
        self.get_logger().info('I heard: "%s"' % msg.name)

def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = MotorControl()
    try:
        rclpy.spin(minimal_subscriber)
    except KeyboardInterrupt:
        pass
    finally:
        minimal_subscriber.destroy_node()
        rclpy.shutdown()
        GPIO.cleanup()
        print("GPIO cleaned")

if __name__ == '__main__':
    main()
