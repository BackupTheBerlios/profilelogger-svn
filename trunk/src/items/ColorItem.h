/*
 * File:   ColorItem.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:39
 */

#ifndef _COLORITEM_H
#define	_COLORITEM_H

#include "StandardItem.h"

class Color;

class ColorItem: public StandardItem {
public:
    ColorItem(Color* oq);
    virtual ~ColorItem();

    Color* getColor();
};

#endif	/* _COLORITEM_H */

