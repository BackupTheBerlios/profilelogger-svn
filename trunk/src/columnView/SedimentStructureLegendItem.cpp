/* 
 * File:   SedimentStructureLegendItem.cpp
 * Author: jolo
 * 
 * Created on 13. Januar 2010, 16:11
 */

#include "SedimentStructureLegendItem.h"

#include "SedimentStructure.h"
#include "LegendItem.h"
#include "GraphicColumnHeader.h"

SedimentStructureLegendItem::SedimentStructureLegendItem(QGraphicsItem* p,
        SedimentStructure* s, int w, int h)
: SymbolLegendItem(p, w, h),
_sedimentStructure(s) {
    addSymbol(_sedimentStructure);
    addId(_sedimentStructure->getId());
    addName(_sedimentStructure->getName());
}

SedimentStructureLegendItem::~SedimentStructureLegendItem() {
}
