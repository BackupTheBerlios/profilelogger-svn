/* 
 * File:   CustomSymbolLegendItem.cpp
 * Author: jolo
 * 
 * Created on 13. Januar 2010, 16:17
 */

#include "CustomSymbolLegendItem.h"

#include "CustomSymbol.h"

CustomSymbolLegendItem::CustomSymbolLegendItem(QGraphicsItem* p, CustomSymbol* s, int w, int h)
: SymbolLegendItem(p, w, h),
_customSymbol(s) {
    addSymbol(_customSymbol);
    addId(_customSymbol->getId());
    addName(_customSymbol->getName());
}

CustomSymbolLegendItem::~CustomSymbolLegendItem() {
}
