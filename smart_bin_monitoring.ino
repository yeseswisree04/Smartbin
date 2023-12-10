#include <ESP8266WiFi.h>
#include <ESP8266TelegramBOT.h>
#include <TinyGPS++.h>
#include <SoftwareSerial.h>

// Wifi network station credentials
#define WIFI_SSID "vivo-1906"
#define WIFI_PASSWORD "yesh1234"


#define CHAT_ID "1250660054"
#define BOT_TOKEN "1790495847:AAGG3w7ZupMFjVzqd-YlxAtFNtsZoXthMg4"
#define botname "Smart-bin"
#define username "cleverbin_bot"
TelegramBOT bot(BOT_TOKEN,botname,username);


// Choose two Arduino pins to use for software serial
int RXPin = 5;
int TXPin = 4;
String latitude_str,longitude_str,link,text;

int GPSBaud = 9600;

// Create a TinyGPS++ object
TinyGPSPlus gps;

// Create a software serial port called "gpsSerial"
SoftwareSerial gpsSerial(RXPin, TXPin);

#define echopin 12
#define trigpin 14

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
  gpsSerial.begin(GPSBaud);

  pinMode(trigpin,OUTPUT);
  pinMode(echopin,INPUT);
}
void handleMessage(String message, String chatId) {

    bot.sendMessage(chatId,message,"");
    
}




void loop() { 
 digitalWrite(trigpin,LOW);
 delayMicroseconds(3000);

 digitalWrite(trigpin,HIGH);
 delayMicroseconds(3000);
 digitalWrite(trigpin,LOW);


 duration=pulseIn(echopin,HIGH);


 distance=duration*0.034/2;
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
    latitude_str=String("17.3118776");
    longitude_str=String("78.5262079");
    String link = "http://maps.google.com/maps?q="+latitude_str+","+longitude_str;
    String text="garbage is"+percentage+"%full need maintanence";
                
    Serial.print(text);
    // Serial.print("\n");
    // Serial.print(link);
    handleMessage(text,CHAT_ID);
    Serial.println("text sent");
    handleMessage(link,CHAT_ID);
    Serial.println("link sent");
    delay(10000);
    }

}
