#!/usr/bin/env python3
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def move_to_goal(x, y, z, w):
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.orientation.z = z
    goal.target_pose.pose.orientation.w = w

    rospy.loginfo(f"Gidilen hedef: x={x}, y={y}")
    client.send_goal(goal)
    client.wait_for_result()

if __name__ == "__main__":
    rospy.init_node('multi_goal_nav')

    points = [
        (-1.4486, -0.4300, 0.0, 1.0),
        (-0.5295209288597107, -0.6853633522987366, 0.0, 1.0),
        (1.615195631980896, -0.532169759273529, 0.0, 1.0),
        (1.7581768035888672, 0.9078540205955505, 0.0, 1.0),
        (1.8705191612243652, -0.9917519688606262, 0.0, 1.0)
    ]

    for p in points:
        move_to_goal(*p)
