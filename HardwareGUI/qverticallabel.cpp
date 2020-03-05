#include "qverticallabel.h"

QVerticalLabel::QVerticalLabel(QWidget *parent):QLabel(parent){}

QVerticalLabel::QVerticalLabel(QString text, QWidget *parent):QLabel(text,parent){}

void QVerticalLabel::paintEvent(QPaintEvent*){
    QPainter painter(this);
    painter.translate(0,sizeHint().height());
    painter.rotate(270);
    painter.drawText(QRect (QPoint(0,0),QLabel::sizeHint()),Qt::AlignCenter,text());
}

QSize QVerticalLabel::minimumSizeHint() const{
    QSize s = QLabel::minimumSizeHint();
    return QSize(s.height(), s.width());
}

QSize QVerticalLabel::sizeHint() const{
    QSize s = QLabel::sizeHint();
    return QSize(s.height(), s.width());
}
