/*
 * File:   ClasticGrainSizeItem.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:39
 */

#include "ClasticGrainSizeItem.h"

#include "ClasticGrainSize.h"

ClasticGrainSizeItem::ClasticGrainSizeItem(ClasticGrainSize* oq)
: GrainSizeItem(oq) {
}

ClasticGrainSizeItem::~ClasticGrainSizeItem() {
}

ClasticGrainSize* ClasticGrainSizeItem::getClasticGrainSize() {
    return (ClasticGrainSize*) getData();
}
