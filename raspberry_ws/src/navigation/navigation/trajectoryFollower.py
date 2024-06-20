from navigation.GPSUtil import GPSUtil
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import Bool
from std_msgs.msg import String
from control.motorCommandCenter import Command
import time
class TrajectoryFollower(Node):

    def __init__(self):

        super().__init__('gps_follower')
        self.subscription = self.create_subscription(
            Bool,
            'raspberry_gps_follower',
            self.image_callback,
            10)
        self.subscription  # prevent unused variable warning

        self.gps_stream_subscription = self.create_subscription(
            String,
            'raspberry_gps_stream',
            self.gps_stream_callback,
            10)
        self.gps_stream_subscription  # prevent unused variable warning

        top_left_point = (42.727850, 27.608618)
        top_right_point = (42.725266, 27.612694)
        bottom_right_point = (42.722352, 27.608125)
        bottom_left_point = (42.725343, 27.602592)
        example_location = (42.725343, 27.602592)
        frame = (top_left_point, top_right_point, bottom_right_point, bottom_left_point)

        self.util = GPSUtil.get_instance()
        #prevents trajectory from recalculating every cycle because this way the boat will
        # always be on the trajectory ( when recalculating the boat's current location
        # is almost always the start of the trajectory)
        self.trajectory_is_set = False

        # indicates to which direction the boat is moving
        self.direction_is_left = False
        self.is_moving_vertically = False
        self.last_movement_is_horizontal = False

        # this field changes weather the program is working. it is designed to
        # be changed from the central node when switching between camera and gps
        self.working = False
        # as the callback executes too often, this field indicates if the
        #  follow function has finishedbefore starting anew
        self.follow_func_locked = False
        self.cmd = Command()

# this function is called upon each tick
    def follow(self):
        # locks command control on gps
        self.follow_func_locked = True
        if (self.util.has_reached_destination()):
            distance_to_left = self.util.distance_point_to_line(self.util.current_location,
                                                                (self.util.left_boundary.locations[0],
                                                                self.util.left_boundary.locations[1]))

            distance_to_right = self.util.distance_point_to_line(self.util.current_location,
                                                                 (self.util.right_boundary.locations[0],
                                                                 self.util.right_boundary.locations[1]))
            # TODO: check if current destination is moving to the left/right or up/down
            print(f"[follower(follow)] distance to left:{distance_to_left}, distance to right:{distance_to_right}")
            # CHANGE DIRECTION
            # as the function is being called constantly by the timer's ticks, it is checking
            # if the current location is near a border of a frame. The boat is designed to move from
            # left to right, drawing a zig-zag line across the frame. When the current location
            # approaches the left or right border of the frame, this means that the direction of traversal
            # needs to be changed

            # current location is near left boundary
            if (distance_to_left <= 5):
                print("[follower(follow)] direction changed to right")
                self.direction_is_left = False

            # current location in near right boundary
            elif (distance_to_right <= 5):
                print("[follower(follow)] direction changed to left")
                self.direction_is_left = True

            # MOVE HORIZONTALLY OR VERTICALLY
            # when the destination point is reached, the new destination point needs to be calculated.
            #in case the boat has last moved vertically, it means the next destination
            # needs to be 5 meters to the left/right. In the oposite case it means that the last action
            # has been to move the boat 5 meters and now the destination needs to be moved
            # to the opposite boundary of the frame

            if (self.last_movement_is_horizontal):
                self.last_movement_is_horizontal = False
                self.util.adjust_trajectory_to_boundary()
            else:
                self.last_movement_is_horizontal = True
                if (self.direction_is_left):
                    self.util.move_destination_to_right()
                else:
                    self.util.move_destination_to_left()
        # following a line
        else:
            command = self.util.point_position_relative_to_line()
            if (command == "left"):
                print("[follower(follow)] go_left")
                self.cmd.go_left

            elif (command == "right"):
                  print("[follower(follow)] go_right")
                  self.cmd.go_right

            elif (command == "forward"):
                  print("[follower(follow)] go_forward")
                  self.cmd.go_forward

        self.follow_func_locked = False


    def image_callback(self, msg):
        if(msg.data):
            self.working = msg.data
        if(self.working and not self.follow_func_locked):
            self.follow()

    def gps_stream_callback(self, msg):
        self.gps_stream = msg


def main(args=None):
    rclpy.init(args=args)
    switch_subscriber = TrajectoryFollower()
    rclpy.spin(switch_subscriber)
    rclpy.shutdown()


if __name__ == '__main__':
    main()

