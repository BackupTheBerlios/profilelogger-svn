/* 
 * File:   LithologicalUnit.h
 * Author: jolo
 *
 * Created on 18. Januar 2010, 17:15
 */

#ifndef _LITHOLOGICALUNIT_H
#define	_LITHOLOGICALUNIT_H

#include "Dataset.h"

#include <QObject>
#include <QStringList>

class LithologicalUnitType;

class LithologicalUnit: public Dataset {
public:
    LithologicalUnit(int id = 0,
            const QString& name = QObject::tr("Lithological Unit"),
            const QString& description = QString::null,
            LithologicalUnitType* t = 0);

    virtual ~LithologicalUnit();

    QString makeToolTipText(const bool withDatasetName=true);
    
    void setLithologicalUnitType(LithologicalUnitType* t) {
        _lithologicalUnitType = t;
    }

    LithologicalUnitType* getLithologicalUnitType() {
        return _lithologicalUnitType;
    }

    bool hasLithologicalUnitType() const {
        return (0 != _lithologicalUnitType);
    }
    
private:
    LithologicalUnitType* _lithologicalUnitType;
};

#endif	/* _LITHOLOGICALUNIT_H */

