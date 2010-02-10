/*
 * File:   LithologicalUnitItem.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:39
 */

#ifndef _LITHOLOGICALUNITITEM_H
#define	_LITHOLOGICALUNITITEM_H

#include "StandardItem.h"

class LithologicalUnit;

class LithologicalUnitItem : public StandardItem {
public:
    LithologicalUnitItem(LithologicalUnit* oq);
    virtual ~LithologicalUnitItem();

    LithologicalUnit* getLithologicalUnit();
};

#endif	/* _LITHOLOGICALUNITITEM_H */

