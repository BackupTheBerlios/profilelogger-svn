/* 
 * File:   LithologicalUnitType.h
 * Author: jolo
 *
 * Created on 18. Januar 2010, 16:28
 */

#ifndef _LITHOLOGICALUNITTYPE_H
#define	_LITHOLOGICALUNITTYPE_H

#include <QObject>
#include <QStringList>

#include "Dataset.h"

class LithologicalUnitType : public Dataset {
public:
    LithologicalUnitType(int id = 0,
            const QString& name = QObject::tr("New Lithological Unit Type"),
            const QString& description = QString::null);

    virtual ~LithologicalUnitType();

    QString makeToolTipText(const bool withDatasetName = true) const;
};

#endif	/* _LITHOLOGICALUNITTYPE_H */

