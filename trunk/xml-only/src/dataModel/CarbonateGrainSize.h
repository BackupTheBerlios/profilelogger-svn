/*
 * File:   CarbonateGrainSize.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:37
 */

#ifndef _CarbonateGrainSize_H
#define	_CarbonateGrainSize_H

#include "GrainSize.h"

class CarbonateGrainSize : public GrainSize {
public:
    CarbonateGrainSize(int id = 0,
            int order = 0,
            const QString& name = QObject::tr("New Carbonate Grain Size"),
            const QString& description = QString::null,
            GraphicColumnHeader::WidthPositions pos = GraphicColumnHeader::ClayEnd);
    virtual ~CarbonateGrainSize();
    QString makeToolTipText(const bool withDatasetName = false) const;
};

#endif	/* _CarbonateGrainSize_H */

