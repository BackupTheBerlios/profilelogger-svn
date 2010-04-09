/* 
 * File:   SymbolLegendItem.h
 * Author: jolo
 *
 * Created on 14. Januar 2010, 10:35
 */

#ifndef _SYMBOLLEGENDITEM_H
#define	_SYMBOLLEGENDITEM_H

#include "LegendItem.h"

class Fossil;
class SedimentStructure;
class CustomSymbol;
class BoundaryType;
class GraphicSvgItem;
class SymbolFactory;

class SymbolLegendItem: public LegendItem {
public:
    SymbolLegendItem(QGraphicsItem* p, int w, int h);
    virtual ~SymbolLegendItem();

    void addSymbol(Fossil* f);
    void addSymbol(SedimentStructure* f);
    void addSymbol(CustomSymbol* f);
    void addSymbol(BoundaryType* f);

protected:
    void addItem(GraphicSvgItem* itm);

    int _maxSymbolSize;
    SymbolFactory* _sf;
};

#endif	/* _SYMBOLLEGENDITEM_H */

