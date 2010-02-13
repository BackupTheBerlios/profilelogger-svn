/* 
 * File:   BoundaryTypeLegendItem.cpp
 * Author: jolo
 * 
 * Created on 13. Januar 2010, 16:15
 */

#include "BoundaryTypeLegendItem.h"

#include "BoundaryType.h"

BoundaryTypeLegendItem::BoundaryTypeLegendItem(QGraphicsItem* p, BoundaryType* t, int w, int h)
: SymbolLegendItem(p, w, h),
_boundaryType(t) {
    addSymbol(_boundaryType);
    addId(_boundaryType->getId());
    addName(_boundaryType->getName());
}

BoundaryTypeLegendItem::~BoundaryTypeLegendItem() {
}
