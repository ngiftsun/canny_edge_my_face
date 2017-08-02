#!/usr/bin/env python
import roslib
roslib.load_manifest('canny_edge_my_face')
import sys
import rospy
import cv2
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class image_converter:    
    
  def __init__(self):
    self.bridge = CvBridge()  
    self.image_pub = rospy.Publisher("image",Image,queue_size=1000)
    self.image_sub = rospy.Subscriber("/cv_camera/image_raw",Image,self.callback)

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)
    gray_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY) 
    canny_image  = cv2.Canny(gray_image ,40,70)  
    cv2.imshow("Canny Edge Filter", canny_image)
    cv2.waitKey(3)
    try:
      self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
    except CvBridgeError as e:
      print(e)

if __name__ == '__main__':
    ic = image_converter()
    rospy.init_node('image_converter', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()



