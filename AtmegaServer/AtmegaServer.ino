
#include <UIPEthernet.h>

EthernetClient client;

void setup() {
  Serial.begin(115200);
  Serial.println("Starting Server ");
  
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
}

void loop() {
  if(Serial.available()){
    String data = Serial.readString();
    client.connect(IPAddress(10,42,0,1),5000);
    client.print(data);
    size_t size = client.available();
    if(size){
      uint8_t* msg = (uint8_t*)malloc(size);
      size = client.read(msg,size);
      Serial.write(msg,size);
      free(msg);
    }
    client.stop();
  }else{
    client.connect(IPAddress(10,42,0,1),5000);
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
