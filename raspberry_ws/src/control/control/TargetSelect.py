import rclpy
from rclpy.node import Node
from custom_msgs.msg import DetectionsArray
from custom_msgs.msg import Detection

from std_msgs.msg import String

def id_filter(f):
    return f.id

def conf_filter(f):
    return f.confidence

def filter_target(detections, trait="conf"):
    smallest_id = detections.sort(key=id_filter)
    largest_conf_score = detections.sort(key=conf_filter, reverse=True)

    if (trait == "id"):
        return smallest_id[0]
    elif (trait == "conf"):
        return largest_conf_score[0]


def select_target(detections, trait="conf", prefered_target = None):
    # TODO: when real sense is added, make a trait of proximity
    #TODO: check if list is empty

    smallest_id = detections.sort(key=id_filter)
    largest_conf_score = detections.sort(key=conf_filter, reverse=True)

    if(prefered_target != None):
        for item in detections:
            if(item.id == prefered_target.id):
                # if the target is found it is being returned
                return item

    #if a prefered target is not found, a target is returned based on the trait selected
    target = None
    if (trait == "id"):
        target = smallest_id[0]
    elif (trait == "conf"):
        target = largest_conf_score[0]
    return target


class TargetSelect(Node):

    def __init__(self):
        super().__init__('target_selection')
        self.subscription = self.create_subscription(
            DetectionsArray,
            'raspberry_detections_array',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        # Locked detection PUBLISHER
        self.publisher_ = self.create_publisher(Detection, 'locked_target', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
        self.detections = None

        self.is_target_locked = False
        self.last_locked_target = None

    def lock_target(self, prefered_target):
        if(prefered_target):
            self.last_locked_target = select_target(self.detections, prefered_target)
        else:
            self.last_locked_target = select_target(self.detections)

        self.is_target_locked = True

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)

    def timer_callback(self, msg):
        msg = String()
        # TODO: write a cse when a target is being unlocked
        # if there is no locked target
        if (not self.is_target_locked):
            # and there was a locked target
            if (self.last_locked_target != None):
                # try to lock to the previously selected target
                self.lock_target(prefered_target=self.last_locked_target)
            # else select a new target
            else:
                self.lock_target()
            # if locking a target fails
            if (self.is_target_locked == False):
                # TODO: write failure case
                msg = "no target locked"
        # if there is a locked target
        else:

            #TODO: get info of desired target and assign it to message
            msg = self.last_locked_target
        self.publisher_.publish(msg)
        self.get_logger().info('CENTRAL_PUB: "%s"' % msg)
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
