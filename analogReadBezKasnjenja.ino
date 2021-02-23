 /*
  AnalogReadSerial + BlinkWithoutDelay
  kombinacijom ova dva koda nastao je ovaj jedan
  ideja je da frekvencija odabiranja bude fiksna, odnosno
  da se na svakih interval milisekundi šalje po jedan
  odbirak na serijski port, a da se on kasnije snimi u R-u.
*/

unsigned long previousMillis = 0;
const long interval = 100; // ako je 10 znači da je sampling rate 100 Hz

void setup() {
  Serial.begin(9600);
}

void loop() {
  unsigned long currentMillis = millis();
  
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;
    int sensorValue = analogRead(A0);
  float voltage = sensorValue * (5.0 / 1023.0);
  Serial.println(voltage);
  }
}
