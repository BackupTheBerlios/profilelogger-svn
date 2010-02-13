/*
 * File:   FaciesItem.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:39
 */

#ifndef _FACIESITEM_H
#define	_FACIESITEM_H

#include "StandardItem.h"

class Facies;

class FaciesItem: public StandardItem {
public:
    FaciesItem(Facies* oq);
    virtual ~FaciesItem();

    Facies* getFacies();
};

#endif	/* _FACIESITEM_H */

