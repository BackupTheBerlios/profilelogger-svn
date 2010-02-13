/* 
 * File:   Sample.h
 * Author: jolo
 *
 * Created on 20. Januar 2010, 16:47
 */

#ifndef _SAMPLE_H
#define	_SAMPLE_H

#include "Dataset.h"

#include <QObject>
#include <QStringList>

class Profile;

class Sample : public Dataset {
public:
    Sample(int id = 0, const QString& name = QObject::tr("New Sample"),
            const QString& description = QString::null,
            Profile* profile = 0);
    virtual ~Sample();

    bool hasProfile() const {
        return 0 != _profile;
    }

    void setProfile(Profile* p) {
        _profile = p;
    }

    Profile* getProfile() {
        return _profile;
    }

    QString makeToolTipText(const bool withDatasetName = false);
    
private:
    Profile* _profile;
};

#endif	/* _SAMPLE_H */

