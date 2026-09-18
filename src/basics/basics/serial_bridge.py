import rclpy  # Librería principal de ROS2 para Python
from rclpy.node import Node  # Clase para crear nodos
from std_msgs.msg import Int32  # Tipo de mensaje
import serial  # Librería para comunicación serial con la ESP32


class SerialBridge(Node):
    def __init__(self):  # Constructor del nodo
        super().__init__('serial_bridge')  # Nombre del nodo

        self.subscription_ = self.create_subscription(Int32, '/led_command', self.led_callback, 10)
        # Se suscribe a /led_command para recibir el estado que debe tener el LED

        self.serial_ = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
        # Abre la conexión serial con la ESP32

        self.get_logger().info('Esperando mensajes')

    def led_callback(self, msg):  # Se ejecuta cada vez que llega un mensaje nuevo
        if msg.data == 1:  # Si el mensaje pide encender
            self.serial_.write(b'1\n')  # Manda el 1 por serial a la ESP32
            self.get_logger().info('ROS 2 -> Serial: 1')

        elif msg.data == 0:  # Si el mensaje apaga
            self.serial_.write(b'0\n')  # Manda el 0 por serial a la ESP32
            self.get_logger().info('ROS 2 -> Serial: 0')


def main(args=None):
    rclpy.init(args=args)  # Inicializa ROS2
    node = SerialBridge()  # Crea el nodo
    rclpy.spin(node)  # Lo mantiene escuchando el tópico
    node.serial_.close()  # Cierra la conexión serial al terminar
    node.destroy_node()  # Destruye el nodo
    rclpy.shutdown()  # Cierra ROS2

if __name__ == '__main__':
    main()
