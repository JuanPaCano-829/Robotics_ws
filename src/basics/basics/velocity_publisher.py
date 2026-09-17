import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class VelocityPublisher(Node):

    def __init__(self): # se crea el Constructor
        super().__init__('velocity_publisher')  # Le da nombre al nodo

        self.publisher_ = self.create_publisher(  # Crea el publicador
            Float32, '/velocity', 10) # el 10 es el buffer

        self.Vel = 0.0 # Variable donde guardamos el valor de la velocidad 

        self.timer_ = self.create_timer(  # Crea el temporizador que cada 0.5 segundos publica la velocidad
            0.5,
            self.publish_velocity
        )

    def publish_velocity(self):  # Función que se ejecuta cada que el timer publica

        msg = Float32()

        msg.data = self.Vel  # Valor actual de velocidad

        self.publisher_.publish(msg) # Publica el mensaje en el tópico "/velocity"

        self.get_logger().info(  # Imprime en consola
            f'Vel = {self.Vel:.1f}'
        )

        if self.Vel < 1.5: # Si la velocidad no es 1.5
            self.Vel = round(self.Vel + 0.1, 1)  # Suma 0.1 y redondea a 1 decimal
        else:
            self.Vel = 0 # Reinicia la velocidad a 0


def main(args=None):

    rclpy.init(args=args) # Inicializa la comunicación

    node = VelocityPublisher()  # Instancia del nodo publicador

    rclpy.spin(node) # Mantiene el nodo corriendo y escuchando

    node.destroy_node() # elimina el nodo correctamente

    rclpy.shutdown()  # Cierra la comunicación


if __name__ == '__main__':
    main()

