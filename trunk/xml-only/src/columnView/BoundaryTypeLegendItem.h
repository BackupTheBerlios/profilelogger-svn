/* 
 * File:   BoundaryTypeLegendItem.h
 * Author: jolo
 *
 * Created on 13. Januar 2010, 16:15
 */

#ifndef _BOUNDARYTYPELEGENDITEM_H
#define	_BOUNDARYTYPELEGENDITEM_H

#include "SymbolLegendItem.h"

class BoundaryType;

class BoundaryTypeLegendItem: public SymbolLegendItem {
public:
    BoundaryTypeLegendItem(QGraphicsItem* p, BoundaryType* t, int w, int h);
    virtual ~BoundaryTypeLegendItem();
private:
    BoundaryType* _boundaryType;
};

#endif	/* _BOUNDARYTYPELEGENDITEM_H */

