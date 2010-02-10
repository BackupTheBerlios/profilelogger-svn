/* 
 * File:   Facies.h
 * Author: jolo
 *
 * Created on 16. Januar 2010, 20:57
 */

#ifndef _Facies_H
#define	_Facies_H

#include "DatasetWithFileName.h"

#include <QObject>
#include <QStringList>

class Facies : public DatasetWithFileName {
public:
    Facies(int id = 0,
            const QString& name = QObject::tr("New Facies"),
            const QString& description = QString::null,
            const QString& fileName = QString::null);

    virtual ~Facies();
    QString makeToolTipText(const bool withDatasetName = false) const;
};

#endif	/* _Facies_H */

