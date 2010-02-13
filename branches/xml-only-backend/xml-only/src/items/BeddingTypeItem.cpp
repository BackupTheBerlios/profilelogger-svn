/*
 * File:   BeddingTypeItem.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:39
 */

#include "BeddingTypeItem.h"

#include "BeddingType.h"

BeddingTypeItem::BeddingTypeItem(BeddingType* oq)
: StandardItem(oq) {
}

BeddingTypeItem::~BeddingTypeItem() {
}

BeddingType* BeddingTypeItem::getBeddingType() {
    return (BeddingType*)getData();
}
