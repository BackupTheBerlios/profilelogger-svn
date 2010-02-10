/*
 * File:   Color.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:37
 */

#ifndef _Color_H
#define	_Color_H

#include "Dataset.h"

#include <QObject>

class Color : public Dataset {
public:
    Color(int id = 0,
            const QString& name = QObject::tr("New Color"),
            const QString& description = QString::null,
            Qt::BrushStyle style = Qt::NoBrush);

    virtual ~Color();
    QString makeToolTipText(const bool withDatasetName = false) const;

    void setBrushStyle(Qt::BrushStyle s) {
        _style = s;
    }

    Qt::BrushStyle getBrushStyle() const {
        return _style;
    }

private:
    Qt::BrushStyle _style;
};

#endif	/* _Color_H */

