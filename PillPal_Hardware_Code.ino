#include <ESP32Servo.h>
const int redPin = 15;
const int greenPin = 4;
const int bluePin = 16;
const int buttonPin = 22;
const int med1Pin = 19;
const int med2Pin = 2;
const int buzzerPin = 23;
int buttonNew;
int buttonOld = 1;
int ledState = 0;
int dt = 100;
Servo med1;
Servo med2;

bool buttonPressed = 0;
int buttonCount = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  pinMode(buttonPin, INPUT);
  pinMode(buzzerPin, OUTPUT);
  med1.attach(med1Pin);
  med2.attach(med2Pin);

  digitalWrite(redPin, HIGH);
  digitalWrite(greenPin, LOW);
  digitalWrite(bluePin, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  checkButtonStatus();
  if(buttonPressed){
    giveMedicine(med1, 3);
    giveMedicine(med2, 2);
    digitalWrite(redPin, LOW);
    digitalWrite(greenPin, HIGH);
    digitalWrite(bluePin, LOW);
    buttonPressed = 0;
    buttonCount++;
  }
  else if(buttonPressed == 0 && buttonCount == 0){
  digitalWrite(buzzerPin, HIGH);
  delay(50);
  digitalWrite(buzzerPin, LOW);
  delay(50);
  }

}

void checkButtonStatus(){
  buttonNew = digitalRead(buttonPin);
  if(buttonOld == 0 && buttonNew == 1){
    if(ledState == 0){
      ledState = 1;
      buttonPressed = 1;
    }
    else{
      ledState = 0;
      buttonPressed = 1;

    }
  }
  buttonOld = buttonNew;
  delay(dt);
}

void giveMedicine(Servo &servo, int pills){
  while(pills > 0){
    servo.write(0);
    delay(2000);
    servo.write(180);
    delay(2000);
    pills--;
  }
}
