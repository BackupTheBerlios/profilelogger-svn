/* 
 * File:   SymbolFactory.h
 * Author: jolo
 *
 * Created on 24. Dezember 2009, 11:40
 */

#ifndef _SYMBOLFACTORY_H
#define	_SYMBOLFACTORY_H

#include "GraphicSvgItem.h"


class Fossil;
class SedimentStructure;
class CustomSymbol;
class BoundaryType;
class GraphicBedItem;

class SymbolFactory {
public:
    SymbolFactory(QGraphicsItem* p);
    SymbolFactory(const SymbolFactory& orig);
    virtual ~SymbolFactory();

    GraphicSvgItem* make(Fossil* f, int maxSize);
    GraphicSvgItem* make(SedimentStructure* f, int maxSize);
    GraphicSvgItem* make(CustomSymbol* f, int maxSize);
    GraphicSvgItem* make(BoundaryType* t, int width);
    
private:
    qreal calculateScaleFactor(GraphicSvgItem* itm, int maxSize);

    QGraphicsItem* _parent;
};

#endif	/* _SYMBOLFACTORY_H */

