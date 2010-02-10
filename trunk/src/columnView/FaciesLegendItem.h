/*
 * File:   FaciesLegendItem.h
 * Author: jolo
 *
 * Created on 13. Januar 2010, 16:08
 */

#ifndef _FACIESLEGENDITEM_H
#define	_FACIESLEGENDITEM_H

#include "PatternLegendItem.h"

class Facies;

class FaciesLegendItem : public PatternLegendItem {
public:
    FaciesLegendItem(QGraphicsItem* p, Facies* l, int width, int height);
    virtual ~FaciesLegendItem();
private:
    Facies* _lithology;
};

#endif	/* _FACIESLEGENDITEM_H */

