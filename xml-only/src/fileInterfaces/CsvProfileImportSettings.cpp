/* 
 * File:   CsvProfileImportSettings.cpp
 * Author: jolo
 * 
 * Created on 27. Januar 2010, 20:58
 */

#include "CsvProfileImportSettings.h"

CsvProfileImportSettings::CsvProfileImportSettings(const QString& fn,
        bool ignoreFirstLine,
        const QString& sepChar,
        const QString& stringSepChar) :
ProfileImportSettings(fn),
_ignoreFirstLine(ignoreFirstLine),
_sepChar(sepChar),
_stringSepChar(stringSepChar) {
}

CsvProfileImportSettings::~CsvProfileImportSettings() {
}

