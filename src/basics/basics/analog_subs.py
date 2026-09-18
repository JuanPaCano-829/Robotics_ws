import rclpy  # Librería principal de ROS2 para Python
from rclpy.node import Node  # Clase para crear nodos
from std_msgs.msg import Int32  # Tipo de mensaje


class AnalogSubscriber(Node):
    def __init__(self):  # Constructor del nodo
        super().__init__('analog_subscriber')  # Nombre del nodo

        self.subscription_ = self.create_subscription(Int32, '/analog', self.analog_callback, 10)
        # Se suscribe al tópico /analog para recibir los valores del potenciómetro
        self.get_logger().info('Esperando datos')

    def analog_callback(self, msg):  # Se ejecuta cada vez que llega un mensaje nuevo
        valor = msg.data  # Extrae el valor numérico del mensaje
        self.get_logger().info(f'ADC = {valor}')  # Lo muestra en consola

def main(args=None):
    rclpy.init(args=args)  # Inicializa ROS2
    node = AnalogSubscriber()  # Crea el nodo
    rclpy.spin(node)  # Lo mantiene corriendo, esperando mensajes
    node.destroy_node()  # Destruye el nodo al terminar
    rclpy.shutdown()  # Cierra ROS2

if __name__ == '__main__':
    main()
