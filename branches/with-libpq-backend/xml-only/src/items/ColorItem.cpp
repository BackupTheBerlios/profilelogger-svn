/*
 * File:   ColorItem.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:39
 */

#include "ColorItem.h"

#include "Color.h"

ColorItem::ColorItem(Color* oq)
: StandardItem(oq) {
}

ColorItem::~ColorItem() {
}

Color* ColorItem::getColor() {
    return (Color*)getData();
}
