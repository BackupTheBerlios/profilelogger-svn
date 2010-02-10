/* 
 * File:   FossilLegendItem.h
 * Author: jolo
 *
 * Created on 13. Januar 2010, 16:10
 */

#ifndef _FOSSILLEGENDITEM_H
#define	_FOSSILLEGENDITEM_H

#include "SymbolLegendItem.h"

class Fossil;

class FossilLegendItem : public SymbolLegendItem {
public:
    FossilLegendItem(QGraphicsItem* p, Fossil* f, int w, int h);
    virtual ~FossilLegendItem();
private:
    Fossil* _fossil;
};

#endif	/* _FOSSILLEGENDITEM_H */

