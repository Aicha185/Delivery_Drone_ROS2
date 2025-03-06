import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger

class ConfirmationLivraisonNode(Node):
    def __init__(self):
        super().__init__('confirmation_livraison_node')
        # Créer un service pour confirmer la livraison
        self.srv = self.create_service(Trigger, 'confirmer_livraison', self.handle_livraison)

    def handle_livraison(self, request, response):
        response.success = True
        response.message = "Colis livré avec succès !"
        # Afficher un message dans les logs
        self.get_logger().info(response.message)
        return response

def main(args=None):
    rclpy.init(args=args)
    node = ConfirmationLivraisonNode()
    rclpy.spin(node)  # Le nœud attend les appels au service
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
