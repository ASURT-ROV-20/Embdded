#include <UIPEthernet.h>
//#define IP   192,168,1,109
//#define PORT 5000

#define StringCompare(str) !strncmp(buffer,str,index-1) 
#define IDLE_STATE 0
#define GET_IP_1_STATE 1
#define GET_IP_2_STATE 2
#define GET_IP_3_STATE 3
#define GET_IP_4_STATE 4
#define GET_PORT_STATE 5

int ipData[5];
uint8_t state = 0;
bool send = false;
EthernetClient client;
char buffer [256];
size_t index;


void etherSend(char *buffer, size_t index){
  client.connect(IPAddress(ipData[0],ipData[1], ipData[2], ipData[3]), ipData[4]);
  client.write(buffer, index);
  size_t size = client.available();
  if(size){
    uint8_t* msg = (uint8_t*)malloc(size);
    size = client.read(msg,size);
    Serial.write(msg,size);
    free(msg);
  }
  client.stop();
}

void idleState(){
  if(StringCompare("AT")){
    Serial.println("OK");
  }else if(StringCompare("AT+START")){
    Serial.println("STARTING ETHERNET");
    uint8_t mac[6] = {0x00,0x01,0x02,0x03,0x04,0x05};
    Ethernet.begin(mac);
    Serial.print("localIP: ");
    Serial.println(Ethernet.localIP());
  }else if(StringCompare("AT+CONNECT")){
    state = GET_IP_1_STATE;
  }else if(StringCompare("AT+SEND")){
    send = true;
  }else{
    if(send) etherSend(buffer, index);
    Serial.write(buffer, index);
    Serial.println("");
  }
}

void getIPState(uint8_t state){
  char *data = malloc(index);
  for(int c = 0; c < index-1; c++) data[c] = buffer[c];
  data[index-1] = '\0';
  ipData[state] = String(data).toInt();
  free(data);
}

void setup() {
  Serial.begin(115200);
  Serial.println("Starting Server [AT COMMANDS]");
}

void loop(){
  if(Serial.available()){
    char chunk = Serial.read();
    buffer[index++] = chunk;
    if(chunk == '\r'){
      switch(state){
        case IDLE_STATE :
          idleState();
          break;
        case GET_IP_1_STATE:
        case GET_IP_2_STATE:
        case GET_IP_3_STATE:
        case GET_IP_4_STATE:
        case GET_PORT_STATE:
          getIPState(state-1);
          state ++;
          if(state == 6) state = IDLE_STATE;
        break;
      }
      index = 0;
    }
  }else{
    if(send) etherSend("{}", 2);
    delay(100);
  }
}
