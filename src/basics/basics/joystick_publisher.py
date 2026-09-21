import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray  # permite mandar un arreglo de enteros
import serial


class JoystickPublisher(Node):
    def __init__(self):
        super().__init__('joystick_publisher')

        # el publicador manda arreglos [x, y] al tópico /joystick_raw
        self.publisher_ = self.create_publisher(Int32MultiArray, '/joystick_raw', 10)

        # Conexión serial con la ESP32
        self.serial_ = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

        # Revisa el puerto serial cada 20ms 
        self.timer_ = self.create_timer(0.02, self.read_serial)
        self.get_logger().info('Joystick publisher iniciado')

    def read_serial(self):
        if self.serial_.in_waiting > 0:  # Si hay datos esperando
            linea = self.serial_.readline().decode(errors='ignore').strip()

            # Esperamos formato x,y que estan separamos por la coma
            partes = linea.split(',')
            if len(partes) == 2 and partes[0].isdigit() and partes[1].isdigit():
                x = int(partes[0])
                y = int(partes[1])

                msg = Int32MultiArray()
                msg.data = [x, y]  # ambos valores en el mensaje
                self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = JoystickPublisher()
    rclpy.spin(node)
    node.serial_.close()
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
