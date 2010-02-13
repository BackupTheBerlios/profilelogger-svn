/* 
 * File:   OutcropQualityItem.cpp
 * Author: jolo
 * 
 * Created on 11. Dezember 2009, 16:39
 */

#include "OutcropQualityItem.h"

#include "OutcropQuality.h"

OutcropQualityItem::OutcropQualityItem(OutcropQuality* oq)
: StandardItem(oq) {
}

OutcropQualityItem::~OutcropQualityItem() {
}

OutcropQuality* OutcropQualityItem::getOutcropQuality() {
    return (OutcropQuality*)getData();
}
