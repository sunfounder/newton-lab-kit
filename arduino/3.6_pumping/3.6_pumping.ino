const int IN1 = 15; // GPIO pin connected to Input 1A
const int IN2 = 14; // GPIO pin connected to Input 2A

void setup() {
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
}

void loop() {
  // Turn the pump on
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  delay(5000); // Run for 5 seconds

  // Stop the pump
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  delay(5000); // Stop for 5 seconds
}