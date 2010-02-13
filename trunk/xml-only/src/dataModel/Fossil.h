/*
 * File:   Fossil.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:37
 */

#ifndef _Fossil_H
#define	_Fossil_H

#include "DatasetWithFileName.h"

#include <QObject>

class Fossil : public DatasetWithFileName {
public:
    Fossil(int id = 0,
            const QString& name = QObject::tr("New Fossil"),
            const QString& description = QString::null,
            const QString& fileName = QString::null);
    virtual ~Fossil();
    QString makeToolTipText(const bool withDatasetName = false) const;
};

#endif	/* _Fossil_H */

