/*
 * UIPEthernet TCPServer example.
 *
 * UIPEthernet is a TCP/IP stack that can be used with a enc28j60 based
 * Ethernet-shield.
 *
 * UIPEthernet uses the fine uIP stack by Adam Dunkels <adam@sics.se>
 *
 *      -----------------
 *
 * This Hello World example sets up a server at 192.168.1.6 on port 1000.
 * Telnet here to access the service.  The uIP stack will also respond to
 * pings to test if you have successfully established a TCP connection to
 * the Arduino.
 *
 * This example was based upon uIP hello-world by Adam Dunkels <adam@sics.se>
 * Ported to the Arduino IDE by Adam Nielsen <malvineous@shikadi.net>
 * Adaption to Enc28J60 by Norbert Truchsess <norbert.truchsess@t-online.de>
 */

#define MACADDRESS 0x00,0x01,0x02,0x03,0x04,0x05
#define MYIPADDR 192,168,1,40
#define MYIPMASK 255,255,255,0
#define MYDNS 192,168,1,1
#define MYGW 192,168,1,1
#define LISTENPORT 8080
#define UARTBAUD 115200


#include <UIPEthernet.h>
EthernetServer server = EthernetServer(LISTENPORT);

void setup(){
  uint8_t mac[6] = {MACADDRESS};
  uint8_t myIP[4] = {MYIPADDR};
  uint8_t myMASK[4] = {MYIPMASK};
  uint8_t myDNS[4] = {MYDNS};
  uint8_t myGW[4] = {MYGW};
//  Ethernet.begin(mac,myIP);
  Serial.begin(115200);
  Serial.println("init ethernet");
  Ethernet.begin(mac,myIP,myDNS,myGW,myMASK);
  Serial.println();
  server.begin();
}

void loop() {
  size_t size;

  if (EthernetClient client = server.available()){
   Serial.println("FOUND !!!!"); 
      while((size = client.available()) > 0){
          uint8_t* msg = (uint8_t*)malloc(size+1);
          memset(msg, 0, size+1);
          size = client.read(msg,size);
          free(msg);
        }
      client.stop();
    }
}
