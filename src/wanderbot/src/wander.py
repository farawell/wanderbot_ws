#!/usr/bin/env python3
# ROS1

# Description: 
# The robot goes straight until either there's a obstacle that is closer
# than 0.8m or it has been moving more than 30 seconds.
# If one of (or both) above conditions are met, it stops and spins for
# 30 seconds.

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

def scan_callback(msg):
    # Distance to the closet obstacle around the robot
    global g_range_ahead
    g_range_ahead = min(msg.ranges)

g_range_ahead = 1 # Just a random number

scan_sub = rospy.Subscriber('scan', LaserScan, scan_callback)
cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size = 1)
rospy.init_node('wnader')

state_change_time = rospy.Time.now()
driving_forward = True
rate = rospy.Rate(10)

while not rospy.is_shutdown():
    if driving_forward:
        if (g_range_ahead < 0.8 or rospy.Time.now() > state_change_time):
            driving_forward = False
            state_change_time = rospy.Time.now() + rospy.Duration(5)
    else:
        if rospy.Time.now() > state_change_time:
            driving_forward = True
            state_change_time = rospy.Time.now() + rospy.Duration(30)

twist = Twist()
if driving_forward:
    twist.linear.x = 1
else:
    twist.angular.z = 1 # Adjusting the yaw angle

cmd_vel_pub.publish(twist)

rate.sleep()