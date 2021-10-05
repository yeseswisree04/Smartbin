#include <ESP8266HTTPClient.h>
#include <ESP8266TelegramBOT.h>

#include <Adafruit_MQTT_FONA.h>
#include <Adafruit_MQTT.h>
#include <Adafruit_MQTT_Client.h>

#include <ESP8266WiFi.h>
#include <TinyGPS++.h>


#include <SoftwareSerial.h>






// Wifi network station credentials
#define WIFI_SSID "wifi_extender_2GHz" //"vivo-1906"
#define WIFI_PASSWORD "niranjan1" //"yesh1234"


#define CHAT_ID "@Smartbin1" //"1250660054"
#define BOT_TOKEN "1925206689:AAEtSxswtMrbicRhJCJeYgimZs6B8WzY9Vc" //"1790495847:AAGG3w7ZupMFjVzqd-YlxAtFNtsZoXthMg4"
#define botname "Bin1" //"Smart-bin"
#define username "Binn1_bot" //"cleverbin_bot"
TelegramBOT bot(BOT_TOKEN,botname,username);


// Choose two Arduino pins to use for software serial
int RXPin = 5;
int TXPin = 4;
String latitude_str,longitude_str,link,text;

int GPSBaud = 9600;

// Create a TinyGPS++ object
//TinyGPSPlus gps;
//
//// Create a software serial port called "gpsSerial"
//SoftwareSerial gpsSerial(RXPin, TXPin);

const int trigPin = 12;
const int echoPin = 14;
#define SOUND_VELOCITY 0.034

long duration;
float distance;
int total_distance=17;
String percentage;

void setup() {
  Serial.begin(115200);
  Serial.println();

 // attempt to connect to Wifi network:
  Serial.print("Connecting to Wifi SSID ");
  Serial.print(WIFI_SSID);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED)
  {
    Serial.print(".");
    delay(500);
  }
  
  Serial.print("\nWiFi connected. IP address: ");
  Serial.println(WiFi.localIP());
//  gpsSerial.begin(GPSBaud);

  pinMode(trigPin,OUTPUT);
  pinMode(echoPin,INPUT);
}
void handleMessage(String message, String chatId) {

    bot.sendMessage(chatId,message,"");
    
}




void loop() { 

  //connect to HTTP url
  WiFiClient client;
  HTTPClient http;
  http.begin(client,"http://192.168.0.100:80/update1");
  http.addHeader("Content-Type", "test/plain");

  
 // Clears the trigPin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  
  // Calculate the distance
  distance = duration * SOUND_VELOCITY/2;
 percentage = String(100-((distance/total_distance)*100));

 //Serial.println(distance);
//String message = link ;
// while (gpsSerial.available() > 0)
//    if (gps.encode(gpsSerial.read()))
 //    displayInfo();
//      
//
//  // If 5000 milliseconds pass and there are no characters coming in
//  // over the software serial port, show a "No GPS detected" error
//  if (millis() > 5000 && gps.charsProcessed() < 10)
//  {
//    Serial.println("No GPS detected");
//    while(true);
//  }


    if(distance<=4){

    String bin_id = "B3";
    String bin_status = "FILLED";
    latitude_str=String("17.3118776");
    longitude_str=String("78.5262079");
    String link = "http://maps.google.com/maps?q="+latitude_str+","+longitude_str;
//    String text="garbage is "+percentage+"% full need maintanence";
    
                
//    Serial.print(text);
//     Serial.print("\n");
//     Serial.print(link);
//    Serial.println(distance);
//    handleMessage(text,CHAT_ID);
//    Serial.println("text sent");
//    handleMessage(link,CHAT_ID);
//    Serial.println("link sent");

     int httpCode = http.POST(bin_id + " " + bin_status + " " +"CONTACTED" +" "+ link);
//     String payload = http.getString();
     
     Serial.println(httpCode);
//     Serial.println(payload);
    
    while(true){
      digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);  

  distance = duration * SOUND_VELOCITY/2;

        if(distance>20){
//          String text="Bin is Empty.";
//
//          handleMessage(text,CHAT_ID);
          
          Serial.println("Breaking from Infinite Loop");
          bin_status = "EMPTY";
          int httpCode = http.POST(bin_id + " " + bin_status + " " +"CONTACTED" +" "+ link);
//          String payload = http.getString();
     
         Serial.println(httpCode);
//         Serial.println(payload);
          break;}
        }

    }

}
