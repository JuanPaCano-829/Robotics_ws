import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray


class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')

        self.subscription_ = self.create_subscription(
            Int32MultiArray, '/joystick_raw', self.joystick_callback, 10)

        self.get_logger().info('Turtle controller iniciado (modo prueba)')

    def joystick_callback(self, msg):
        x, y = msg.data[0], msg.data[1]
        # solo mostramos los valores recibidos para confirmar
        # que la comunicación entre nodos funciona
        self.get_logger().info(f'Recibido: x={x}, y={y}')


def main(args=None):
    rclpy.init(args=args)
    node = TurtleController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
