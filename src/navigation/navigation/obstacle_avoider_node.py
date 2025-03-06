
import rclpy
import math
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped

class ObstacleAvoiderNode(Node):
    def __init__(self):
        super().__init__('obstacle_avoider_node')

        # Subscriber pour le chemin planifié
        self.path_subscription = self.create_subscription(
            Path, 'planned_path', self.path_callback, 10
        )

        # Subscriber pour les données LiDAR
        self.lidar_subscription = self.create_subscription(
            LaserScan, 'scan', self.lidar_callback, 10
        )

        # Publisher pour le chemin corrigé
        self.corrected_path_publisher = self.create_publisher(Path, 'corrected_path', 10)

        # Variables internes
        self.current_path = None

        self.get_logger().info('ObstacleAvoiderNode is running...')

    def path_callback(self, path_msg):
        """Callback pour recevoir le chemin planifié."""
        self.current_path = path_msg
        self.get_logger().info('Path received.')


    def lidar_callback(self, scan_msg):
        """Callback pour analyser les obstacles et ajuster le chemin."""
        if self.current_path is None:
            self.get_logger().warn('No path available to adjust.')
            return

        corrected_path = Path()
        corrected_path.header = self.current_path.header

        self.get_logger().info('Processing path adjustment...')

        for pose in self.current_path.poses:
            if self.is_obstacle_nearby(scan_msg, pose):
                self.get_logger().info(
                    f'Obstacle detected near ({pose.pose.position.x}, {pose.pose.position.y}). Adjusting path.'
                )
                pose.pose.position.y += 1.0  # Ajustement simple pour éviter l'obstacle
            corrected_path.poses.append(pose)

        self.get_logger().info('Publishing corrected path...')
        self.corrected_path_publisher.publish(corrected_path)

   

    def is_obstacle_nearby(self, scan_msg, pose):
        """Vérifie si un obstacle est proche de la position donnée."""
        for i, distance in enumerate(scan_msg.ranges):
            if distance < 1.0:  # Distance seuil pour détecter un obstacle
                angle = scan_msg.angle_min + i * scan_msg.angle_increment
                x = distance * math.cos(angle)
                y = distance * math.sin(angle)
                if abs(x - pose.pose.position.x) < 0.5 and abs(y - pose.pose.position.y) < 0.5:
                    return True
        return False

def main(args=None):
    rclpy.init(args=args)
    node = ObstacleAvoiderNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
