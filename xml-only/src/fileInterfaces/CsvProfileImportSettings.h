/* 
 * File:   CsvProfileImportSettings.h
 * Author: jolo
 *
 * Created on 27. Januar 2010, 20:58
 */

#ifndef _CSVPROFILEIMPORTSETTINGS_H
#define	_CSVPROFILEIMPORTSETTINGS_H

#include "ProfileImportSettings.h"

class CsvProfileImportSettings: public ProfileImportSettings {
public:
    CsvProfileImportSettings(const QString& fn = QString::null,
            bool ignoreFirstLine = true,
            const QString& sepChar = ";",
            const QString& stringSepChar = "\"");

    virtual ~CsvProfileImportSettings();

    void setIgnoreFirstLine(bool b) {
        _ignoreFirstLine = b;
    }

    bool getIgnoreFirstLine() const {
        return _ignoreFirstLine;
    }

    void setSepChar(const QString& s) {
        _sepChar = s;
    }

    QString getSepChar() const {
        return _sepChar;
    }

    void setStringSepChar(const QString& s) {
        _stringSepChar = s;
    }

    QString getStringSepChar() const {
        return _stringSepChar;
    }
    
private:
    bool _ignoreFirstLine;
    QString _sepChar;
    QString _stringSepChar;
};

#endif	/* _CSVPROFILEIMPORTSETTINGS_H */

