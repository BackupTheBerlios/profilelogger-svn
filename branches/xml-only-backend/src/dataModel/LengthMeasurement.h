/* 
 * File:   LengthMeasurement.h
 * Author: jolo
 *
 * Created on 14. Dezember 2009, 16:18
 */

#ifndef _LENGTHMEASUREMENT_H
#define	_LENGTHMEASUREMENT_H

#include <QString>

#include "ProfileLogger.h"
#include "Project.h"
#include "LengthUnit.h"

class LengthUnit;

class LengthMeasurement {
public:
    LengthMeasurement(int value = 0, LengthUnit* unit = 0);
    virtual ~LengthMeasurement();

    bool hasUnit() const {
        return 0 != _unit;
    }

    void setValue(int v) {
        _value = v;
    }

    void setUnit(LengthUnit* u) {
        if (!u) {
            _unit = (static_cast<ProfileLogger*> (QApplication::instance()))->getProject()->getDefaultLengthUnit();
        } else {
            _unit = u;
        }
    }

    int getValue() const {
        return _value;
    }

    LengthUnit* getUnit() const {
        return _unit;
    }

    QString toString() const;

    int getMillimetres() const;
    
private:
    int _value;
    LengthUnit* _unit;
};

#endif	/* _LENGTHMEASUREMENT_H */

