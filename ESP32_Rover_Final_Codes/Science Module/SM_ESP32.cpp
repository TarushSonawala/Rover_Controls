#include <Arduino.h>
#include <iostream>
#include <string>

HardwareSerial Receiver(0);

std::string buffer = "";

const int freq = 5000;
const int channel1 = 0;
const int channel2 = 1;
const int channel3 = 2;
const int resolution = 8;

#define relay1 21
#define relay2 19
#define relay3 18
#define relay4 5
#define water_heater 17
#define stepper_step 23
#define stepper_dir 22 ///
#define auger_pwm 14
#define auger_dir 27
#define auger_rot_pwm 13
#define auger_rot_dir 15
#define senser_suit_pwm 33
#define senser_suit_dir 32

char sm = '0';

void setup()
{

  Serial.begin(115200);
  Receiver.begin(115200);

  delay(1000);

  pinMode(relay1, OUTPUT);          // relay 1
  pinMode(relay2, OUTPUT);          // relay 2
  pinMode(relay3, OUTPUT);          // relay 3
  pinMode(relay4, OUTPUT);          // relay 4
  pinMode(water_heater, OUTPUT);    // water heater
  pinMode(stepper_step, OUTPUT);    // stepper step
  pinMode(stepper_dir, OUTPUT);     // stepper direction
  pinMode(auger_dir, OUTPUT);       // auger actuation direction
  pinMode(auger_rot_dir, OUTPUT);   // auger rotation direction
  pinMode(senser_suit_dir, OUTPUT); // sensor suite direction

  ledcSetup(channel1, freq, resolution);
  ledcSetup(channel2, freq, resolution);
  ledcSetup(channel3, freq, resolution);

  ledcAttachPin(auger_pwm, channel1);       // auger actuation PWM
  ledcAttachPin(auger_rot_pwm, channel2);   // auger rotation PWM
  ledcAttachPin(senser_suit_pwm, channel3); // sensor suite PWM


  ledcWrite(channel1, 0);
  ledcWrite(channel2, 0);
  ledcWrite(channel3, 0);
  digitalWrite(relay1, LOW);
  digitalWrite(relay2, LOW);
  digitalWrite(relay3, LOW);
  digitalWrite(relay4, LOW);
  digitalWrite(water_heater, LOW);
  digitalWrite(stepper_step, LOW);
  digitalWrite(stepper_dir, LOW);
  digitalWrite(auger_dir, LOW);
  digitalWrite(auger_rot_dir, LOW);
  digitalWrite(senser_suit_dir, LOW);
}

void loop()
{
  while (Receiver.available())
  {
    char RxdChar = Receiver.read();
    Serial.println(RxdChar);
    SMControl(RxdChar);
  }
  delay(100);
}


void SMControl(char buffer)
{
  switch (buffer)
  {
    case '0': // safety
      ledcWrite(channel1, 0);
      ledcWrite(channel2, 0);
      ledcWrite(channel3, 0);
      digitalWrite(relay1, LOW);
      digitalWrite(relay2, LOW);
      digitalWrite(relay3, LOW);
      digitalWrite(relay4, LOW);
      digitalWrite(water_heater, LOW);
      digitalWrite(stepper_step, LOW);
      digitalWrite(stepper_dir, LOW);
      digitalWrite(auger_dir, LOW);
      digitalWrite(auger_rot_dir, LOW);
      digitalWrite(senser_suit_dir, LOW);
      break;

    case '1': // relay 1,2,3,4
      Serial.println("Hey its chutiya tarush");
      digitalWrite(relay1, HIGH);
      digitalWrite(relay2, HIGH);
      digitalWrite(relay3, HIGH);
      digitalWrite(relay4, HIGH);
      break;

    case '2': // water heater
      digitalWrite(water_heater, HIGH);
      break;

    case '3': // servo rotate
      Serial.println("Hey its 3 cute fkers");

      digitalWrite(stepper_step, HIGH);
      delayMicroseconds(5000);
      digitalWrite(stepper_step, LOW);
      delayMicroseconds(5000);
      break;

    case '4': // servo direction toggle
      digitalWrite(stepper_dir, !digitalRead(stepper_dir));
      delay(100);
      // may have to add delay
      break;

    case '5': // auger down with rotation
      Serial.println("Hey its 500 mo-fkers");
      for (int i = 0; i < 500; i++) {


        digitalWrite(auger_dir, HIGH);
        digitalWrite(auger_rot_dir, HIGH);
        ledcWrite(channel1, 255);
        ledcWrite(channel2, 255);
      }
      break;

    case '6': // auger up]
      for (int i = 0; i < 500; i++)
      {

        digitalWrite(auger_dir, LOW);
        digitalWrite(auger_rot_dir, LOW);
        ledcWrite(channel1, 255);
        ledcWrite(channel2, 0);
      }
      break;

    case '7': // auger rotation for deposition
      for (int i = 0; i < 500; i++)
      {

        digitalWrite(auger_dir, LOW);
        digitalWrite(auger_rot_dir, LOW);
        ledcWrite(channel1, 0);
        ledcWrite(channel2, 255);
      }
      break;

    case '8': // sensor suite up
      for (int i = 0; i < 500; i++)
      {

        digitalWrite(senser_suit_dir, HIGH);
        ledcWrite(channel3, 255);
      }
      break;

    case '9': // sensor suite down
      for (int i = 0; i < 500; i++)
      {

        digitalWrite(senser_suit_dir, LOW);
        ledcWrite(channel3, 255);
      }
      break;

    default:
      ledcWrite(channel1, 0);
      ledcWrite(channel2, 0);
      ledcWrite(channel3, 0);
      break;
  }
}
