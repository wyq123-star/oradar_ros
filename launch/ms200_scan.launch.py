#!/usr/bin/env python3
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # LiDAR publisher node
    ordlidar_node = Node(
        package='oradar_lidar',
        executable='oradar_scan',  # 确保这是正确的可执行文件名称
        name='MS200',
        output='screen',
        parameters=[
            {'device_model': 'MS200'},
            {'frame_id': 'laser_frame'},
            {'scan_topic': 'MS200/scan'},
            {'port_name': '/dev/ttyACM0'},  # 请根据实际设备端口修改
            {'baudrate': 230400},
            {'angle_min': 0.0},
            {'angle_max': 360.0},
            {'range_min': 0.05},
            {'range_max': 20.0},
            {'clockwise': False},
            {'motor_speed': 10}
        ]
    )

    # base_link 到 laser_frame 的静态坐标变换节点 (如需启用，请取消注释并检查参数)
    # base_link_to_laser_tf_node = Node(
    #     package='tf2_ros',
    #     executable='static_transform_publisher',  # 关键修正：参数名应为 executable
    #     arguments=['0', '0', '0.18', '0', '0', '0', 'base_link', 'laser_frame'], # 发布变换的参数
    #     name='base_link_to_laser_tf_publisher'   # 关键修正：参数名应为 name
    # )

    # 创建启动描述并添加节点
    ld = LaunchDescription()
    ld.add_action(ordlidar_node)
    # ld.add_action(base_link_to_laser_tf_node) # 如需发布静态变换，请取消注释

    return ld