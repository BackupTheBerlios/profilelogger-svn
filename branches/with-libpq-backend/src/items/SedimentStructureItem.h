/*
 * File:   SedimentStructureItem.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:39
 */

#ifndef _SEDIMENTSTRUCTUREITEM_H
#define	_SEDIMENTSTRUCTUREITEM_H

#include "StandardItem.h"

class SedimentStructure;

class SedimentStructureItem : public StandardItem {
public:
    SedimentStructureItem(SedimentStructure* oq);
    virtual ~SedimentStructureItem();

    SedimentStructure* getSedimentStructure();
};

#endif	/* _SEDIMENTSTRUCTUREITEM_H */

