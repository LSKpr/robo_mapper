#!/usr/bin/env python


import rospy
from std_msgs.msg import String
from std_msgs.msg import String
  
def obj_sender_init():
    pub = rospy.Publisher('obj_marker', String, queue_size=10)
    rospy.init_node('obj_sender', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    
  
def obj_sender():
   if not rospy.is_shutdown():
        data_content = "hello wrd, obj_sender %s" % rospy.get_time()
        rospy.loginfo(data_content)
        pub.publish(data_content)
        rate.sleep()
 
if __name__ == '__main__':
    try:
        obj_sender_init()
        obj_sender()
    except rospy.ROSInterruptException:
        pass


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    
def listener():

    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("obj_marker", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()

