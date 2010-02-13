/*
 * File:   CustomSymbolItem.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:39
 */

#ifndef _CUSTOMSYMBOLITEM_H
#define	_CUSTOMSYMBOLITEM_H

#include "StandardItem.h"

class CustomSymbol;

class CustomSymbolItem: public StandardItem {
public:
    CustomSymbolItem(CustomSymbol* oq);
    virtual ~CustomSymbolItem();

    CustomSymbol* getCustomSymbol();
};

#endif	/* _CUSTOMSYMBOLITEM_H */

