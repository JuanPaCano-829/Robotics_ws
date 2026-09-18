import rclpy  # Librería principal de ROS2 para Python
from rclpy.node import Node  # Clase para crear nodos
from std_msgs.msg import Int32  # Tipo de mensaje


class LedBlink(Node):
    def __init__(self):  # Constructor nodo
        super().__init__('led_blink')  # Nombre del nodo en ROS2
        self.publisher_ = self.create_publisher(Int32, '/led_command', 10)
        # Publicador que manda mensajes al "/led_command"

        self.estado = 1  # Variable que guarda si el LED debe estar en 1 o 0
        self.timer_ = self.create_timer(1.0, self.blink_callback)  # Cada 1 seg llama a blink_callback
        self.get_logger().info('Nodo iniciado')
        self.publicar_estado()  # Publica el estado inicial 1 apenas arranca

    def blink_callback(self):  # Se ejecuta cada vez que se cumple el timer
        if self.estado == 1:  # Si encendido
            self.estado = 0  # apaga
        else:  # Si apagado
            self.estado = 1  # enciende

        self.publicar_estado()  # Publica nuevo estado

    def publicar_estado(self):  # Función que crea y publica el mensaje
        msg = Int32()  # Crea un mensaje vacío 
        msg.data = self.estado  # Le asigna el estado actual 1 o 0

        self.publisher_.publish(msg)  # Publica el mensaje
        self.get_logger().info(f'Publicando: {self.estado}')  # Muestra en consola el mensaje

def main(args=None):
    rclpy.init(args=args)  # Inicializa ROS2
    node = LedBlink()  # Crea el nodo
    rclpy.spin(node)  # Lo mantiene escuchando
    node.destroy_node()  # Destruye el nodo
    rclpy.shutdown()  #  cierre 

if __name__ == '__main__':
    main()
