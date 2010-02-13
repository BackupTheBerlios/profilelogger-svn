/* 
 * File:   OutcropQualityItem.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:39
 */

#ifndef _OUTCROPQUALITYITEM_H
#define	_OUTCROPQUALITYITEM_H

#include "StandardItem.h"

class OutcropQuality;

class OutcropQualityItem: public StandardItem {
public:
    OutcropQualityItem(OutcropQuality* oq);
    virtual ~OutcropQualityItem();

    OutcropQuality* getOutcropQuality();
};

#endif	/* _OUTCROPQUALITYITEM_H */

