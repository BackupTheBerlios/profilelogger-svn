/* 
 * File:   BedItem.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 11:37
 */

#ifndef _BEDITEM_H
#define	_BEDITEM_H

#include "StandardItem.h"

class Bed;

class BedItem: public StandardItem {
public:
    BedItem(Bed* bed);

    virtual ~BedItem();

    Bed* getBed();
};

#endif	/* _BEDITEM_H */

