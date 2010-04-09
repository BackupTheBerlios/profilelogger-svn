/* 
 * File:   Image.h
 * Author: jolo
 *
 * Created on 21. Januar 2010, 07:31
 */

#ifndef _IMAGE_H
#define	_IMAGE_H

#include "DatasetWithFileName.h"

#include <QObject>
#include <QStringList>

class Image: public DatasetWithFileName {
public:
    Image(int id = 0,
            const QString& name = QObject::tr("New Image"),
            const QString& description = QString::null,
            const QString& fileName = QString::null);
    virtual ~Image();
    QString makeToolTipText(const bool withDatasetName = false);
};

#endif	/* _IMAGE_H */

