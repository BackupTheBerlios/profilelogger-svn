/* 
 * File:   OutcropQuality.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:37
 */

#ifndef _OUTCROPQUALITY_H
#define	_OUTCROPQUALITY_H

#include <QObject>
#include <QStringList>

#include "DatasetWithFileName.h"

class OutcropQuality : public DatasetWithFileName {
public:
    OutcropQuality(int id = 0,
            const QString& name = QObject::tr("New Outcrop Quality"),
            const QString& description = QString::null,
            const QString& fileName = QString::null);

    virtual ~OutcropQuality();
    QString makeToolTipText(const bool withDatasetName = false) const;
};

#endif	/* _OUTCROPQUALITY_H */

