#include <OneWire.h>
#include <DallasTemperature.h>

#include <ESP8266WiFi.h>

using namespace std;

#define N 0
#define ONE_WIRE_BUS 2 // Data wire is plugged into pin 2 on the Arduino
OneWire oneWire(ONE_WIRE_BUS); // Setup a oneWire instance to communicate with any OneWire devices (not just Maxim/Dallas temperature ICs)
DallasTemperature sensors(&oneWire); // Pass our oneWire reference to Dallas Temperature. 



const char *ssid = "N+1_ssid"; //ssid and password of next chain
const char *password = "N+1_password";


void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  sensors.begin(); 
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print("no connection\n");
    delay(500);
  }

}


void loop() {
  // put your main code here, to run repeatedly:
  // Use WiFiClient class to create TCP connections
  WiFiClient client;
  const char * host = "192.168.4.1"; 
  const int httpPort = 80;
  if (!client.connect(host, httpPort)) {
    Serial.println("connection failed");
    return;
  }
  
   // This will send the request to the server
   
if (client.connected()) { // check if connection exists
  Serial.print("Requesting temperatures...\n");
  sensors.requestTemperatures(); // Send the command to get temperatures
  Serial.println("DONE");
  float temp = sensors.getTempCByIndex(0);
  Serial.print("Temperature for Device 1 is: ");
  Serial.print(String(temp) + "\n");
  
  String url = "/data/";
  url += "?sensors_reading=";
  url = url + String(N) + '=' + String(temp);
  client.print(String("GET ") + url + " HTTP/1.1\r\n" +
    "Host: " + host + "\r\n" +
    "Connection: close\r\n\r\n");
}    
else {     
      Serial.println("No server available");                                   
 }


  delay(1000);

}
