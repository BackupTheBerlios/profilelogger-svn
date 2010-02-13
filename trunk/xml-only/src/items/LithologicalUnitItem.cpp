/*
 * File:   LithologicalUnitItem.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:39
 */

#include "LithologicalUnitItem.h"

#include "LithologicalUnit.h"

LithologicalUnitItem::LithologicalUnitItem(LithologicalUnit* oq)
: StandardItem(oq) {
}

LithologicalUnitItem::~LithologicalUnitItem() {
}

LithologicalUnit* LithologicalUnitItem::getLithologicalUnit() {
    return (LithologicalUnit*) getData();
}
