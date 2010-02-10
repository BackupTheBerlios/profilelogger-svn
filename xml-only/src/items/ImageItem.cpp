/*
 * File:   ImageItem.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 11:37
 */

#include "ImageItem.h"

#include "Image.h"

ImageItem::ImageItem(Image* image)
: StandardItem(image) {
    setToolTip(image->makeToolTipText());
}

ImageItem::~ImageItem() {
}

Image* ImageItem::getImage() {
    return (Image*) getData();
}
