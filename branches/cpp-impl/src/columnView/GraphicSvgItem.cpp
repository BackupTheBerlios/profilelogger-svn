/* 
 * File:   GraphicsSvgItem.cpp
 * Author: jolo
 * 
 * Created on 24. Dezember 2009, 10:18
 */

#include "GraphicSvgItem.h"

GraphicSvgItem::GraphicSvgItem(const QString& filename, QGraphicsItem* parent)
: QGraphicsSvgItem(filename, parent) {
}

GraphicSvgItem::~GraphicSvgItem() {
}
