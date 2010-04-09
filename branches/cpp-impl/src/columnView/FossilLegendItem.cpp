/* 
 * File:   FossilLegendItem.cpp
 * Author: jolo
 * 
 * Created on 13. Januar 2010, 16:10
 */

#include "FossilLegendItem.h"

#include "Fossil.h"

FossilLegendItem::FossilLegendItem(QGraphicsItem* p, Fossil* f, int w, int h)
: SymbolLegendItem(p, w, h),
_fossil(f) {
    addSymbol(_fossil);
    addId(f->getId());
    addName(f->getName());
}

FossilLegendItem::~FossilLegendItem() {
}
