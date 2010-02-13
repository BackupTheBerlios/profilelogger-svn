/* 
 * File:   BeddingTypeLegendItem.h
 * Author: jolo
 *
 * Created on 13. Januar 2010, 16:09
 */

#ifndef _BEDDINGTYPELEGENDITEM_H
#define	_BEDDINGTYPELEGENDITEM_H

#include "PatternLegendItem.h"

class BeddingType;

class BeddingTypeLegendItem: public PatternLegendItem {
public:
    BeddingTypeLegendItem(QGraphicsItem* p, BeddingType* t, int w, int h);
    virtual ~BeddingTypeLegendItem();
private:
    BeddingType* _beddingType;
};

#endif	/* _BEDDINGTYPELEGENDITEM_H */

