import rclpy
from rclpy.node import Node
from std_msgs.msg import String

from ultralytics import YOLO
import cv2

import json

# DTO class to send to raspberry
class Detection:

    def __init__(self,name,id,center_point_location, screen_size):

        self.name = name # class name of the detected cobject
        self.id = id # id assigned from the tracking
        self.location = center_point_location # centeer point of the detected object
        self.screen_size = screen_size # current size of the fram ( used on rpi4 to calculate the center)

    # makes the class int a Json
    def to_json(self):
        return json.dumps(self.__dict__)
    
class DetectionPublisher(Node):


    def __init__(self):

        super().__init__('vision_detections') # name of the node
        self.publisher_ = self.create_publisher(String, 'detections', 10) # initializing publisher with a name 'detections' of type string
        timer_period = 0.5  # seconds between message published
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

        self.model = YOLO('yolov8s.pt')
        self.model = YOLO('v4_greyscale_best.pt')  # load a custom model
        video_path = 0
        self.cap = cv2.VideoCapture(video_path)
        self.ret = True
        
        self.msg = String()
        self.items = [] # holding the current detected objects

    def timer_callback(self):
        self.ret, self.frame = self.cap.read()

        if(self.ret):
            results = self.model.track(self.frame, persist=True,conf=0.3, iou=0.3)

            # count boxes from left and from right side of frame
            for r in results:
                left_item_counter = 0
                right_item_counter = 0
                
                boxes = r.boxes

                for box in boxes:
                    b = box.xyxy[0]  # get box coordinates in (left, top, right, bottom) format
                    center_x = int((b[0] + b[2]) / 2)
                    center_y = int((b[1] + b[3]) / 2)

                    if(center_x < self.frame.shape[1] // 2):
                        left_item_counter += 1
                    else:
                        right_item_counter +=1

                    location = (center_x, center_y) #center of a detection
                    # frame size
                    width  = self.cap.get(3)  
                    height = self.cap.get(4)  
                    screen_size = (width, height)
                    # class name of the detection
                    cls =  int(box.cls.item())
                    name = r.names[cls]
                    #tracker id of the detection
                    if(box.id):
                        id = int(box.id)
                    else:
                        id = "none"

                    item = Detection(name=name, id=id, center_point_location=location, screen_size = screen_size)
                    self.msg.data = item.to_json()
                    #self.items.append(item)
                    

            print(f'left: {left_item_counter}, right: {right_item_counter}')

        
        #self.msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(self.msg)
        self.get_logger().info('Publishing: "%s"' % self.msg.data)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = DetectionPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
