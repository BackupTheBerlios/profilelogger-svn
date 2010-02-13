/*
 * File:   GrainSizeItem.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:39
 */

#include "GrainSizeItem.h"

#include "GrainSize.h"

GrainSizeItem::GrainSizeItem(GrainSize* oq)
: StandardItem(oq) {
}

GrainSizeItem::~GrainSizeItem() {
}

GrainSize* GrainSizeItem::getGrainSize() {
    return (GrainSize*)getData();
}
