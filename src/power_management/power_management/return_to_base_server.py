#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger

class ReturnToBaseServer(Node):
    def __init__(self):
        super().__init__('return_to_base_server')
        self.srv = self.create_service(Trigger, 'return_to_base', self.return_to_base_callback)

    def return_to_base_callback(self, request, response):
        self.get_logger().info('Service "return_to_base" appelé, retour à la base...')
        response.success = True
        response.message = 'Retour à la base activé.'
        return response

def main(args=None):
    rclpy.init(args=args)
    node = ReturnToBaseServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
