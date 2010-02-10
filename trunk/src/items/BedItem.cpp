/* 
 * File:   BedItem.cpp
 * Author: jolo
 * 
 * Created on 11. Dezember 2009, 11:37
 */

#include "BedItem.h"

#include "Bed.h"

BedItem::BedItem(Bed* bed)
: StandardItem(bed) {
    setToolTip(bed->makeToolTipText());
}

BedItem::~BedItem() {
}

Bed* BedItem::getBed() {
    return (Bed*) getData();
}
