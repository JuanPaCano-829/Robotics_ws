#define VRX 34  // pin conectado eje X del joystick
#define VRY 35  // pin conectado eje Y del joystick

void setup() {
  Serial.begin(115200);  // comunicación serial a 115200 baudios
}

void loop() {
  int x = analogRead(VRX);  // lee el valor del eje X
  int y = analogRead(VRY);  // lee el valor analógico eje Y

  // envía ambos valores separados por coma
  Serial.print(x);
  Serial.print(",");
  Serial.println(y);

  delay(20);  // pausa para no saturar
}
