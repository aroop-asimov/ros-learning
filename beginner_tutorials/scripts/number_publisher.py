#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64


class NumberPublisher():

    def __init__(self) -> None:
        self.num_pub = rospy.Publisher('/number', Int64, queue_size=1)
        # self.number = 0
        self.rate = rospy.Rate(1)
    
    def publish_num(self, number) -> None:
        self.num_pub.publish(number)
        rospy.loginfo("Number published: " + str(number))

    
    def run(self) -> None:
        while not rospy.is_shutdown():
            self.publish_num(2)
            self.rate.sleep()

if __name__ == '__main__':
    rospy.init_node("number_publisher")
    rospy.loginfo("NumberPublisher node is started")
    try:
        node = NumberPublisher()
        node.run()

    except rospy.ROSInterruptException:
        pass
        # rospy.loginfo("shuted down")
