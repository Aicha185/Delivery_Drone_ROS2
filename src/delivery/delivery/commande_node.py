import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class CommandeNode(Node):
    def __init__(self):
        super().__init__('commande_node')
        self.publisher_ = self.create_publisher(String, 'commande', 10)
        self.create_timer(2.0, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = "Nouvelle commande: Livraison de colis"
        self.publisher_.publish(msg)
        self.get_logger().info('Commande envoyée: %s' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = CommandeNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
