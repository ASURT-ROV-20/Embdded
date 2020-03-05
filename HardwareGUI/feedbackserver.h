#ifndef FEEDBACKSERVER_H
#define FEEDBACKSERVER_H

#include <QTcpServer>
#include <QTcpSocket>
#include <QJsonDocument>
#include <QJsonObject>
#include <QJsonArray>

class FeedbackServer : public QObject{
    Q_OBJECT
public:
    FeedbackServer(quint16 port = 8000);
    ~FeedbackServer();

private:
    QTcpServer *server;
    QTcpSocket *etherSocket;
    void onConnection();
    void readyRead();
};

#endif // FEEDBACKSERVER_H
