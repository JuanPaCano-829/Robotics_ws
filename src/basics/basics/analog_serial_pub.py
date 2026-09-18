import rclpy  # Librería principal de ROS2 para Python
from rclpy.node import Node  # Clase para crear nodos
from std_msgs.msg import Int32  # Tipo de mensaje
import serial  # Librería para comunicación serial con la ESP32


class AnalogSerialPublisher(Node):
    def __init__(self):  # Constructor del nodo
        super().__init__('analog_serial_pub')  # Nombre del nodo

        self.publisher_ = self.create_publisher(Int32, '/analog', 10)
        # Publicador que manda al tópico /analog el valor leído del potenciómetro

        self.serial_ = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
        # Abre la conexión serial con la ESP32

        self.timer_ = self.create_timer(0.01, self.read_serial)
        # Cada 0.01 seg revisa si llegó dato nuevo
        self.get_logger().info('ESP32 conectada')

    def read_serial(self):  # Se ejecuta con cada tick del timer
        if self.serial_.in_waiting > 0:  # Si hay datos esperando
            linea = self.serial_.readline().decode().strip()
            # Lee una línea y la convierte de bytes a texto y quita espacios/saltos de línea

            if linea.isdigit():  # Verifica que lo leído sea un número válido
                valor = int(linea)  # Convierte el texto a entero
                msg = Int32()  # Crea el mensaje
                msg.data = valor  # Le asigna el valor leído
                self.publisher_.publish(msg)  # Publica el valor en el tópico /analog

def main(args=None):
    rclpy.init(args=args)  # Inicializa ROS2
    node = AnalogSerialPublisher()  # Crea el nodo
    rclpy.spin(node)  # Lo mantiene corriendo
    node.serial_.close()  # Cierra la conexión serial al terminar
    node.destroy_node()  # Destruye el nodo
    rclpy.shutdown()  # Cierra ROS2

if __name__ == '__main__':
    main()
