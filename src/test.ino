#include <ESP32Servo.h>

int en2 = 17;
int en1 = 16;
int enA = 18;
int servo = 26;
bool flag;
bool flag2;

Servo smukservo;

void setup() {
  // put your setup code here, to run once:
Serial.begin(115200);
pinMode(en1, OUTPUT);
pinMode(en2, OUTPUT);
ledcAttach(enA, 12000, 8);
pinMode(servo, OUTPUT);
smukservo.attach(servo);
smukservo.write(110);
}

void loop()
{
  byte n = Serial.available(); //check if charctaer(s)has been accumulated in buffer
  if ( n != 0) //there is at least onr charcater in the buffer
  {
    char colourinput = Serial.read();
    Serial.print(colourinput);
    if (colourinput == 'f') //checking if it is f
    {
        Serial.print("forward");
        digitalWrite(en1, HIGH);
        digitalWrite(en2, LOW);
    }
    if (colourinput == '5') //checking if it is f
    {
        Serial.print("forward5");
        int pwmValue = map(5, 1, 9, 0, 255); // Map number to PWM range
        ledcWrite(enA, pwmValue);
        digitalWrite(en1, HIGH);
        digitalWrite(en2, LOW);
    }
    if (colourinput == '7') //checking if it is f
    {
        Serial.print("forward7");
        int pwmValue = map(9, 1, 9, 0, 255); // Map number to PWM range
        ledcWrite(enA, pwmValue);
        digitalWrite(en1, HIGH);
        digitalWrite(en2, LOW);
    }
    if (colourinput == 'b') //checking if it is b
    {
        Serial.print("backward");
        digitalWrite(en1, LOW);
        digitalWrite(en2, HIGH);
    }

    if (colourinput == 's') //checking if it is s
    {
        Serial.print("stop");
        digitalWrite(en1, LOW);
        digitalWrite(en2, LOW);
    }
    if (colourinput == 'c')
    {
      Serial.print("center");
      smukservo.write(110);
    }
    if (colourinput ==  'r')
    {
      Serial.print("right");
      smukservo.write(150);
    }
    if (colourinput == 'l')
    {
      Serial.print("left");
      smukservo.write(80);
    }
    else
    {
      Serial.print("INVALID");
    }
  }
}
