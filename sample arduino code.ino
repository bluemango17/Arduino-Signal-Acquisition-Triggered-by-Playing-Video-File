

unsigned long previousMillis = 0;
const long interval = 10; // ako je 10 znači da je sampling rate 100 Hz
int i = 0;
void setup() {
  Serial.begin(74880);

}

void loop() {
  unsigned long currentMillis = millis();

  
  if (currentMillis - previousMillis >= interval) {
   previousMillis = currentMillis;
  int sensorValue = analogRead(A0);
    
  float voltage = sensorValue*5.0/1023.0;
  
  
  Serial.println(voltage);
  
  
  }
}
