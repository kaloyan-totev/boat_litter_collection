from navigation.GPSUtil import GPSUtil
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import Bool
class TrajectoryFollower:

    def __init__(self):

        super().__init__('gps_follower')
        self.subscription = self.create_subscription(
            bool,
            'raspberry_gps_follower',
            self.image_callback,
            10)
        self.subscription  # prevent unused variable warning

        self.util = GPSUtil(current_location=example_location,frame=frame)
        #prevents trajectory from recalculating every cycle because this way the boat will
        # always be on the trajectory ( when recalculating the boat's current location
        # is almost always the start of the trajectory)
        self.trajectory_is_set = False

        # indicates to which direction the boat is moving
        self.direction_is_left = False
        self.is_moving_vertically = False
        self.last_movement_is_horizontal = False

        # this field changes wether the program is working. it is designed to be changed from the central node
        # when switching between camera and gps
        self.working = False

        self.cmd = Command()


    def follow(self):
        # recalculate new target when arrived at ddestination
        if (util.has_reached_destination):
            distance_to_left = util.distance_between(util.current_location, util.left_boundary)
            distance_to_right = util.distance_between(util.current_location, util.right_boundary)
            # TODO: check if current destination is moving to the left/right or up/down

            # CHANGE DIRECTON
            # current location in near left boundary
            if (distance_to_left <= 5):
                self.direction_is_left = False

            # current location in near right boundary
            elif (distance_to_right <= 5):
                self.direction_is_left = True

            # MOVE HORIZONTALLY OR VERTICALLY
            if (self.last_movement_is_horizontal):
                self.last_movement_is_horizontal = False
                util.adjust_trajectory_to_boundary()
            else:
                self.last_movement_is_horizontal = True
                if (self.direction_is_left):
                    util.move_destination_to_right()
                else:
                    util.move_destination_to_left()
        # following a line
        else:
            command = util.point_position_relative_to_line()
            if (command == "left"):
                print("go_left")
                # self.cmd.go_left

            elif (command == "right"):
                  print("go_right")
                # self.cmd.go_right

            elif (command == "forward"):(
                print("go_forward"))
                # self.cmd.go_forward


    def image_callback(self, msg):
        self.get_logger().info()
        if(self.working):
            follow()














"""import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image

class TrajectoryFollower(Node):

    def __init__(self):
        super().__init__('gps_commands')
        self.subscription = self.create_subscription(
            String,
            'raspberry_gps',
            self.image_callback,
            10)
        self.subscription  # prevent unused variable warning

    def image_callback(self, msg):
        self.get_logger().info()


def main(args=None):
    rclpy.init(args=args)
    image_subscriber = ImageSubscriber()
    rclpy.spin(image_subscriber)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
"""