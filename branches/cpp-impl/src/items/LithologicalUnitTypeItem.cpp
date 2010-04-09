/*
 * File:   LithologicalUnitTypeItem.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:39
 */

#include "LithologicalUnitTypeItem.h"

#include "LithologicalUnitType.h"

LithologicalUnitTypeItem::LithologicalUnitTypeItem(LithologicalUnitType* oq)
: StandardItem(oq) {
}

LithologicalUnitTypeItem::~LithologicalUnitTypeItem() {
}

LithologicalUnitType* LithologicalUnitTypeItem::getLithologicalUnitType() {
    return (LithologicalUnitType*)getData();
}
