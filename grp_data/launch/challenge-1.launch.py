import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():

    tbot_start_path = get_package_share_directory('tbot_start')
    launch_file_dir = os.path.join(tbot_start_path, 'launch')

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([launch_file_dir, '/full.launch.py'])
            ),
        Node(
            package='grp_data',
            executable='scan_echo',
            name='scan'
        ),
        Node(
            package='grp_data',
            executable='reactive_move',
            name='reactive_move'
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='visualization',
            arguments=['-d', [os.path.join('/home/bot/ros2_ws/LARM-kim-nathan/grp_data/for_rvizz/config_rviz2_for_grp_data.rviz')]]
        )
    ])