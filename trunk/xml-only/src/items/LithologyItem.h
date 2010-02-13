/*
 * File:   LithologyItem.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:39
 */

#ifndef _LITHOLOGYITEM_H
#define	_LITHOLOGYITEM_H

#include "StandardItem.h"

class Lithology;

class LithologyItem: public StandardItem {
public:
    LithologyItem(Lithology* oq);
    virtual ~LithologyItem();

    Lithology* getLithology();
};

#endif	/* _LITHOLOGYITEM_H */

