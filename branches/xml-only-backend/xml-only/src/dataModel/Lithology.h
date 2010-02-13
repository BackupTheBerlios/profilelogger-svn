/*
 * File:   Lithology.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:37
 */

#ifndef _Lithology_H
#define	_Lithology_H

#include "DatasetWithFileName.h"

#include "GrainSizeModes.h"

#include <QObject>
#include <QStringList>

class ClasticGrainSize;
class CarbonateGrainSize;

class Lithology : public DatasetWithFileName {
public:
    Lithology(int id = 0,
            const QString& name = QObject::tr("New Color"),
            const QString& description = QString::null,
            const QString& fileName = QString::null,
            GrainSizeModes defaultGrainSizeMode = ClasticGrainSizeMode,
            ClasticGrainSize* defaultClasticGrainSize = 0,
            CarbonateGrainSize* defaultCarbonateGrainSize = 0);
    virtual ~Lithology();
    QString makeToolTipText(const bool withDatasetName = false) const;

    bool hasDefaultClasticGrainSize() const {
        return 0 != _defaultClasticGrainSize;
    }

    bool hasDefaultCarbonateGrainSize() const {
        return 0 != _defaultCarbonateGrainSize;
    }

    GrainSizeModes getDefaultGrainSizeMode() const {
        return _defaultGrainSizeMode;
    }

    ClasticGrainSize* getDefaultClasticGrainSize() const {
        return _defaultClasticGrainSize;
    }

    CarbonateGrainSize* getDefaultCarbonateGrainSize() const {
        return _defaultCarbonateGrainSize;
    }

    void setDefaultGrainSizeMode(GrainSizeModes m) {
        if (m != _defaultGrainSizeMode) {
            _defaultCarbonateGrainSize = 0;
            _defaultClasticGrainSize = 0;
        }
        _defaultGrainSizeMode = m;
    }

    void setDefaultCarbonateGrainSize(CarbonateGrainSize* s) {
        if (s) {
            _defaultGrainSizeMode = CarbonateGrainSizeMode;
            _defaultClasticGrainSize = 0;
        }

        _defaultCarbonateGrainSize = s;
    }

    void setDefaultClasticGrainSize(ClasticGrainSize* s) {
        if (s) {
            _defaultGrainSizeMode = ClasticGrainSizeMode;
            _defaultCarbonateGrainSize = 0;
        }

        _defaultClasticGrainSize = s;
    }

    QString getDefaultGrainSizeModeName();
    QString getDefaultGrainSizeName();
    
private:
    GrainSizeModes _defaultGrainSizeMode;
    CarbonateGrainSize* _defaultCarbonateGrainSize;
    ClasticGrainSize* _defaultClasticGrainSize;
};

#endif	/* _Lithology_H */

