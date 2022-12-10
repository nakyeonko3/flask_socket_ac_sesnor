#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <iostream>

// Update these with values suitable for your network.

const char* ssid = "KNU_WLAN_Open";
const char* password = "beyondme";
const char* mqtt_server = "nakyeonkopi.local";

// const char* ssid = "215";
// const char* password = NULL;
// const char* mqtt_server = "nakyeonkopi.local";

WiFiClient espClient;
PubSubClient client(espClient);
long lastMsg = 0;
char msg[50];
int value = 0;
int led = 13;

int readValue = 0;

void setup() {
  pinMode(led, OUTPUT);     // Initialize the led pin as an output
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
}

void setup_wifi() {

  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();

  // Switch on the LED if an 1 was received as first character
  if ((char)payload[0] == '1') {
    digitalWrite(led, LOW);   // Turn the LED on (Note that LOW is the voltage level
    // but actually the LED is on; this is because
    // it is acive low on the ESP-01)
  } else {
    digitalWrite(led, HIGH);  // Turn the LED off by making the voltage HIGH
  }

}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    if (client.connect("ESP8266Client_ac_sensor")) {
      Serial.println("connected");
      // Once connected, publish an announcement...
      client.publish("ac_sensor_outTopic", "ac_sensor_start");
      // ... and resubscribe
      client.subscribe("ac_sensor_inTopic");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}
void loop() {

  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  long now = millis();
  if (now - lastMsg > 2000) {
    lastMsg = now;
    ++value;
    readValue= analogRead(A0);
    int A = map(readValue,0,573,0,20000)*220*0.01;
    std::sprintf(msg, "%d", A);
    Serial.print("Publish message: ");
    Serial.println(msg);
    client.publish("ac_sensor_outTopic", msg);
  }
}