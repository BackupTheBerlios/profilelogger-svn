/* 
 * File:   LegendItem.cpp
 * Author: jolo
 * 
 * Created on 13. Januar 2010, 16:00
 */

#include <qpen.h>
#include <qfont.h>

#include "LegendItem.h"

LegendItem::LegendItem(QGraphicsItem* parent, int width, int height)
: QGraphicsRectItem(parent),
_currHeight(0){
    setRect(QRect(0, 0, width, height));
    QPen p;
    p.setColor(Qt::black);
    p.setStyle(Qt::SolidLine);
    setPen(p);

    _font.setPointSize(10);
}

LegendItem::~LegendItem() {
}

void LegendItem::addId(int i) {
    QGraphicsTextItem* id = new QGraphicsTextItem(this);
    id->setHtml(QString("[%1]").arg(i));
    id->setFont(getFont());

    int idXPos = 0;
    int idYPos = _currHeight + _space;

    if (id->boundingRect().width() > rect().width()) {
      idXPos = (int)(0 - id->boundingRect().width() / 2);
    } else {
      idXPos = (int)((rect().width() - id->boundingRect().width()) / 2);
    }

    id->setPos(idXPos, idYPos);

    _currHeight += _space + (int)(id->boundingRect().height());
}

void LegendItem::addName(const QString& n) {
    QGraphicsTextItem* name = new QGraphicsTextItem(this);
    QString html = n;
    html.replace(QString(" "), QString("<br/>"));
    name->setHtml(QString("<p align=\"center\">%1</p>").arg(html));
    name->setFont(getFont());

    int nameXPos = 0;
    int nameYPos = (int)(rect().height() - _space - name->boundingRect().height());

    if (name->boundingRect().width() > rect().width()) {
      nameXPos = (int)(0 - name->boundingRect().width() / 2);
    } else {
      nameXPos = (int)((rect().width() - name->boundingRect().width()) / 2);
    }

    name->setPos(nameXPos, nameYPos);
    _currHeight = (int)(_space + name->boundingRect().height());
}
