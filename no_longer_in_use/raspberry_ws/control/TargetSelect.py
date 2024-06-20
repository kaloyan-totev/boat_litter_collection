import rclpy
from rclpy.node import Node
from custom_msgs.msg import DetectionsArray
from custom_msgs.msg import Detection
import json
from std_msgs.msg import String

def id_filter(d):
    print(f"[id_filter] : {int(d.id.data)}")
    return d.id.data

def conf_filter(d):
    print(f"[conf_filter] : {float(d.confidence.data)}")
    return float(d.confidence.data)

def filter_target(detections, trait="conf"):
    if (trait == "id"):
        smallest_id = detections.sort(key=id_filter)
        return smallest_id[0]
    elif (trait == "conf"):
        largest_conf_score = detections.sort(key=conf_filter, reverse=True)
        return largest_conf_score[0]





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
        self.lock_attempts = 5

    def select_target(self,detections = (0,0), trait="conf", prefered_target = Detection()):
        if(detections != (0,0) and detections != None and len(detections) > 0 and detections[0].confidence.data != 0.0 ):
            if(self.last_locked_target):
                prefered_target = self.last_locked_target
            print("[select_target]====================================================================================")
            print(prefered_target)
            # TODO: when real sense is added, make a trait of proximity

            target = Detection()
            smallest_id = detections
            smallest_id.sort(key=id_filter)
            largest_conf_score = detections
            largest_conf_score.sort(key=conf_filter, reverse=True)
            print(f"\n[select_target] largest_conf_score: {largest_conf_score} \n")
            print(f"\n[select_target] smallest_id: {smallest_id} \n")

            print(f"CONF: {prefered_target.confidence.data}")
            # assert that the data is not a dummy data an an actual detection
            if( prefered_target.confidence.data != 0.0):
                print(f"\n[select_target] DATA IS NOT DUMMY \n")
                for item in detections:
                    print(f"\n[select_target] detections id: {item.id.data} : {prefered_target.id.data} :preffered id\n")
                    if(item.id.data == prefered_target.id.data):
                        # if the target is found it is being returned
                        target = item
            else:
            #if a prefered target is not found or specified, a target is returned based on the trait selected
                if (trait == "id"):
                    target = smallest_id[0]
                    print(f"\n[select_target] target selected by id: {target} \n")
                elif (trait == "conf"):
                    target = largest_conf_score[0]
                    print(f"\n[select_target] target selected by conf: {target} \n")
            print(f"\n[select_target] target returned: {target} \n")
            print("[/select_target]====================================================================================")
            return target

    def lock_target(self, prefered_target = []):
        self.lock_attempts -= 1
        #TODO:
        print("[lock_target]+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        if(prefered_target):
            print("lock to prefered target")
            target = self.select_target(self.detections, prefered_target)
        else:
            print("lock to any target")
            target = self.select_target(self.detections)
        if(target != None and target != [] and target.confidence.data != 0.0):
            self.last_locked_target = target
            self.is_target_locked = True
        else:
            self.is_target_locked = False
            pass


        print(f"\n[lock_target] locked target: {self.last_locked_target}\n")
        print("[/lock_target]+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    def listener_callback(self, msg):
        self.detections = msg.detections
        #self.get_logger().info('\n I heard: "%s" \n' % msg)
        pass

    def timer_callback(self):
        msg = Detection()
        # TODO: write a cse when a target is being unlocked
        # if there is no locked target
        print(f" are detections available: {self.detections != None and self.detections != []}")

        if(self.detections != None and self.detections != []):
            print(f"detections available: {self.detections}")
            if (not self.is_target_locked):
                print("\nNO TARGET LOCKED\n")
                print("select a new target")
                self.lock_target()
                msg = self.last_locked_target
                # if locking a target fails
                if (self.is_target_locked == False):
                    # if this case is executed, an empty detection will be sent
                    print("locking a target failed")
                    self.lock_attempts = 4
                    msg = Detection()
            # if there is a locked target
            else:
                print("\n[timer_callback] THERE Was LOCKED TARGET\n")

                print(f"try to lock to the previously selected target: {self.last_locked_target}")
                self.lock_target(prefered_target=self.last_locked_target)

                if (self.is_target_locked == False):
                    print("locking a target failed")

                    while(self.lock_attempts >= 0 or self.is_target_locked == True):

                        self.lock_target(prefered_target=self.last_locked_target)
                        msg = self.last_locked_target
                else:
                    self.lock_attempts = 4
                    msg = self.last_locked_target
        
        print(type(msg))
        print((msg))
        self.publisher_.publish(msg)
        self.get_logger().info('\n Target_select_PUB: "%s" \n' % msg)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = TargetSelect()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
