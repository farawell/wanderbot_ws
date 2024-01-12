#!/usr/bin/env python3
# ROS1

# note for myself: tty stands for teletypewriter, and termios for terminal I/O settings
import sys, select, tty, termios
import rospy
from std_msgs.msg import String

if __name__ == '__main__':
    key_pub = rospy.Publisher('keys', String, queue_size = 1)
    rospy.init_node("keyboard_driver")
    rate = rospy.Rate(100)
    
    # Saving the previous terminal settings
    old_attr = termios.tcgetattr('sys.stdin') 

    # .fineno() method returns the fd of sys.stdin
    # cbreak mode: still acepts ctrl-c, but 
    #              input characters are made available to the program  
    #              immediately after they are typed.
    tty.setcbreak(sys.stdin.fileno())

    print('Publishing keystrokes. Press Ctrl-c to exit...')

    while not rospy.is_shutdown():
        # select.select(read_list, write_list, error_list, timeout)
        # [sys.stdin]: list containing the sys.stdin
        # timeout is set to 0, making select.select() returns immediately
        # 
        # select.select([sys.stdin], [], [], 0)[0]: 
        # Returns the read-available [sys.stdin] when there's a keyboard input
        # When no keyboard input, it reutns empty list. While [sys.stdin]
        # always holds the list containing the sys.stdin file-like object
        #
        # [0]: list of file descriptors that are ready for 'reading'
        if select.select([sys.stdin], [], [], 0)[0] == [sys.stdin]:
            key_pub.publish(sys.stdin.read(1))
        rate.sleep()
    
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_attr)
