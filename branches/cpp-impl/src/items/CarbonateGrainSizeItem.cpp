/*
 * File:   CarbonateGrainSizeItem.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:39
 */

#include "CarbonateGrainSizeItem.h"

#include "CarbonateGrainSize.h"

CarbonateGrainSizeItem::CarbonateGrainSizeItem(CarbonateGrainSize* oq)
: GrainSizeItem(oq) {
}

CarbonateGrainSizeItem::~CarbonateGrainSizeItem() {
}

CarbonateGrainSize* CarbonateGrainSizeItem::getCarbonateGrainSize() {
    return (CarbonateGrainSize*) getData();
}
