/*
 * File:   LithologyItem.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:39
 */

#include "LithologyItem.h"

#include "Lithology.h"

LithologyItem::LithologyItem(Lithology* oq)
: StandardItem(oq) {
}

LithologyItem::~LithologyItem() {
}

Lithology* LithologyItem::getLithology() {
    return (Lithology*)getData();
}
