/*
 * File:   SampleItem.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 11:37
 */

#include "SampleItem.h"

#include "Sample.h"

SampleItem::SampleItem(Sample* sample)
: StandardItem(sample) {
    setToolTip(sample->makeToolTipText());
}

SampleItem::~SampleItem() {
}

Sample* SampleItem::getSample() {
    return (Sample*) getData();
}
