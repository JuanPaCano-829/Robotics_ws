import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
# Twist es el tipo de mensaje que usa turtlesim para moverse (tiene velocidad lineal y angular)


class VelocityTurtlePub(Node):

    def __init__(self):
        super().__init__('velocity_turtle_pub')

        # Publicamos directo al tópico que escucha la tortuga de turtlesim
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.Vel = 0.0
        self.timer_ = self.create_timer(0.5, self.publish_velocity)  # cada 0.5 segundos

    def publish_velocity(self):
        msg = Twist()

        if self.Vel >= 1.2:
            # Ya llegamos al límite: mandamos velocidad 0 para detener la tortuga
            msg.linear.x = 0.0
            self.publisher_.publish(msg)
            self.get_logger().info('Vel = 0.0 (tortuga detenida)')
            self.timer_.cancel()  # dejamos de publicar, el ciclo terminó
        else:
            # Seguimos incrementando la velocidad translacional (eje x)
            msg.linear.x = self.Vel
            self.publisher_.publish(msg)
            self.get_logger().info(f'Vel = {self.Vel:.1f}')
            self.Vel = round(self.Vel + 0.1, 1)


def main(args=None):
    rclpy.init(args=args)
    node = VelocityTurtlePub()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
