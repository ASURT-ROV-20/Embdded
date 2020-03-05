#include "mainwindow.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);


//    QFile styleFile ("://style.css");
//    styleFile.open(QIODevice::ReadOnly);
//    QString style = styleFile.readAll();
//    a.setStyleSheet(style);
//    a.setWindowIcon(QIcon(":/icons/icons/logo.png"));
    MainWindow w;
    w.show();
    return a.exec();
}
