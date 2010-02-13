/* 
 * File:   SedimentStructureLegendItem.h
 * Author: jolo
 *
 * Created on 13. Januar 2010, 16:11
 */

#ifndef _SEDIMENTSTRUCTURELEGENDITEM_H
#define	_SEDIMENTSTRUCTURELEGENDITEM_H

#include "SymbolLegendItem.h"

class SedimentStructure;

class SedimentStructureLegendItem: public SymbolLegendItem {
public:
    SedimentStructureLegendItem(QGraphicsItem* p, SedimentStructure* s, int w, int h);
    virtual ~SedimentStructureLegendItem();
private:
    SedimentStructure* _sedimentStructure;
};

#endif	/* _SEDIMENTSTRUCTURELEGENDITEM_H */

