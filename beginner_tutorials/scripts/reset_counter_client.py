#!/usr/bin/env python

import rospy
from std_srvs.srv import SetBool

def reset_counter_client(flag):
    rospy.wait_for_service('reset_counter')
    
    try:
        reset_counter_srv = rospy.ServiceProxy('reset_counter', SetBool)
        resp = reset_counter_srv(flag)
        rospy.loginfo(resp)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    reset_counter_client(True)