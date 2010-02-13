/* 
 * File:   ColorLegendItem.h
 * Author: jolo
 *
 * Created on 14. Januar 2010, 10:09
 */

#ifndef _COLORLEGENDITEM_H
#define	_COLORLEGENDITEM_H

#include "PatternLegendItem.h"

class Color;

class ColorLegendItem : public PatternLegendItem {
public:
    ColorLegendItem(QGraphicsItem* p, Color* c, int w, int h);
    virtual ~ColorLegendItem();
private:
    Color* _color;
};

#endif	/* _COLORLEGENDITEM_H */

