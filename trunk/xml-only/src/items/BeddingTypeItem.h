/*
 * File:   BeddingTypeItem.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:39
 */

#ifndef _BEDDINGTYPEITEM_H
#define	_BEDDINGTYPEITEM_H

#include "StandardItem.h"

class BeddingType;

class BeddingTypeItem: public StandardItem {
public:
    BeddingTypeItem(BeddingType* oq);
    virtual ~BeddingTypeItem();

    BeddingType* getBeddingType();
};

#endif	/* _BEDDINGTYPEITEM_H */

