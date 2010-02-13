/*
 * File:   OutcropQualityLegendItem.h
 * Author: jolo
 *
 * Created on 13. Januar 2010, 16:08
 */

#ifndef _OUTCROPQUALITYLEGENDITEM_H
#define	_OUTCROPQUALITYLEGENDITEM_H

#include "PatternLegendItem.h"

class OutcropQuality;

class OutcropQualityLegendItem : public PatternLegendItem {
public:
    OutcropQualityLegendItem(QGraphicsItem* p, OutcropQuality* l, int width, int height);
    virtual ~OutcropQualityLegendItem();
private:
    OutcropQuality* _outcropQuality;
};

#endif	/* _OUTCROPQUALITYLEGENDITEM_H */

