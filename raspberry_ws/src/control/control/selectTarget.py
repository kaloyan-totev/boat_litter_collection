import rclpy
from rclpy.node import Node
from custom_msgs.msg import DetectionsArray, Detection


class TargetSelector(Node):
    def __init__(self):
        super().__init__('target_selection')
        self.subscription = self.create_subscription(
            DetectionsArray,
            'raspberry_detections_array',
            self.listener_callback,
            10)
        self.publisher_ = self.create_publisher(Detection, 'locked_target', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.detections = None
        self.is_target_locked = False
        self.last_locked_target = None
        self.lock_attempts = 5

    def listener_callback(self, msg):
        self.detections = msg.detections

    def select_target(self, detections=None, trait="conf", preferred_target=None):
        if not detections or not detections[0].confidence.data:
            return Detection()

        if preferred_target and preferred_target.confidence.data:
            for item in detections:
                if item.id.data == preferred_target.id.data:
                    return item

        if trait == "id":
            return min(detections, key=lambda x: int(x.id.data))
        elif trait == "conf":
            return max(detections, key=lambda x: float(x.confidence.data))

        return Detection()

    def lock_target(self, preferred_target=None):
        self.lock_attempts -= 1
        target = self.select_target(self.detections, preferred_target=preferred_target)

        if target.confidence.data:
            self.last_locked_target = target
            self.is_target_locked = True
        else:
            self.is_target_locked = False

    def timer_callback(self):
        if self.detections:
            if not self.is_target_locked:
                self.lock_target()
            else:
                self.lock_target(preferred_target=self.last_locked_target)

        msg = self.last_locked_target if self.is_target_locked else Detection()
        self.publisher_.publish(msg)

        # self.get_logger().info(f'Target_select_PUB: {msg}')

        self.lock_attempts = 5 if self.is_target_locked else 4


def main(args=None):
    rclpy.init(args=args)
    target_selector = TargetSelector()
    try:
        rclpy.spin(target_selector)
    except KeyboardInterrupt:
        pass
    finally:
        target_selector.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()