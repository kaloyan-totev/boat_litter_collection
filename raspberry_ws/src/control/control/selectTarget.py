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
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

        self.detections = None
        self.is_target_locked = False
        self.last_locked_target = None
        self.lock_attempts = 5

    def listener_callback(self, msg):
        self.detections = msg.detections
        print(f"\nRECEIVED: {self.detections}\n")
        for d in self.detections:
            print(f"\n{d}\n")
            pass

    def select_target(self, detections=None, trait="conf", preferred_target=None):
        print(f"[select_target] ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
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
        print(f"[/select_target] ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        return Detection()

    def lock_target(self, preferred_target=None):
        self.lock_attempts -= 1
        print(f"[lock_target]=================================================================")
        if preferred_target:
            target = self.select_target(self.detections, preferred_target=preferred_target)
        else:
            target = self.select_target(self.detections)
        print(f"target: {str(target)}")
        if target.confidence.data:
            self.last_locked_target = target
            self.is_target_locked = True
        else:
            self.is_target_locked = False

        print(f"[/lock_target]=================================================================")
        
        
    def timer_callback(self):
        print(f"[timer_callback] ---------------------------------------------------------------{self.detections}")
        msg = self.last_locked_target if self.is_target_locked else Detection()

        if self.detections and not self.is_target_locked:
            self.lock_target()
            msg = self.last_locked_target if self.is_target_locked else Detection()

        elif self.is_target_locked:
            self.lock_target(preferred_target=self.last_locked_target)
            msg = self.last_locked_target if self.is_target_locked else Detection()

        self.publisher_.publish(msg)
        #print(f"\nSENT: {msg}\n")
        #self.get_logger().info('\n Target_select_PUB: "%s" \n' % msg)

        self.lock_attempts = 4 if not self.is_target_locked else 5  # Reset attempts when a target is locked
        print(f"[/timer_callback] ---------------------------------------------------------------")

def main(args=None):
    rclpy.init(args=args)

    target_selector = TargetSelector()

    try:
        rclpy.spin(target_selector)
    except KeyboardInterrupt:
        pass

    target_selector.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
