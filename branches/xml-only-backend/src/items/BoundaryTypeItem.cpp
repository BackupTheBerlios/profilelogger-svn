/*
 * File:   BoundaryTypeItem.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:39
 */

#include "BoundaryTypeItem.h"

#include "BoundaryType.h"

BoundaryTypeItem::BoundaryTypeItem(BoundaryType* oq)
: StandardItem(oq) {
}

BoundaryTypeItem::~BoundaryTypeItem() {
}

BoundaryType* BoundaryTypeItem::getBoundaryType() {
    return (BoundaryType*)getData();
}
