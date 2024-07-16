#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray
import threading

# Initialize global variables for position
x, y = 0.0, 0.0

def callback(data):
    global x, y
    
    # Extract position from the PoseStamped message
    x = data.pose.position.x
    y = data.pose.position.y
    
    rospy.loginfo("Received PoseStamped message:")
    rospy.loginfo("Position - x: %f, y: %f", x, y)

def obj_sender():
    # Initialize a new node named 'obj_sender'
    pub = rospy.Publisher('visualization_marker_array', MarkerArray, queue_size=10)  # Create a Publisher

    # Define the rate at which messages are published
    rate = rospy.Rate(1)  # 1Hz
    markerArray = MarkerArray()
    count = 0
    MARKERS_MAX = 100
    while not rospy.is_shutdown():
        # Create a Marker message
        marker = Marker()
        marker.header.frame_id = "map"
        marker.header.stamp = rospy.get_rostime()
        marker.ns = "obj_name"
        marker.id = count
        marker.type = Marker.SPHERE  # sphere
        marker.action = Marker.ADD
        marker.pose.position.x = x
        marker.pose.position.y = y
        marker.pose.orientation.x = 0
        marker.pose.orientation.y = 0
        marker.pose.orientation.z = 0
        marker.pose.orientation.w = 1.0
        marker.scale.x = 0.5
        marker.scale.y = 0.5
        marker.scale.z = 0.5
        marker.color.r = 0.0
        marker.color.g = 1.0
        marker.color.b = 0.0
        marker.color.a = 1.0

        rospy.loginfo("Publishing Marker message:")
        if len(markerArray.markers) >= MARKERS_MAX:
            markerArray.markers.pop(0)

        markerArray.markers.append(marker)

        # Renumber the marker IDs
        for i, m in enumerate(markerArray.markers):
           m.id = i
    
        # Publish the MarkerArray
        pub.publish(markerArray)
    
        count += 1
        rospy.loginfo(markerArray)
        rate.sleep()

def cord_listener():
    # Subscribe to the `slam_out_pose` topic with `PoseStamped` message type
    rospy.Subscriber("slam_out_pose", PoseStamped, callback)

    # Keep Python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    try:
        # Initialize the ROS node with a unique name
        rospy.init_node('object_recognition_node', anonymous=True)

        # Start the listener in a separate thread
        listener_thread = threading.Thread(target=cord_listener)
        listener_thread.start()

        # Run the object sender function
        obj_sender()
    except rospy.ROSInterruptException:
        pass
