#!/usr/bin/env python3
# ROS1

# Refined version of wander.py

# Description: 
# The robot goes straight until either there's a obstacle that is closer
# than 0.8m or it has been moving more than 30 seconds.
# If one of (or both) above conditions are met, it stops and spins for
# 30 seconds.

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class wanderBotController:
    SAFE_DISTANCE = 0.8 #meter
    MAX_DRIVE_TIME = rospy.Duration(30)
    MAX_SPIN_TIME = rospy.Duration(30)

    def __init__(self):
        self.range_ahead = 1 # Just a random number
        self.last_state_update_time = rospy.Time.now()
        self.driving_forward = True
        self.scan_sub = rospy.Subscriber('scan', LaserScan, scan_callback)
        self.cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size = 1)
        self.rate = rospy.Rate(10)

    def scan_callback(self, msg):
        self.range_ahead = min(msg.ranges)

    def run(self):
        twist = Twist()

        while not rospy.is_shutdown():
            elapsed_time = rospy.Time.now() - self.last_state_update_time
            
            if  driving_forward and \
                (elapsed_time > self.MAX_DRIVE_TIME or 
                 self.range_ahead < self.SAFE_DISTANCE):
                    self.driving_forward = False
                    twist.angular.z = 0
                    twist.linear.x = 1
                    self.last_state_update_time = rospy.Time.now()
            elif not driving_forward and elapsed_time > self.MAX_SPIN_TIME:
                self.driving_forward = True
                twist.linear.x = 0
                twist.angular.z = 1
                self.last_state_update_time = rospy.Time.now()
            
            self.cmd_vel_pub.publish(twist)
            self.rate.sleep()

if __name__ == '__main__':
    rospy.init_node(wander)

    try:
        controller = wanderBotController()
        controller.run()
    except rospy.ROSInterruptException:
        pass
