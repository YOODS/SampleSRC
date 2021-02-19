#!/usr/bin/python

import roslib
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2

def cb_binary(msg):
  bridge = CvBridge()
  try:
    orig = bridge.imgmsg_to_cv2(msg, "mono8")
  except CvBridgeError as e:
    print 'cvbridge exception: ',e
  else:
    thresh = rospy.get_param("/rovi_test/binthresh")
    ret, binimg = cv2.threshold(orig, thresh, 255, cv2.THRESH_BINARY)
    try:
      imgmsg = bridge.cv2_to_imgmsg(binimg, "mono8")
    except CvBridgeError as e:
      print 'cvbridge exception: ',e
    else:
      pub_binary.publish(imgmsg)

if __name__=="__main__":
  rospy.init_node("rovi_bin", anonymous = True)
  rospy.Subscriber("/rovi/left/image_raw", Image, cb_binary)
  pub_binary = rospy.Publisher("/rovi_test/left/image_bin",
                               Image,
                               queue_size = 1)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    pass
