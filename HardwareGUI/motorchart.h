#ifndef MOTORCHART_H
#define MOTORCHART_H

#define LIST_INITALIZATION {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}

#include <QWidget>
#include <QHBoxLayout>
#include <QVBoxLayout>
#include <QtCharts/QChartView>
#include <QtCharts/QChart>
#include <QtCharts/QLineSeries>
#include <QtCharts/QValueAxis>
#include "qverticallabel.h"

using namespace  QtCharts;

class MotorChart : public QWidget{
private:
    QHBoxLayout *chartsLayout;
    QChartView *currentChartView;
    QChartView *pwmChartView;
    QChart *currentChart;
    QChart *pwmChart;
    QLineSeries *currentSeries;
    QLineSeries *pwmSeries;
    QValueAxis *currentAxisY;
    QValueAxis *pwmAxisY;
    QList<QPointF> *currentPoints;
    QList<QPointF> *pwmPoints;
    QList<int> currentValues LIST_INITALIZATION;
    QList<int> pwmValues LIST_INITALIZATION;
    QVerticalLabel *motorName;
    int counter = 0;

    void initPoints(QList<QPointF>*);

public:
    MotorChart(QString, QWidget *parent = nullptr);
    void setCurrentRange(int,int);
    void setPWMRange(int,int);
    void addCurrentValue(int);
    void addPWMValue(int);
};

#endif // MOTORCHART_H
