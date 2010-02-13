/*
 * File:   SedimentStructure.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:37
 */

#ifndef _SedimentStructure_H
#define	_SedimentStructure_H

#include "DatasetWithFileName.h"

#include <QObject>
#include <QStringList>

class SedimentStructure : public DatasetWithFileName {
public:
    SedimentStructure(int id = 0,
            const QString& name = QObject::tr("New SedimentStructure"),
            const QString& description = QString::null,
            const QString& fileName = QString::null);
    virtual ~SedimentStructure();
    QString makeToolTipText(const bool withDatasetName = false) const;
};

#endif	/* _SedimentStructure_H */

