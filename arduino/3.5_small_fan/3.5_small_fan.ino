const int IN1 = 15; // GPIO pin connected to Input 1A
const int IN2 = 14; // GPIO pin connected to Input 2A

void setup() {
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
}

void loop() {
  // Rotate motor clockwise
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  delay(2000); // Run for 2 seconds

  // Stop motor
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  delay(1000); // Stop for 1 second

  // Rotate motor counterclockwise
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  delay(2000); // Run for 2 seconds

  // Stop motor
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  delay(1000); // Stop for 1 second
}