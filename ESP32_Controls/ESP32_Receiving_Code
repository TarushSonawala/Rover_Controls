#include <Arduino.h>
#include <WiFi.h>

const char *ssid = "Trace Paradox";
const char *password = "meowmeow";

WiFiServer wifiServer(8000);
char rxData = 0;
void setup()
{
    Serial.begin(9600);
    delay(1000);
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(1000);
        Serial.println("Connecting to WiFi..");
    }
    Serial.println("Connected to the WiFi network");
    Serial.println(WiFi.localIP());
    wifiServer.begin();
}

void loop()
{

    WiFiClient client = wifiServer.available();
    if (client)
    {   
        while (client.connected())
        {
            while (client.available() > 0)
            {
                rxData = client.read();
                Serial.println(rxData);
                // client.write(rxData);
            }
            delay(10);
        }
        client.stop();
        Serial.println("Client disconnected");
    }
}
