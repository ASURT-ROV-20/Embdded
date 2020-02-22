
#include <UIPEthernet.h>
#include "utility/logging.h"

EthernetClient client;
unsigned long next;


void setup() {
  Serial.begin(115200);
  Serial.println("Hello");
  uint8_t mac[6] = {0x00,0x01,0x02,0x03,0x04,0x05};
  Ethernet.begin(mac); //Configure IP address via DHCP

  Serial.print("localIP: ");
  Serial.println(Ethernet.localIP());
  Serial.print("subnetMask: ");
  Serial.println(Ethernet.subnetMask());
  Serial.print("gatewayIP: ");
  Serial.println(Ethernet.gatewayIP());
  Serial.print("dnsServerIP: ");
  Serial.println(Ethernet.dnsServerIP());
  next = 0;
}

void loop() {
  long a = millis();
  if(Serial.available()){
    a = millis();
    String data = Serial.readString();
    Serial.print("Received Data => ");
    Serial.println(data);//display same received Data back in serial monitor.
    
    if (client.connect(IPAddress(10,42,0,1),5000)){
        client.print(data);
        size_t s = client.available();
        Serial.println(s);
        client.stop();
      }
      Serial.print("Time is ");
      Serial.println(millis() - a);
  }else{
    if (client.connect(IPAddress(10,42,0,1),5000)){
        client.print("{}");
        size_t size = client.available();
        if(size){
          uint8_t* msg = (uint8_t*)malloc(size);
          size = client.read(msg,size);
          Serial.write(msg,size);
          free(msg);
        }
        client.stop();
     }
  }
//  if(client.connect(IPAddress(10,42,0,1),5000)){
//    size_t s = client.available();
//    Serial.println(s);
//    client.stop();
//  }
  
  }
