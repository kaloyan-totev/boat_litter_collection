import rclpy
from rclpy.node import Node
from custom_msgs.msg import Detection
from std_msgs.msg import String
import RPi.GPIO as GPIO
from control.motorCommandCenter import Command

class MotorControl(Node):

    def __init__(self):
        super().__init__('camera_motor_controller')
        self.camera_subscription = self.create_subscription(
            Detection,
            'locked_target',
            self.target_listener_callback,
            10)

        self.gps_subscription = self.create_subscription(
            String,
            'trajectory_follower_command',
            self.gps_listener_callback,
            10)

        self.switch_subscription = self.create_subscription(
            String,
            'follower_switch',
            self.switch_listener_callback,
            10)

        self.subscription  # prevent unused variable warning
        self.cmd = Command()
        self.current_command = "STOP"
        self.current_follower = "gps"

    def target_listener_callback(self, msg):
        if(self.current_follower == "camera"):
            if(msg != None and msg != [] and msg.id.data != 0.0):
                self.current_command = self.cmd.decide(msg)

            if (self.current_command == "GO FORWARD"):
                self.cmd.go_forward
            elif (self.current_command == "GO LEFT"):
                self.cmd.go_left
            elif (self.current_command == "GO RIGHT"):
                self.cmd.go_right
            elif (self.current_command == "STOP"):
                self.cmd.stop_motors
            self.get_logger().info('I heard: "%s"' % msg.name)

    def gps_listener_callback(self, msg):
        if(self.current_follower == "gps"):
            if(msg.data == "GO FORWARD"):
                self.cmd.go_forward
            elif(msg.data == "GO LEFT"):
                self.cmd.go_left
            elif(msg.data == "GO RIGHT"):
                self.cmd.go_right
            elif(msg.data == "STOP"):
                self.cmd.stop_motors

    def switch_listener_callback(self,msg):
        self.current_follower = msg.data

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
