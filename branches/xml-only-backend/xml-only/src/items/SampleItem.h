/*
 * File:   SampleItem.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 11:37
 */

#ifndef _SAMPLEITEM_H
#define	_SAMPLEITEM_H

#include "StandardItem.h"

class Sample;

class SampleItem: public StandardItem {
public:
    SampleItem(Sample* bed);

    virtual ~SampleItem();

    Sample* getSample();
};

#endif	/* _SAMPLEITEM_H */

