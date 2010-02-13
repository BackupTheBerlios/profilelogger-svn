/*
 * File:   LengthUnit.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:37
 */

#ifndef _LengthUnit_H
#define	_LengthUnit_H

#include "Dataset.h"

#include <QObject>
#include <QStringList>

class LengthUnit : public Dataset {
public:
    LengthUnit(int id = 0,
            int mm = 0,
            const QString& name = QObject::tr("New Length Unit"),
            const QString& description = QString::null);
    virtual ~LengthUnit();
    QString makeToolTipText(const bool withDatasetName = false) const;

    void setMilliMetre(int m) {
        _mm = m;
    }

    int getMilliMetre() const {
        return _mm;
    }

private:
    int _mm;
};

#endif	/* _LengthUnit_H */

