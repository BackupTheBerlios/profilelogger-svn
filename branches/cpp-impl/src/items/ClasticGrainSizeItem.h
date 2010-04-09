/*
 * File:   ClasticGrainSizeItem.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:39
 */

#ifndef _CLASTICGRAINSIZEITEM_H
#define	_CLASTICGRAINSIZEITEM_H

#include "GrainSizeItem.h"

class ClasticGrainSize;

class ClasticGrainSizeItem: public GrainSizeItem {
public:
    ClasticGrainSizeItem(ClasticGrainSize* oq);
    virtual ~ClasticGrainSizeItem();

    ClasticGrainSize* getClasticGrainSize();
};

#endif	/* _CLASTICGRAINSIZEITEM_H */

