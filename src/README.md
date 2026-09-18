# Robotics_ws — Velocity Publisher/Subscriber

## Alumno
Juan Pablo Cano Rubio

## Descripción
Esta actividad consiste en implementar dos nodos de ROS que se comunican mediante: un nodo publicador `velocity_publisher.py` que generalos valores que simulan la velocidad
y un nodo suscriptor `velocity_subscriber.py` que recibe estos valores
y los despliega en la terminal. El objetivo es comprobar el funcionamiento
del los nodos publicador/suscriptor usando las herramientas como `ros2 topic`, `ros2 node` y el grafo.

## Funcionamiento

### Publicador = velocity_publisher.py
El nodo `velocity_publisher` crea un publicador en el tópico `/velocity`. Usando un timer que se
ejecuta cada 1 seg. , después publica un valor de velocidad que empieza en 0
y se incrementa 0.1 con cada  ciclo hasta llegar a 1.5, aquí se 
reinicia a 0 para repetir el ciclo.

### Suscriptor = velocity_subscriber.py
El nodo `velocity_subscriber` se suscribe al tópico `/velocity` . Cada vez que llega un mensaje , el `velocity_callback` lo recibe y muestra el valor en
consola, seguido de la unidad en m/s.

## Comandos utilizados
ros2 run basics velocity_publisher
ros2 run basics velocity_subscriber
ros2 topic list
ros2 topic info /velocity
ros2 topic echo /velocity
ros2 topic hz /velocity
ros2 node list
ros2 node info /velocity_publisher
ros2 node info /velocity_subscriber
rqt_graph

## Problema
Al llegar a la velocidad de  1.5 y reiniciar a 0.0, aparece el
siguiente error tanto en el publicador como en el suscriptor:

python3: ./.obj-x86_64-linux-gnu/rosidl_generator_py/std_msgs/msg/_float32_s.c:58:
std_msgs__msg__float32__convert_from_py: Assertion `PyFloat_Check(field)' failed.
[ros2run]: Aborted

Se investigó el error y se determinó que corresponde a un problema conocido
a nivel de la librería `rclpy` en ROS. Se intentó recompliar el workspace, pero el error siguió, confirmando que no se trata de problemas en la compilación sino de un problema en el entorno.

## Video de evidencia
[https://drive.google.com/file/d/1trtEGrdVqCTSipwbotfSvsvO4Ny0M0_S/view?usp=sharing](https://drive.google.com/file/d/1VV_9rB2liUBDP6wEKo30pgkuDaUI1PI9/view?usp=sharing)

## Ejemplo LED  ROS2 y ESP32

### Descripción
Este ejemplo controla un LED físico conectado a una ESP32 desde ROS2,
usando comunicación serial como puente entre ambos.

### Cómo funciona
- `led_blink.py`: nodo que publica en el tópico `/led_command` (tipo
  `std_msgs/msg/Int32`) alternando entre 1 y 0 cada segundo mediante un timer.
- `serial_bridge.py`: nodo suscrito al mismo tópico `/led_command`; al recibir
  un mensaje, lo traduce y lo envía por puerto serie (`/dev/ttyUSB0` a 115200
  baudios) a la ESP32 como el carácter '1' o '0'.
- `LED_Serial.ino`: firmware de la ESP32 que lee el puerto serie y enciende
  o apaga el LED en el pin GPIO2 según el carácter recibido.

### Comandos utilizados
ros2 run basics serial_bridge
ros2 run basics led_blink
ros2 topic list
ros2 topic info /led_command
ros2 topic echo /led_command
ros2 node list
ros2 node info /led_blink
ros2 node info /serial_bridge
rqt_graph

### Video de evidencia — LED


## Ejemplo Potenciómetro ROS2 y ESP32

### Descripción
Este ejemplo lee el valor analógico de un potenciómetro conectado a una
ESP32 y lo transmite a ROS2 mediante comunicación serial, para ser
desplegado en tiempo real por un nodo suscriptor.

### Cómo funciona
- `ADC_Pot.ino`: firmware de la ESP32 que lee continuamente el valor
  analógico del potenciómetro conectado al pin GPIO15 (rango de 0 a 4095,
  ya que la ESP32 tiene un ADC de 12 bits) y lo envía por puerto serie
  cada 100ms.
- `analog_serial_pub.py`: nodo que abre la conexión serial con la ESP32
  (`/dev/ttyUSB0` a 115200 baudios), lee las líneas que llegan, y publica
  cada valor como un mensaje `std_msgs/msg/Int32` en el tópico `/analog`.
- `analog_subs.py`: nodo suscrito al tópico `/analog` que recibe cada
  valor y lo muestra en consola.

### Comandos utilizados
ros2 run basics analog_serial_pub
ros2 run basics analog_subs
ros2 topic list
ros2 topic info /analog
ros2 topic echo /analog
ros2 node list
ros2 node info /analog_serial_pub
ros2 node info /analog_subscriber
rqt_graph

### Video de evidencia — Potenciómetro
