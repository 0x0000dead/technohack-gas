#include <ESP8266WebServer.h>
#include <ESP8266WiFi.h>

#include <OneWire.h>
#include <DallasTemperature.h>




using namespace std;

#define N 1 // Module number (id)
#define ONE_WIRE_BUS 0 // Data wire is plugged into pin 2 on the Arduino
OneWire oneWire(ONE_WIRE_BUS); // Setup a oneWire instance to communicate with any OneWire devices (not just Maxim/Dallas temperature ICs)
DallasTemperature sensors(&oneWire); // Pass our oneWire reference to Dallas Temperature. 


const char *current_ssid = "N_ssid";  
const char *current_password = "N_password";

const char *next_ssid = "N+1_ssid";
const char *next_password = "N+1_password";



ESP8266WebServer server(80);

void handleSentVar() {
  if (server.hasArg("sensors_reading")) { // This is the variable sent from the client

    String data = server.arg("sensors_reading");
    Serial.print("Requesting temperatures...\n");
    sensors.requestTemperatures(); // Send the command to get temperatures
    Serial.println("DONE");
  
    Serial.print("Temperatures is: ");
    String temperatures_to_send = data + ' ' + String(N) + '=' + sensors.getTempCByIndex(0);
    Serial.print(temperatures_to_send + "\n");
    
    server.send(200, "text/html", "Data received");

    WiFiClient client;
    const char * host = "192.168.137.1"; 
    const int httpPort = 80;
    if (!client.connect(host, httpPort)) {
      Serial.println("connection failed");
    return;
    }

  if (client.connected()) { // Check if connection exists
    
    String url = "/data/";
    url += "?sensors_reading=";
    url = url + temperatures_to_send;
    client.print(String("GET ") + url + " HTTP/1.1\r\n" +
      "Host: " + host + "\r\n" +
      "Connection: close\r\n\r\n");
  }    
  else {     
        Serial.println("No server available");                                   
  }

  }
}


void setup() {
  // Put your setup code here, to run once:
  Serial.begin(115200);
  Serial.println();

  //Connect to N + 1 module
  WiFi.mode(WIFI_AP);
  WiFi.begin(next_ssid, next_password);
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print("no connection\n");
    delay(500);
  }

  //for N - 1 module 
  WiFi.mode(WIFI_AP_STA);
  Serial.print("Setting soft-AP ... ");
  Serial.println(WiFi.softAP(current_ssid,current_password) ? "Ready" : "Failed!");

  Serial.print("Soft-AP IP address = ");
  Serial.println(WiFi.softAPIP());
  
  
  server.on("/data/", HTTP_GET, handleSentVar); // When the server receives a request with /data/ in the string then run the handleSentVar function
  server.begin();
  

}


void loop() {
  // put your main code here, to run repeatedly:
  server.handleClient();


  delay(500);
}
