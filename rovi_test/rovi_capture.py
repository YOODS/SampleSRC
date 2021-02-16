#!/usr/bin/python

import roslib
import rospy
from rovi.msg import Floats
from rospy.numpy_msg import numpy_msg
from std_msgs.msg import Bool
import numpy as np
import open3d as o3d

def np2F(d):  #numpy to Floats
  f = Floats()
  f.data = np.ravel(d)
  return f

def voxel(data):
  mesh = nfparam['mesh']
  if mesh == 0:
    return data
  if len(data) < 10:
    return data
  d = np.asarray(data).astype(np.float32)
  pc = o3d.geometry.PointCloud()
  pc.points = o3d.Vector3dVector(d)
  dwpc = o3d.geometry.voxel_down_sample(pc,voxel_size=mesh)
  rospy.loginfo("down sample done")
  return np.reshape(np.asarray(dwpc.points),(-1, 3))

def nf(data):
  d = np.asarray(data).astype(np.float32)
  pc = o3d.geometry.PointCloud()
  pc.points = o3d.Vector3dVector(d)
  nfmin = nfparam['nfmin']
  if nfmin <= 0:
    nfmin = 1
  nfrad = nfparam['nfrad']
  cl, ind = o3d.geometry.radius_outlier_removal(pc,
                                                nb_points = nfmin,
                                                radius = nfrad)
  dwpc = o3d.geometry.select_down_sample(pc, ind)
  rospy.loginfo("noise filter done")
  return np.reshape(np.asarray(dwpc.points),(-1, 3))

def get_nfparam():
  global nfparam
  nfparam['nf'] = rospy.get_param("/rovi_test/nf", False)
  nfparam['mesh'] = rospy.get_param("/rovi_test/mesh", 0)
  nfparam['nfmin'] = rospy.get_param("/rovi_test/nfmin", 0)
  nfparam['nfrad'] = rospy.get_param("/rovi_test/nfrad", 0)

def cb_capture(msg):
  rospy.loginfo("[%d] capture result %s", count, msg.data)

def cb_ps(msg):
  pc = np.reshape(msg.data,(-1,3))
  get_nfparam()
  if nfparam['nf']:
    pc = voxel(pc)
    if nfparam['nfrad'] > nfparam['mesh']:
      pc = nf(pc)
    out_floats = np2F(pc)
    pub_nf.publish(out_floats)

if __name__=="__main__":
  global nfparam
  nfparam = dict()
  rospy.init_node("rovi_capture", anonymous = True)
  rospy.Subscriber("/rovi/Y1", Bool, cb_capture)
  rospy.Subscriber("/rovi/ps_floats", numpy_msg(Floats), cb_ps)
  pub_capture = rospy.Publisher("/rovi/X1", Bool, queue_size = 1)
  pub_nf = rospy.Publisher("rovi_test/ps_floats",
                           numpy_msg(Floats),
                           queue_size = 1)
  rospy.sleep(1)
  count = 0
  r = rospy.Rate(0.1) # 10s
  while not rospy.is_shutdown():
    if rospy.get_param("/rovi_test/pshift"):
      count = count + 1
      msg = Bool()
      msg.data = True
      rospy.loginfo("[%d] capture request", count)
      pub_capture.publish(msg)
    r.sleep()
