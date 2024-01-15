import rclpy
from rclpy.node import Node
from std_msgs.msg import String

from ultralytics import YOLO
import cv2

import json

class Detection:

    def __init__(self,name,id,center_point_location):
        self.name = name
        self.id = id
        self.location = center_point_location

    def to_json(self):
        return json.dumps(self.__dict__)
    
class MinimalPublisher(Node):


    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

        self.model = YOLO('yolov8s.pt')
        self.model = YOLO('v4_greyscale_best.pt')  # load a custom model
        video_path = 0
        self.cap = cv2.VideoCapture(video_path)
        self.ret = True
        
        self.msg = String()

        self.items = []

    def timer_callback(self):
        self.ret, self.frame = self.cap.read()

        if(self.ret):
            results = self.model.track(self.frame, persist=True,conf=0.3, iou=0.3)
            # count boxes from left and from right side of frame
            for r in results:
                left_item_counter = 0
                right_item_counter = 0
                

                boxes = r.boxes
                #for box, id in zip(boxes, track_ids):

                for box  in boxes:
                    b = box.xyxy[0]  # get box coordinates in (left, top, right, bottom) format
                    c = box.cls
                    center_x = int((b[0] + b[2]) / 2)
                    center_y = int((b[1] + b[3]) / 2)

                    if(center_x < self.frame.shape[1] // 2):
                        left_item_counter += 1
                    else:
                        right_item_counter +=1

                    location = (center_x, center_y)
                    item = Detection(name='',id=0, center_point_location=location)
                    self.msg.data = item.to_json()
                    #self.items.append(item)
                    #print(item.to_json())

            print(f'left: {left_item_counter}, right: {right_item_counter}')

        
        #self.msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(self.msg)
        self.get_logger().info('Publishing: "%s"' % self.msg.data)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
