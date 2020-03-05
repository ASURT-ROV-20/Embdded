#include "feedbackserver.h"

FeedbackServer::FeedbackServer(quint16 port){
    server = new QTcpServer();
    server->listen(QHostAddress::Any, port);
    connect(server, &QTcpServer::newConnection, this, &FeedbackServer::onConnection);
}

void FeedbackServer::onConnection(){
    etherSocket = server->nextPendingConnection();
    connect(etherSocket, &QTcpSocket::readyRead, this, &FeedbackServer::readyRead);
}

/**

a = {
    "Time": [2000, 1, 1, 5, 1, 12, 54, 72591],
    "ADC": [0,0,0,0,0,0,0,0],
    "PWM": [0,0,0,0,0,0]
}


*/

void FeedbackServer::readyRead(){
    QByteArray msg = etherSocket->readAll();
    QJsonDocument jsonDocument = QJsonDocument::fromJson(msg);
    if(jsonDocument.isNull()) qDebug() << "Failed, msg:" << msg;
    QJsonObject json_obj = jsonDocument.object();
    QJsonArray pwmArr = json_obj["PWM"].toArray();
    QJsonArray adcArr = json_obj["ADC"].toArray();
    QJsonArray timeArr = json_obj["Time"].toArray();

}



FeedbackServer::~FeedbackServer(){

}
