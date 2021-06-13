#!/usr/bin/env python3
import roslib; roslib.load_manifest('ros_test')
import rospy
from std_msgs.msg import String

count = 0


def talker():
    global count
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10)    # 10hz
    while not rospy.is_shutdown():
        count_str = f"Count: {count}"
        count += 1
        rospy.loginfo(count_str)
        pub.publish(count_str)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
