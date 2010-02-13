/* 
 * File:   LithologyLegendItem.h
 * Author: jolo
 *
 * Created on 13. Januar 2010, 16:08
 */

#ifndef _LITHOLOGYLEGENDITEM_H
#define	_LITHOLOGYLEGENDITEM_H

#include "PatternLegendItem.h"

class Lithology;

class LithologyLegendItem : public PatternLegendItem {
public:
    LithologyLegendItem(QGraphicsItem* p, Lithology* l, int width, int height);
    virtual ~LithologyLegendItem();
private:
    Lithology* _lithology;
};

#endif	/* _LITHOLOGYLEGENDITEM_H */

