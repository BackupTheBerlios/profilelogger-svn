/*
 * File:   ClasticGrainSize.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:37
 */

#ifndef _ClasticGrainSize_H
#define	_ClasticGrainSize_H

#include "GrainSize.h"
#include "GraphicColumnHeader.h"
#include "GraphicBedItem.h"

class ClasticGrainSize : public GrainSize {
public:
    ClasticGrainSize(int id = 0,
            int order = 0,
            const QString& name = QObject::tr("New Clastic Grain Size"),
            const QString& description = QString::null,
            GraphicColumnHeader::WidthPositions pos = GraphicColumnHeader::ClayEnd);
    virtual ~ClasticGrainSize();
    QString makeToolTipText(const bool withDatasetName = false) const;

};

#endif	/* _ClasticGrainSize_H */

