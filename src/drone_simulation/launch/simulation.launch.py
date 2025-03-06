import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
    # Chemin vers le monde Ignition Gazebo
    world_file = os.path.join(get_package_share_directory('drone_simulation'), 'worlds', 'delivery_world.sdf')

    # Démarrer Ignition Gazebo avec le monde spécifié
    ignition = ExecuteProcess(
        cmd=['ign', 'gazebo', '--verbose', world_file],
        output='screen'
    )

    # Démarrer les nœuds ROS
    path_generator_node = Node(
        package='navigation',  # Remplacez par le nom correct de votre package
        executable='path_generator_node_withoutSrv',
        output='screen'
    )

    obstacle_avoider_node = Node(
        package='navigation',  # Remplacez par le nom correct de votre package
        executable='obstacle_avoider_node',
        output='screen'
    )

    commande_node = Node(
        package='delivery',  # Remplacez par le nom correct de votre package
        executable='commande_node',
        output='screen'
    )

    confirmation_livraison_node = Node(
        package='delivery',  # Remplacez par le nom correct de votre package
        executable='confirmation_livraison_node',
        output='screen'
    )

    suivi_livraison_node = Node(
        package='delivery',  # Remplacez par le nom correct de votre package
        executable='suivi_livraison_node',
        output='screen'
    )

    battery_monitor_node = Node(
        package='power_management',  # Remplacez par le nom correct de votre package
        executable='battery_monitor',
        output='screen'
    )

    emergency_handler_node = Node(
        package='power_management',  # Remplacez par le nom correct de votre package
        executable='emergency_handler',
        output='screen'
    )

    return_to_base_server_node = Node(
        package='power_management',  # Remplacez par le nom correct de votre package
        executable='return_to_base_server',
        output='screen'
    )

    return LaunchDescription([
        ignition,
        path_generator_node,
        obstacle_avoider_node,
        commande_node,
        confirmation_livraison_node,
        suivi_livraison_node,
        battery_monitor_node,
        emergency_handler_node,
        return_to_base_server_node
    ])