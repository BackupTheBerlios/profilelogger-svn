/* 
 * File:   StandardItem.cpp
 * Author: jolo
 * 
 * Created on 10. Dezember 2009, 20:09
 */

#include "StandardItem.h"

#include "Dataset.h"

StandardItem::StandardItem(Dataset* d)
: QStandardItem(),
_data(d) {
    setText(_data->getName());
    setToolTip(_data->makeToolTipText());
}

StandardItem::~StandardItem() {
}

