/*
 * File:   BoundaryTypeItem.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:39
 */

#ifndef _BOUNDARYTYPEITEM_H
#define	_BOUNDARYTYPEITEM_H

#include "StandardItem.h"

class BoundaryType;

class BoundaryTypeItem: public StandardItem {
public:
    BoundaryTypeItem(BoundaryType* oq);
    virtual ~BoundaryTypeItem();

    BoundaryType* getBoundaryType();
};

#endif	/* _BOUNDARYTYPEITEM_H */

