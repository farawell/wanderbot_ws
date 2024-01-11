#!/usr/bin/env python3
# ROS1

# Description: 
# The robot goes straight until either there's a obstacle that is closer
# than 0.8m or it has been running more than 30 seconds.
# If one of (or both) above conditions are met, the robot stops and spins
# for 5 seconds, and runs again.

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
rospy.init_node('wander')

state_change_time = rospy.Time.now()
driving_forward = True
rate = rospy.Rate(10)

while not rospy.is_shutdown():
    state_duration = rospy.Time.now() - state_change_time
    run_state_over_30s = state_duration > rospy.Duration(30)
    stop_state_over_5s = state_duration > rospy.Duration(5)

    if driving_forward:
        if (g_range_ahead < 0.2 or run_state_over_30s):
            driving_forward = False
            state_change_time = rospy.Time.now()
    else: # On halt
        if stop_state_over_5s:
            driving_forward = True
            state_change_time = rospy.Time.now()

    twist = Twist() # initialization
    if driving_forward:
        twist.angular.z = 0
        twist.linear.x = 1
    else:
        twist.linear.x = 0
        twist.angular.z = 1 # Adjusting the yaw angle

    cmd_vel_pub.publish(twist)

    rate.sleep()
