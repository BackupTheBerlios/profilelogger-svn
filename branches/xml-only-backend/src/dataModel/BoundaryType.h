/*
 * File:   BoundaryType.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:37
 */

#ifndef _BoundaryType_H
#define	_BoundaryType_H

#include "DatasetWithFileName.h"
#include "DatasetWithFileNameEditorDialog.h"

class BoundaryType : public DatasetWithFileName {
public:
    BoundaryType(int id = 0,
            const QString& name = QObject::tr("New Boundary Type"),
            const QString& description = QString::null,
            const QString& fileName = QString::null);
    virtual ~BoundaryType();
    QString makeToolTipText(const bool withDatasetName = false) const;
};

#endif	/* _BoundaryType_H */

