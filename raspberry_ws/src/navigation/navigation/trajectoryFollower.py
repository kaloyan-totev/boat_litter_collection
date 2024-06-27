import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import Bool, String
from control.motorCommandCenter import Command
from navigation.GPSUtil import GPSUtil


class TrajectoryFollower(Node):
    def __init__(self):
        super().__init__('gps_motor_controller')

        self.create_subscription(Bool, 'raspberry_gps_follower', self.image_callback, 10)
        self.create_subscription(String, 'raspberry_gps_stream', self.gps_stream_callback, 10)

        self.util = GPSUtil.get_instance()
        self.cmd = Command()

        self.trajectory_is_set = False
        self.direction_is_left = False
        self.is_moving_vertically = False
        self.last_movement_is_horizontal = False
        self.working = False
        self.follow_func_locked = False

    def follow(self):
        self.follow_func_locked = True
        try:
            if self.util.has_reached_destination():
                self._handle_destination_reached()
            else:
                self._follow_trajectory()
        finally:
            self.follow_func_locked = False

    def _handle_destination_reached(self):
        distance_to_left = self.util.distance_point_to_line(
            self.util.current_location,
            (self.util.left_boundary.locations[0], self.util.left_boundary.locations[1])
        )
        distance_to_right = self.util.distance_point_to_line(
            self.util.current_location,
            (self.util.right_boundary.locations[0], self.util.right_boundary.locations[1])
        )

        self.get_logger().info(f"Distance to left: {distance_to_left}, Distance to right: {distance_to_right}")

        self._update_direction(distance_to_left, distance_to_right)
        self._update_trajectory()

    def _update_direction(self, distance_to_left, distance_to_right):
        if distance_to_left <= 5:
            self.direction_is_left = False
            self.get_logger().info("Direction changed to right")
        elif distance_to_right <= 5:
            self.direction_is_left = True
            self.get_logger().info("Direction changed to left")

    def _update_trajectory(self):
        if self.last_movement_is_horizontal:
            self.last_movement_is_horizontal = False
            self.util.adjust_trajectory_to_boundary()
        else:
            self.last_movement_is_horizontal = True
            if self.direction_is_left:
                self.util.move_destination_to_right()
            else:
                self.util.move_destination_to_left()

    def _follow_trajectory(self):
        command = self.util.point_position_relative_to_line()
        if command == "left":
            self.get_logger().info("Going left")
            self.cmd.go_left()
        elif command == "right":
            self.get_logger().info("Going right")
            self.cmd.go_right()
        elif command == "forward":
            self.get_logger().info("Going forward")
            self.cmd.go_forward()

    def image_callback(self, msg):
        self.get_logger().info(f"Following GPS data: {msg.data}, Following camera data: {not msg.data}")
        self.working = msg.data
        if self.working and not self.follow_func_locked:
            self.follow()

    def gps_stream_callback(self, msg):
        self.gps_stream = msg.data


def main(args=None):
    rclpy.init(args=args)
    trajectory_follower = TrajectoryFollower()
    try:
        rclpy.spin(trajectory_follower)
    except KeyboardInterrupt:
        pass
    finally:
        trajectory_follower.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()