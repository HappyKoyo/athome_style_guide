#!/usr/bin/env python
# -*- coding: utf-8 -*

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan

class DoorOpenDetector:
    def __init__(self):
        #1.インターフェース
        self.laser_range_sub = rospy.Subscriber('/scan',LaserScan,self.getLaserRangeCB)
        self.door_open_detect_request_sub = rospy.Subscriber('/door_open_detector/request',String,self.detectDoorOpenCB)
        self.door_state_pub = rospy.Publisher('/door_open_detector/result',String,queue_size=1)
        #2.定数
        self.ALL_LIDAR_SCAN_LINE = 1080
        #3.変数
        self.front_laser_dist = 999
        
    def getLaserRangeCB(self,lidar_input):
        self.front_laser_dist = lidar_input.ranges[self.ALL_LIDAR_SCAN_LINE/2]

    def detectDoorOpenCB(self,msg):
        print "front_laser_dist is",self.front_laser_dist
        if self.front_laser_dist > 0.5:
            print "The door is opened!"
            result = String("True")
            self.door_state_pub.publish(result)
        else:
            print "The door is closed!"
            result = String("False")
            self.door_state_pub.publish(result)
        
if __name__ == '__main__':
    rospy.init_node('door_open_detector')
    door_open_detector = DoorOpenDetector()
    rospy.spin()
