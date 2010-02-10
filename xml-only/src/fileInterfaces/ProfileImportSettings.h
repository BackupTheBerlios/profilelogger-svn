/* 
 * File:   ProfileImportSettings.h
 * Author: jolo
 *
 * Created on 27. Januar 2010, 20:54
 */

#ifndef _PROFILEIMPORTSETTINGS_H
#define	_PROFILEIMPORTSETTINGS_H

#include <QString>

class ProfileImportSettings {
public:
    ProfileImportSettings(const QString& fileName = QString::null);
    virtual ~ProfileImportSettings();

    void setFileName(QString file) {
        _file = file;
    }

    QString getFileName() const {
        return _file;
    }
    
private:
    QString _file;
};

#endif	/* _PROFILEIMPORTSETTINGS_H */

