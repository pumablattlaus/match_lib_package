from match_lib.match_geometry import MyPoint, MyPose, MyPointStamped, MyOrient, rotateVector, rotationDiffRotated, getOrientationDiffList
from geometry_msgs.msg import Pose
from match_lib.filter_img import LowPassFilter
import pytest
import rospy

def test_geometry():
    p1 = MyPoint((1, 2, 3))
    p2 = MyPoint((1, 2, 3))

    p3 = p1 + p2

    p3_result = MyPoint((2, 4, 6))
    assert p3 == p3_result

    pose1 = MyPose((1, 2, 3))
    pose2 = MyPose((1, 2, 3))

    pose3 = MyPose()

    pose3.position = pose1.position + pose2.position

    pose3_res = MyPose((2, 4, 6))
    
    assert pose3.position == pose3_res.position

    # MyPose from Pose:
    pose = Pose()
    pose.position.x, pose.position.y, pose.position.z = 1, 2, 3
    pose.orientation.x, pose.orientation.y, pose.orientation.z, pose.orientation.w = 0, 1, 0, 0

    pose_my = MyPose(pose)
    assert(MyPose((1, 2, 3),(0,1,0,0)) == pose_my)

    p1 = MyPose((0.656036424314, -0.0597577841713, -0.103558385398), (-0.909901224555, 0.41268467068,
                                                                      -0.023065127793, 0.0352011934197))
    a1 = [-0.198922703533319, 1.3937412735955756, 0.11749296106956011, -1.312658217933717, -0.1588243463469876,
          2.762937863667806, 0.815807519980951]

    # panda_goal = PandaGoals(p1, a1)
    # print(panda_goal)

    # Orientation:
    o_diff = MyOrient((0, 0, 0.7071068, 0.7071068))
    assert [0,-1,0,0] == pytest.approx(rotateVector((1, 0, 0, 1), o_diff.asArray()).asArray())

    o = MyOrient()  # 0°
    o_diff_rot = rotationDiffRotated(o.asArray(), o_diff.asArray())
    assert [0,0,0,1] == pytest.approx(o_diff_rot)  # 0°

    o = MyOrient((0.7071068, 0, 0.0, 0.7071068))  # 45° um x
    o_diff_rot = rotationDiffRotated(o.asArray(), o_diff.asArray())
    assert [0.,-0.70710684,0.,0.70710684] == pytest.approx(o_diff_rot)

    diff_list = getOrientationDiffList(o, [p1.orientation, pose1.orientation, pose2.orientation, pose3.orientation])
    print(diff_list)

@pytest.mark.parametrize("p1, p2, p_res", [
      ((1, 2, 3), (1, 2, 3), (2, 4, 6)),
      ((1, 2, 3), (-1, -2, -3), (0, 0, 0))])

def test_with_ros(p1,p2,p_res):
    rospy.init_node("Test_geom")
    
#     p_stamped = MyPointStamped((1, 2, 3))
#     p_stamped2 = MyPointStamped((1, 2, 3))

    p_stamped = MyPointStamped(p1)
    p_stamped2 = MyPointStamped(p2)

    p_stamped_res = p_stamped + p_stamped2

#     p_vgl = MyPointStamped((2, 4, 6))
    p_vgl = MyPointStamped(p_res)
    p_vgl.header.stamp = p_stamped_res.header.stamp
    assert p_stamped_res == p_vgl

@pytest.mark.skip(reason="test not yet fully implemented: different loop lengths and shapes")
def test_filter(shape=(1, 1)):
    filter = LowPassFilter(shape, 0.1)
    filter.filter(1)
    assert filter.integrator() == [[0.1]]

def test_filter2(shape=(10, 10)):
    with pytest.raises(TypeError):
          LowPassFilter(shape[0], shape[1], 0.1)

if __name__ == '__main__':
    test_geometry()