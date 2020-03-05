#include "motorchart.h"

MotorChart::MotorChart(QString name, QWidget *parent) : QWidget(parent){
    chartsLayout = new QHBoxLayout();
    currentChartView = new QChartView();
    pwmChartView = new QChartView();
    currentChart = new QChart();
    pwmChart = new QChart();
    currentSeries = new QLineSeries();
    pwmSeries = new QLineSeries();
    currentAxisY = new QValueAxis();
    pwmAxisY = new QValueAxis();
    currentPoints = new QList<QPointF>();
    pwmPoints = new QList<QPointF>();
    motorName = new QVerticalLabel(name);

    this->setLayout(chartsLayout);

    QVBoxLayout *labelLayout = new QVBoxLayout();
    labelLayout->addWidget(new QWidget);
    labelLayout->addWidget(motorName);
    labelLayout->addWidget(new QWidget);
    motorName->setStyleSheet("fontweight : bold; font-size : 15px;");

    chartsLayout->addLayout(labelLayout);
    chartsLayout->addWidget(currentChartView);
    chartsLayout->addWidget(pwmChartView);

//    motorName->setStyleSheet("background : red");

    currentChartView->setChart(currentChart);
    pwmChartView->setChart(pwmChart);
    currentChart->addSeries(currentSeries);
    pwmChart->addSeries(pwmSeries);
    currentChart->setAxisX(currentAxisY,currentSeries);
    pwmChart->setAxisX(pwmAxisY,pwmSeries);

    currentChart->setTitle("Current States");
    currentChart->setAnimationOptions(QChart::NoAnimation);
    currentChart->createDefaultAxes();
    currentChartView->setRenderHint(QPainter::Antialiasing);
    currentChart->legend()->setAlignment(Qt::AlignRight);
    currentChart->axisX()->setRange(0,60);
    currentChart->axisX()->setTitleText("Time");
    currentChart->axisY()->setTitleText("Value in mA");

    pwmChart->setTitle("Pwm States");
    pwmChart->setAnimationOptions(QChart::NoAnimation);
    pwmChart->createDefaultAxes();
    pwmChartView->setRenderHint(QPainter::Antialiasing);
    pwmChart->legend()->setAlignment(Qt::AlignRight);
    pwmChart->axisX()->setRange(0,60);
    pwmChart->axisX()->setTitleText("Time");
    pwmChart->axisY()->setTitleText("PWM Value");

    QColor currentClr(Qt::red);
    QPen pen(currentClr);
    pen.setWidth(2);
    currentSeries->setPen(pen);
    pen.setColor(Qt::blue);
    pwmSeries->setPen(pen);

    initPoints(currentPoints);
    initPoints(pwmPoints);
    setCurrentRange(0,50);
    setPWMRange(0,50);
    setMaximumHeight(400);
}

void MotorChart::setCurrentRange(int min, int max){
    currentChart->axisY()->setRange(min, max);
}

void MotorChart::setPWMRange(int min, int max){
    pwmChart->axisY()->setRange(min, max);
}

void MotorChart::initPoints(QList<QPointF> *points){
    for(int c = 0; c < 60; c++){
        points->append(QPointF(c,0));
    }
}

void MotorChart::addCurrentValue(int v){
    currentValues.pop_front();
    currentValues.append(v);
    for(int a = 0; a < currentValues.length(); a++){
        (*currentPoints)[a] = QPointF(a,currentValues[a]);
    }
    currentSeries->replace(*currentPoints);
}

void MotorChart::addPWMValue(int v){
    pwmValues.pop_front();
    pwmValues.append(v);
    for(int a = 0; a < currentValues.length(); a++){
        (*pwmPoints)[a] = QPointF(a,pwmValues[a]);
    }
    pwmSeries->replace(*pwmPoints);
}
