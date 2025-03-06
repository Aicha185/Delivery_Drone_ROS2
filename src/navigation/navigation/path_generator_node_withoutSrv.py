import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Path

class PathGeneratorNode(Node):
    def __init__(self):
        super().__init__('path_generator_node')

        # Subscriber pour la destination
        self.destination_subscriber = self.create_subscription(
            PoseStamped, 'destination', self.destination_callback, 10
        )

        # Publisher pour le chemin généré
        self.path_publisher = self.create_publisher(Path, 'planned_path', 10)

        # Initialisation des variables
        self.destination = None
        self.timer = None

        self.get_logger().info('PathGeneratorNode is running...')
    def destination_callback(self, msg):
        """Callback pour recevoir la destination et commencer à générer le chemin."""
        new_destination = (msg.pose.position.x, msg.pose.position.y)

        # Vérifiez si la destination est différente
        if self.destination == new_destination:
            self.get_logger().info('Received same destination. Skipping path generation.')
            return

        self.destination = new_destination
        self.get_logger().info(f'Received new destination: {self.destination}')
        
        # Annulez le timer existant (s'il y en a un)
        if self.timer is not None:
            self.timer.cancel()
        
        # Créez un nouveau timer pour générer le chemin
        self.timer = self.create_timer(1.0, self.generate_path)

   
    def generate_path(self):
        """Génère un chemin vers la destination et le publie."""
        if self.destination is None:
            self.get_logger().warn('No destination set. Path cannot be generated.')
            return

        path = Path()
        path.header.frame_id = 'map'
        path.header.stamp = self.get_clock().now().to_msg()

        # Génération d'un chemin linéaire simple
        steps = 20
        for i in range(steps + 1):
            pose = PoseStamped()
            pose.header.frame_id = 'map'
            pose.pose.position.x = self.destination[0] * i / steps
            pose.pose.position.y = self.destination[1] * i / steps
            pose.pose.orientation.w = 1.0  # Orientation par défaut
            path.poses.append(pose)

        self.path_publisher.publish(path)
        self.get_logger().info('Path published successfully.')

def main(args=None):
    rclpy.init(args=args)
    node = PathGeneratorNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Shutting down Path Generator Node.")
    finally:
        node.destroy_node()
        rclpy.shutdown()

    #rclpy.spin(node)
    #node.destroy_node()
   # rclpy.shutdown()

if __name__ == '__main__':
    main()
