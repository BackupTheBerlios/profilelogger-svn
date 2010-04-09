/*
 * File:   SedimentStructureItem.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:39
 */

#include "SedimentStructureItem.h"

#include "SedimentStructure.h"

SedimentStructureItem::SedimentStructureItem(SedimentStructure* oq)
: StandardItem(oq) {
}

SedimentStructureItem::~SedimentStructureItem() {
}

SedimentStructure* SedimentStructureItem::getSedimentStructure() {
    return (SedimentStructure*) getData();
}
