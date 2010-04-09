/*
 * File:   ColorLegendItem.cpp
 * Author: jolo
 *
 * Created on 13. Januar 2010, 16:08
 */

#include <qpen.h>

#include "ColorLegendItem.h"

#include "Color.h"
#include "ProfileLogger.h"
#include "GraphicBedItem.h"
#include "Settings.h"
#include "ProfileLogger.h"

ColorLegendItem::ColorLegendItem(QGraphicsItem* parent, Color* l, int width, int height)
: PatternLegendItem(parent, width, height),
_color(l) {
    QBrush b;
    b.setStyle(l->getBrushStyle());

    addPattern(b);
    addId(l->getId());
    addName(l->getName());
}

ColorLegendItem::~ColorLegendItem() {
}
