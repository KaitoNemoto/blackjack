#!/usr/bin/env python3

"""
BDS 3-Clause License

Copyring (c) 2021 Ryuichi Ueda + Kaito Nemoto.
All right reserved.
"""

import rospy
from std_msgs.msg import Int32

n = 0

def cb(message):
    global n
    n = message.data

    while 1:
        if n > 21:
            rospy.loginfo('you lose...')
        elif n < 21:
            rospy.loginfo('win!!')
        else:
            rospy.loginfo('BlackJack!!!')

if __name__ == '__main__':
    rospy.init_node('discrimination')
    sub = rospy.Subscriber('card', Int32, cb) 
    rospy.spin()
