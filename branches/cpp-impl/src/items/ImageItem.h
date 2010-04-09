/*
 * File:   ImageItem.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 11:37
 */

#ifndef _IMAGEITEM_H
#define	_IMAGEITEM_H

#include "StandardItem.h"

class Image;

class ImageItem : public StandardItem {
public:
    ImageItem(Image* bed);

    virtual ~ImageItem();

    Image* getImage();
};

#endif	/* _IMAGEITEM_H */

