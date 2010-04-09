/*
 * File:   LithologicalUnitTypeItem.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:39
 */

#ifndef _LITHOLOGICALUNITTYPEITEM_H
#define	_LITHOLOGICALUNITTYPEITEM_H

#include "StandardItem.h"

class LithologicalUnitType;

class LithologicalUnitTypeItem : public StandardItem {
public:
    LithologicalUnitTypeItem(LithologicalUnitType* oq);
    virtual ~LithologicalUnitTypeItem();

    LithologicalUnitType* getLithologicalUnitType();
};

#endif	/* _LITHOLOGICALUNITTYPEITEM_H */

