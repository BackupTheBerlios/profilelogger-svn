/* 
 * File:   PatternLegendItem.cpp
 * Author: jolo
 * 
 * Created on 14. Januar 2010, 09:30
 */

#include "PatternLegendItem.h"

#include <QPen>

PatternLegendItem::PatternLegendItem(QGraphicsItem* p, int w, int h)
: LegendItem(p, w, h) {
}

PatternLegendItem::~PatternLegendItem() {
}

void PatternLegendItem::addPattern(const QBrush& b) {
    QPen p;

    p.setColor(Qt::black);
    p.setStyle(Qt::SolidLine);

    QGraphicsRectItem* pattern = new QGraphicsRectItem(this);
    pattern->setBrush(b);
    pattern->setPen(p);

    pattern->setRect(QRectF(0, 0, rect().width() * 0.8, rect().width() * 0.8));
    _space = (int)((rect().width() - pattern->rect().width()) / 2);
    pattern->setPos(_space, _space);

    _currHeight = (int)(_space + pattern->rect().height());
}
