/*
 * File:   CustomSymbolItem.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:39
 */

#include "CustomSymbolItem.h"

#include "CustomSymbol.h"

CustomSymbolItem::CustomSymbolItem(CustomSymbol* oq)
: StandardItem(oq) {
}

CustomSymbolItem::~CustomSymbolItem() {
}

CustomSymbol* CustomSymbolItem::getCustomSymbol() {
    return (CustomSymbol*) getData();
}
