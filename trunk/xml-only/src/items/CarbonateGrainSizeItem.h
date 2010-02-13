/*
 * File:   CarbonateGrainSizeItem.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:39
 */

#ifndef _CARBONATEGRAINSIZEITEM_H
#define	_CARBONATEGRAINSIZEITEM_H

#include "GrainSizeItem.h"

class CarbonateGrainSize;

class CarbonateGrainSizeItem: public GrainSizeItem {
public:
    CarbonateGrainSizeItem(CarbonateGrainSize* oq);
    virtual ~CarbonateGrainSizeItem();

    CarbonateGrainSize* getCarbonateGrainSize();
};

#endif	/* _CARBONATEGRAINSIZEITEM_H */

