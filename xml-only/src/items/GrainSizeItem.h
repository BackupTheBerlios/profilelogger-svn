/*
 * File:   GrainSizeItem.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:39
 */

#ifndef _GRAINSIZEITEM_H
#define	_GRAINSIZEITEM_H

#include "StandardItem.h"

class GrainSize;

class GrainSizeItem: public StandardItem {
public:
    GrainSizeItem(GrainSize* oq);
    virtual ~GrainSizeItem();

    GrainSize* getGrainSize();
};

#endif	/* _GRAINSIZEITEM_H */

