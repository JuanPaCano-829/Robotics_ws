import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class VelocitySubscriber(Node):

    def __init__(self): # Constructor
        super().__init__('velocity_subscriber')  # Nombre del nodo
        self.subscription_ = self.create_subscription(Float32,'/velocity',self.velocity_callback,10) # Crea la suscripción

    def velocity_callback(self, msg):  # Función que se ejecuta cada vez que llega un mensaje
        Velocity = msg.data # Extrae el valor numérico del mensaje
        self.get_logger().info(f'Vel = {Velocity:.1f} m/s') # Lo imprime en consola con 1 decimal


def main(args = None):
    rclpy.init(args=args)  # Inicializa comunicación
    node = VelocitySubscriber() # Instancia nodo suscriptor
    rclpy.spin(node) # Mantiene el nodo corriendo y esperando mensajes
    node.destroy_node()  # Elimina el nodo correctamente
    rclpy.shutdown() # Cierra la comunicación


if __name__ == '__main__':
    main()
