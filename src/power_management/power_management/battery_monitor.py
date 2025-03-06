#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from sensor_msgs.msg import BatteryState
from random import randint  # Pour générer un niveau de batterie aléatoire

class BatteryMonitor(Node):
    def __init__(self):
        super().__init__('battery_monitor')

        # Publier l'état de la batterie
        self.battery_publisher = self.create_publisher(BatteryState, 'battery_status', 10)

        # Publier l'état de la livraison
        self.delivery_publisher = self.create_publisher(String, 'delivery_status', 10)

        # Timer qui simule l'envoi de l'état de la batterie et de la livraison toutes les 1 seconde
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        # Créer un message pour l'état de la batterie
        battery_msg = BatteryState()
        battery_msg.voltage = 12.5  # Exemple de tension
        battery_msg.current = 3.5   # Exemple de courant
        battery_msg.percentage = float(randint(0, 100))  # Niveau de batterie aléatoire (0-100%) converti en float
  # Niveau de batterie aléatoire (0-100%)
        self.get_logger().info(f"Battery Status: {battery_msg.percentage}%")

        # Publier l'état de la batterie
        self.battery_publisher.publish(battery_msg)

        # Créer un message pour l'état de la livraison
        delivery_msg = String()
        delivery_msg.data = "Delivery in progress"
        self.get_logger().info("Delivery Status: Delivery in progress")

        # Publier l'état de la livraison
        self.delivery_publisher.publish(delivery_msg)

def main(args=None):
    rclpy.init(args=args)
    node = BatteryMonitor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
