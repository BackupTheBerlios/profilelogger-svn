/*
 * File:   FossilItem.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:39
 */

#ifndef _FOSSILITEM_H
#define	_FOSSILITEM_H

#include "StandardItem.h"

class Fossil;

class FossilItem : public StandardItem {
public:
    FossilItem(Fossil* oq);
    virtual ~FossilItem();

    Fossil* getFossil();
};

#endif	/* _FOSSILITEM_H */

