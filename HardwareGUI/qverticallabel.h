#ifndef QVERTICALLABEL_H
#define QVERTICALLABEL_H

#include <QLabel>
#include <QPainter>

class QVerticalLabel : public QLabel{

public:
    QVerticalLabel(QWidget *parent = nullptr);
    QVerticalLabel(QString text, QWidget *parent = nullptr);

private:
    void paintEvent(QPaintEvent*);
    QSize sizeHint() const ;
    QSize minimumSizeHint() const;
};

#endif // QVERTICALLABEL_H
