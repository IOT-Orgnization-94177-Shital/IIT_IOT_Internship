#define ADC 
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(LDR_PIN,INPUT);
  Serial.println("ADC set up is done");
}
void loop() {
  // put your main code here, to run repeatedly:
int value = analogRead(LDR_PIN);
Serial.printf("light intensity : %d\n",value);
delay(2000);
}
