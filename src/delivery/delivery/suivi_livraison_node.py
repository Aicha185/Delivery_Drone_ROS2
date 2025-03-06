import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped

class SuiviLivraisonNode(Node):
    def __init__(self):
        super().__init__('suivi_livraison_node')
        self.subscription = self.create_subscription(
            PoseStamped,
            'position_drone',  # Le topic auquel ce nœud va s'abonner
            self.listener_callback,
            10
        )
        self.get_logger().info('En attente de la position du drone...')

    def listener_callback(self, msg):
        self.get_logger().info('Position actuelle du drone: x=%.2f, y=%.2f' % (msg.pose.position.x, msg.pose.position.y))

def main(args=None):
    rclpy.init(args=args)
    node = SuiviLivraisonNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
