#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QHBoxLayout>
#include <QVBoxLayout>
#include <QScrollArea>
#include <QTimer>
//#include <QDesktopWidget>
#include <QScreen>
#include "motorchart.h"
#include "feedbackserver.h"

using namespace QtCharts;
class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private:
    QWidget *centeralWidget;
    QScrollArea *scroll;
    QVBoxLayout *centeralLayout;
    MotorChart *frontRightMotor;
    MotorChart *frontLeftMotor;
    MotorChart *backRightMotor;
    MotorChart *backLeftMotor;
    MotorChart *verticalRightMotor;
    MotorChart *verticalLeftMotor;
    QTimer *t1;
    FeedbackServer *server;

private slots:
    void onTimerTick();
};
#endif // MAINWINDOW_H
