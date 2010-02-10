/* 
 * File:   StandardItem.h
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 20:09
 */

#ifndef _STANDARDITEM_H
#define	_STANDARDITEM_H

#include <QStandardItem>

class Dataset;

class StandardItem: public QStandardItem {
public:
    StandardItem(Dataset* d);
    virtual ~StandardItem();

protected:
    Dataset* getData() { return _data; }

private:
    Dataset* _data;
};

#endif	/* _STANDARDITEM_H */

