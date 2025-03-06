#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from sensor_msgs.msg import BatteryState
from std_srvs.srv import Trigger

class EmergencyHandler(Node):
    def __init__(self):
        super().__init__('emergency_handler')

        # Souscrire au topic 'battery_status'
        self.battery_subscription = self.create_subscription(
            BatteryState,
            'battery_status',
            self.battery_status_callback,
            10)

        # Créer un client pour le service 'return_to_base'
        self.return_to_base_client = self.create_client(Trigger, 'return_to_base')

        while not self.return_to_base_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service "return_to_base" non disponible, attente...')

    def battery_status_callback(self, msg):
        # Vérifier si la batterie est faible (par exemple < 20%)
        if msg.percentage < 20:
            self.get_logger().warn('Batterie faible, envoi du signal pour retourner à la base...')
            self.trigger_return_to_base()

    def trigger_return_to_base(self):
        # Appeler le service 'return_to_base'
        request = Trigger.Request()
        future = self.return_to_base_client.call_async(request)

        # Attendre la réponse du service
        future.add_done_callback(self.return_to_base_response)

    def return_to_base_response(self, future):
        try:
            response = future.result()
            if response.success:
                self.get_logger().info('Retour à la base activé avec succès.')
            else:
                self.get_logger().warn('Erreur dans l\'activation du retour à la base.')
        except Exception as e:
            self.get_logger().error(f'Exception lors de l\'appel du service: {e}')

def main(args=None):
    rclpy.init(args=args)
    node = EmergencyHandler()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
