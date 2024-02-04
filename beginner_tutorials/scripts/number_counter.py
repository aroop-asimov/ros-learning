#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64
from std_srvs.srv import SetBool

class NumberCounter():
    
    def __init__(self) -> None:
        self.counter = 0
        self.number_sub = rospy.Subscriber('number', Int64, self.number_callback)
        self.counter_pub = rospy.Publisher('number_counter', Int64, queue_size=2)
        self.reset_counter_srv = rospy.Service('reset_counter', SetBool, self.reset_counter_handler)
    
    def number_callback(self, msg) -> None:
        self.counter += msg.data
        self.counter_pub.publish(self.counter)
    
    def reset_counter_handler(self, req):
        if req.data:
            print(req)
            self.counter = 0
            return True, "Counter has been successfully reset"
        else:
            return False, "Counter can't reset"

if __name__ == '__main__':
    rospy.init_node("NumberCounter")
    rospy.loginfo("NumberCounter node is started")
    try:
        node = NumberCounter()
        rospy.spin()
    except Exception as e:
        rospy.loginfo(e)


        