/*
 * File:   BedCorrelationItem.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 11:37
 */

#ifndef _BEDCORRELATIONITEM_H
#define	_BEDCORRELATIONITEM_H

#include "StandardItem.h"

class BedCorrelation;

class BedCorrelationItem: public StandardItem {
public:
    BedCorrelationItem(BedCorrelation* bed);

    virtual ~BedCorrelationItem();

    BedCorrelation* getBedCorrelation();
};

#endif	/* _BEDCORRELATIONITEM_H */

