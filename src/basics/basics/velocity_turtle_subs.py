import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class VelocityTurtleSubs(Node):

    def __init__(self):
        super().__init__('velocity_turtle_subs')

        # Escuchamos el mismo tópico al que le publica velocity_turtle_pub
        self.subscription_ = self.create_subscription(
            Twist, '/turtle1/cmd_vel', self.velocity_callback, 10)

    def velocity_callback(self, msg):
        # De todo el mensaje Twist, solo nos interesa la velocidad lineal en x
        velocidad = msg.linear.x
        self.get_logger().info(f'Vel = {velocidad:.1f} m/s')


def main(args=None):
    rclpy.init(args=args)
    node = VelocityTurtleSubs()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
