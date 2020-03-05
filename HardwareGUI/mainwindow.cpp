#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) : QMainWindow(parent){
    centeralWidget = new QWidget(this);
    centeralLayout = new QVBoxLayout();
    scroll = new QScrollArea();

    QRect screenRes = QGuiApplication::primaryScreen()->geometry();

    centeralWidget->resize(screenRes.width(),2200);

    scroll->setWidget(centeralWidget);

    centeralWidget->setLayout(centeralLayout);
    setCentralWidget(scroll);

    frontRightMotor = new MotorChart("FRONT RIGHT MOTOR");
    frontLeftMotor = new MotorChart("FRONT LEFT MOTOR");
    backRightMotor = new MotorChart("BACK RIGHT MOTOR");
    backLeftMotor = new MotorChart("BACK LEFT MOTOR");
    verticalRightMotor = new MotorChart("VERTICAL RIGHT MOTOR");
    verticalLeftMotor = new MotorChart("VERTICAL RIGHT MOTOR");

    t1 = new QTimer();
    server = new FeedbackServer();
    centeralLayout->addWidget(frontRightMotor);
    centeralLayout->addWidget(frontLeftMotor);
    centeralLayout->addWidget(backRightMotor);
    centeralLayout->addWidget(backLeftMotor);
    centeralLayout->addWidget(verticalRightMotor);
    centeralLayout->addWidget(verticalLeftMotor);
    t1->start(100);

    showFullScreen();

    connect(t1, &QTimer::timeout, this, &MainWindow::onTimerTick);
}

void MainWindow::onTimerTick(){
    frontRightMotor->addCurrentValue(qrand()%50);
    frontRightMotor->addPWMValue(qrand()%50);
    frontLeftMotor->addCurrentValue(qrand()%50);
    frontLeftMotor->addPWMValue(qrand()%50);
    backRightMotor->addCurrentValue(qrand()%50);
    backRightMotor->addPWMValue(qrand()%50);
}


MainWindow::~MainWindow(){
}

