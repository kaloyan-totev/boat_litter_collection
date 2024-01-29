#include <Servo.h>

Servo leftMotor;
Servo rightMotor;
int pos = 0;

int zeroSpeed = 90;
int maxSpeed = 120;
int minSpeed = 60;

void setup() {
  Serial.begin(9600);
  leftMotor.attach(9);
  rightMotor.attach(10);

/*Serial.println("Zero Throttle");
leftMotor.write(zeroSpeed);  // Set the output to the middle or "zero" position. CONNECT THE ESC DURING THIS DELAY!!
rightMotor.write(zeroSpeed);
delay(5000);       // This delay allows the ESC to be connected and powered on. The motor will beep once on
                    // power up and once when it recognises the zero position.

Serial.println("Max");
leftMotor.write(maxSpeed); // Make sure your test bed is safe for the motor to turn at this point. It will run at maximum speed!
rightMotor.write(maxSpeed);
delay(2000);

Serial.println("Zero");
leftMotor.write(zeroSpeed); // Simulates the receiver sending a zero throttle signal again
rightMotor.write(zeroSpeed);
delay(2000);
*/


Serial.println("Setup Complete");
  
  Serial;
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB
  }
  //pinMode(LED_BUILTIN, OUTPUT);
}

void go_left(){
 rightMotor.write(maxSpeed);
}

void go_right(){
 leftMotor.write(maxSpeed);
}
void go_forward(){
 leftMotor.write(maxSpeed);
 rightMotor.write(maxSpeed);
}

void stop_left_motor(){
 leftMotor.write(zeroSpeed);
}

void stop_right_motor(){
 rightMotor.write(zeroSpeed);
}

void stop_motors(){
 rightMotor.write(minSpeed);
 delay(20);
 leftMotor.write(minSpeed);
}

void loop() {
  char c;
  Serial.print(c);
  if (Serial.available() > 0) {
    c = Serial.read();
    switch (c) {
    case '0':
      stop_motors();
      Serial.println("stop_motors");
      Serial.write("A", 1);
      break;
    case '1':
      go_forward();
      Serial.println("go_forward");
      Serial.write("A", 1);
      break;
    case '2':
      go_right();
      Serial.println("go_right");
      Serial.write("A", 1);
      break;
    case '3':
      go_left();
      Serial.println("go_left");
      Serial.write("Arrrr", 1); // a - allright
      break;
    default:
      Serial.write("E", 1); // error
      stop_motors();
      Serial.println("stop_motors");
      break;    
    }
  } else {
    //Serial.write("W", 1); // w - waiting to connect
    //Serial.println();
    //stop_motors();
  }
}
