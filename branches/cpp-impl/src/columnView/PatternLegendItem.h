/* 
 * File:   PatternLegendItem.h
 * Author: jolo
 *
 * Created on 14. Januar 2010, 09:30
 */

#ifndef _PATTERNLEGENDITEM_H
#define	_PATTERNLEGENDITEM_H

#include "LegendItem.h"

class PatternLegendItem: public LegendItem {
public:
    PatternLegendItem(QGraphicsItem* p, int width, int height);
    virtual ~PatternLegendItem();

protected:
    void addPattern(const QBrush& b);
};

#endif	/* _PATTERNLEGENDITEM_H */

