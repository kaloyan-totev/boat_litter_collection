import rclpy
from rclpy.node import Node
from custom_msgs.msg import DetectionsArray
from custom_msgs.msg import Detection

from ultralytics import YOLO
import cv2

class DetectionPublisher(Node):

    def __init__(self):

        super().__init__('vision_detections') # name of the node
        self.publisher_ = self.create_publisher(DetectionsArray, 'detections', 10) # initializing publisher with a name 'detections' of type string
        timer_period = 0.05  # seconds between message published
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

        self.model = YOLO('yolov8s.pt')
        #self.model = YOLO('v4_greyscale_best.pt')  # load a custom model
        video_path = 0
        self.cap = cv2.VideoCapture(video_path)
        self.ret = True
        
        self.msg = DetectionsArray()


    def timer_callback(self):
        self.ret, self.frame = self.cap.read()

        if(self.ret):
            results = self.model.track(self.frame, persist=True,conf=0.5, iou=0.3, show=True, imgsz=320)
            self.msg.is_empty = len(results) == 0
            # count boxes from left and from right side of frame
            for r in results:
                left_item_counter = 0
                right_item_counter = 0
                self.msg.detections.clear()
                
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


                    detection = Detection()
                    detection.name.data = str(name)
                    detection.id.data = str(id)
                    detection.location_x.data = float(center_x)
                    detection.location_y.data = float(center_y)
                    detection.screen_size_x.data = float(width)
                    detection.screen_size_y.data = float(height)
                    detection.confidence.data = float(box.conf)
                    self.msg.detections.append(detection)


                    

            print(f'left: {left_item_counter}, right: {right_item_counter}')

        
        #self.msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(self.msg)
        for item in self.msg.detections:
            print(f"name: {item.name.data} id: {item.id.data} location: {item.location_x.data}\n")
        #self.get_logger().info('Publishing: "%s"' % self.msg.detections)
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
