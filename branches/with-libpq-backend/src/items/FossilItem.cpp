/*
 * File:   FossilItem.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:39
 */

#include "FossilItem.h"

#include "Fossil.h"

FossilItem::FossilItem(Fossil* oq)
: StandardItem(oq) {
}

FossilItem::~FossilItem() {
}

Fossil* FossilItem::getFossil() {
    return (Fossil*)getData();
}
