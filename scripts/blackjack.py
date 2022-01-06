#!/usr/bin/env python3

"""
BDS 3-Clause License

Copyring (c) 2021 Ryuichi Ueda + Kaito Nemoto.
All right reserved.
"""

import rospy
from std_msgs.msg import Int32
import random 

rospy.init_node('toranpu')
pub = rospy.Publisher('card', Int32, queue_size=1)  
rate = rospy.Rate(10)
n = 0

x = random.randint(1,13)
y = random.randint(1,13)
z = random.randint(1,13)

n = x + y + z

print('数は', x, 'と', y, 'と', z)
print('合わせて', n)

while not rospy.is_shutdown():
    pub.publish(n)
    rate.sleep()
