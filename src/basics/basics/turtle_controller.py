import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray
from geometry_msgs.msg import Twist


# :::::::::::: Parametros de calibración ::::::::
CENTRO = 2048        # valor esperado joystick en reposo
RANGO = 2048         # distancia del centro al extremo
ZONA_MUERTA = 0.10   # 10% alrededor del centro
VEL_LINEAL_MAX = 2.0   # velocidad maxima de la tortuga
VEL_ANGULAR_MAX = 2.0  # velocidad angular máxima de la tortuga


class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')

        self.subscription_ = self.create_subscription(
            Int32MultiArray, '/joystick_raw', self.joystick_callback, 10)

        # Publicador hacia la tortuga de turtlesim
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        self.get_logger().info('Turtle controller iniciado')

    def normalizar(self, valor):
        # convierte el valor crudo a un rango -1.0 a 1.0
        normalizado = (valor - CENTRO) / RANGO

        # Zona muerta si está muy cerca del centro es 0
        if abs(normalizado) < ZONA_MUERTA:
            return 0.0

        # recorta el valor para que no pase de -1.0 o 1.0
        return max(-1.0, min(1.0, normalizado))

    def joystick_callback(self, msg):
        x_crudo, y_crudo = msg.data[0], msg.data[1]

        x_norm = self.normalizar(x_crudo)  # controla giro
        y_norm = self.normalizar(y_crudo)  # controla avance

        twist = Twist()
        twist.linear.x = y_norm * VEL_LINEAL_MAX      # adelante/atras
        twist.angular.z = -x_norm * VEL_ANGULAR_MAX   # izquierda/derecha
        # el signo negativo en angular porque como este
        # orientado el joystick mover a la derecha debe girar en sentido horario

        self.publisher_.publish(twist)
        self.get_logger().info(
            f'x={x_crudo} y={y_crudo} -> lineal={twist.linear.x:.2f} angular={twist.angular.z:.2f}'
        )


def main(args=None):
    rclpy.init(args=args)
    node = TurtleController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
