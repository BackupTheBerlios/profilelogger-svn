/*
 * File:   GrainSize.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:37
 */

#ifndef _GrainSize_H
#define	_GrainSize_H

#include "Dataset.h"
#include "GraphicColumnHeader.h"

class GrainSize : public Dataset {
public:
    GrainSize(int id = 0,
            int order = 0,
            const QString& name = QObject::tr("New Grain Size"),
            const QString& description = QString::null,
            GraphicColumnHeader::WidthPositions pos = GraphicColumnHeader::ClayEnd);
    virtual ~GrainSize();
    QString makeToolTipText(const bool withDatasetName = false) const;

    void setOrder(int o) {
        _order = o;
    }

    int getOrder() const {
        return _order;
    }

    GraphicColumnHeader::WidthPositions getPosition() {
        return _pos;
    }

private:
    int _order;
    GraphicColumnHeader::WidthPositions _pos;
};

#endif	/* _GrainSize_H */

