/* 
 * File:   CustomSymbolLegendItem.h
 * Author: jolo
 *
 * Created on 13. Januar 2010, 16:17
 */

#ifndef _CUSTOMSYMBOLLEGENDITEM_H
#define	_CUSTOMSYMBOLLEGENDITEM_H

#include "SymbolLegendItem.h"

class CustomSymbol;

class CustomSymbolLegendItem: public SymbolLegendItem {
public:
    CustomSymbolLegendItem(QGraphicsItem* p, CustomSymbol* s, int w, int h);
    virtual ~CustomSymbolLegendItem();
private:
    CustomSymbol* _customSymbol;
};

#endif	/* _CUSTOMSYMBOLLEGENDITEM_H */

