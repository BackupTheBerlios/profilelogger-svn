/*
 * File:   BedCorrelationItem.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 11:37
 */

#include "BedCorrelationItem.h"

#include "BedCorrelation.h"

BedCorrelationItem::BedCorrelationItem(BedCorrelation* bedCorrelation)
: StandardItem(bedCorrelation) {
    setToolTip(bedCorrelation->makeToolTipText());
}

BedCorrelationItem::~BedCorrelationItem() {
}

BedCorrelation* BedCorrelationItem::getBedCorrelation() {
    return (BedCorrelation*) getData();
}
