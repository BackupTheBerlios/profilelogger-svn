/* 
 * File:   Sample.cpp
 * Author: jolo
 * 
 * Created on 20. Januar 2010, 16:47
 */

#include "Sample.h"

#include "Profile.h"

Sample::Sample(int id,
        const QString& name,
        const QString& description,
        Profile* profile)
: Dataset(id, name, description),
_profile(profile) {
}

Sample::~Sample() {
}

QString Sample::makeToolTipText(const bool withDatasetName) {
    QStringList ret;

    if (withDatasetName) {
        ret << QObject::tr("Sample");
    }

    ret << QObject::tr("Id: %1").arg(getId())
            << QObject::tr("Name: %1").arg(getName())
            << QObject::tr("Description: %1").arg(getDescription());

    if (hasProfile()) {
        ret << QObject::tr("Profile: %1").arg(getProfile()->getName());
    }
    
    return ret.join("\n");
}
