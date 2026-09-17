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
