/* 
 * File:   StandardItemModel.h
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 20:07
 */

#ifndef _STANDARDITEMMODEL_H
#define	_STANDARDITEMMODEL_H

#include <QStandardItemModel>

class StandardItemModel : public QStandardItemModel {
    Q_OBJECT

public:
    StandardItemModel(QObject* p = 0);
    virtual ~StandardItemModel();

signals:
    void reloaded();
};

#endif	/* _STANDARDITEMMODEL_H */

