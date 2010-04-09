/*
 * File:   BeddingType.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:37
 */

#ifndef _BeddingType_H
#define	_BeddingType_H

#include "DatasetWithFileName.h"

#include <QObject>

class BeddingType: public DatasetWithFileName {
public:
    BeddingType(int id = 0,
            const QString& name = QObject::tr("New Bedding Type"),
            const QString& description = QString::null,
            const QString& filename = QString::null);
    virtual ~BeddingType();
    QString makeToolTipText(const bool withDatasetName=false) const;
};

#endif	/* _BeddingType_H */

