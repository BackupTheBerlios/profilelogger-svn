/* 
 * File:   SymbolLegendItem.cpp
 * Author: jolo
 * 
 * Created on 14. Januar 2010, 10:35
 */

#include <qrect.h>

#include "SymbolLegendItem.h"
#include "SymbolFactory.h"
#include "GraphicSvgItem.h"
#include "GraphicBedItem.h"

SymbolLegendItem::SymbolLegendItem(QGraphicsItem* p, int w, int h)
: LegendItem(p, w, h),
_maxSymbolSize(0),
_sf(0) {
    _sf = new SymbolFactory(this);
    _maxSymbolSize = (int)(rect().width() * 0.8);
}

SymbolLegendItem::~SymbolLegendItem() {
}

void SymbolLegendItem::addItem(GraphicSvgItem* itm) {
    if (!itm) {
        return;
    }

    _space = (int)((rect().width() - _maxSymbolSize) / 2);
    itm->setPos(_space, _space);

    _currHeight = _space + _maxSymbolSize;
}

void SymbolLegendItem::addSymbol(Fossil* f) {
    addItem(_sf->make(f, _maxSymbolSize));
}

void SymbolLegendItem::addSymbol(SedimentStructure* f) {
    addItem(_sf->make(f, _maxSymbolSize));
}

void SymbolLegendItem::addSymbol(CustomSymbol* f) {
    addItem(_sf->make(f, _maxSymbolSize));
}

void SymbolLegendItem::addSymbol(BoundaryType* f) {
    addItem(_sf->make(f, _maxSymbolSize));
}

