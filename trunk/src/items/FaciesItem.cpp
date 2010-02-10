/*
 * File:   FaciesItem.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:39
 */

#include "FaciesItem.h"

#include "Facies.h"

FaciesItem::FaciesItem(Facies* oq)
: StandardItem(oq) {
}

FaciesItem::~FaciesItem() {
}

Facies* FaciesItem::getFacies() {
    return (Facies*)getData();
}
