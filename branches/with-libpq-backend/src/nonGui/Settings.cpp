/* 
 * File:   Settings.cpp
 * Author: jolo
 * 
 * Created on 11. Dezember 2009, 09:29
 */

#include "Settings.h"

#include <QSettings>
#include <qcoreapplication.h>

Settings::Settings(QObject* parent)
: QObject(parent) {
    QCoreApplication::setOrganizationName("Johannes Lochmann");
    QCoreApplication::setOrganizationDomain("johanneslochmann.blogspot.com");
    QCoreApplication::setApplicationName("ProfileLogger");
}

Settings::~Settings() {
}

void Settings::setLastFile(const QString& f) {
    QSettings s;
    s.setValue("LastFile", f);
}

QString Settings::getLastFile() {
    QSettings s;
    return s.value("LastFile", QVariant()).toString();
}

void Settings::setLithologiesPatternPath(const QString& p) {
    QSettings s;
    s.setValue("LithologiesPatternPath", p);
}

QString Settings::getLithologiesPatternPath() {
    QSettings s;
    return s.value("LithologiesPatternPath", QVariant()).toString();
}

void Settings::setBeddingTypesPatternPath(const QString& p) {
    QSettings s;
    s.setValue("BeddingTypesPatternPath", p);
}

QString Settings::getBeddingTypesPatternPath() {
    QSettings s;
    return s.value("BeddingTypesPatternPath", QVariant()).toString();
}

void Settings::setGraphicsViewScaleStep(qreal r) {
    QSettings s;
    s.setValue("GraphicsViewScaleStep", r);
}

qreal Settings::getGraphicsViewScaleStep() {
    QSettings s;
    return s.value("GraphicsViewScaleStep", QVariant(0.2)).toDouble();
}

void Settings::setFossilsPath(const QString& p) {
    QSettings s;
    s.setValue("FossilsPath", p);
}

QString Settings::getFossilsPath() {
    QSettings s;
    return s.value("FossilsPath", QVariant()).toString();
}

void Settings::setSedimentStructuresPath(const QString& p) {
    QSettings s;
    s.setValue("SedimentStructuresPath", p);
}

QString Settings::getSedimentStructuresPath() {
    QSettings s;
    return s.value("SedimentStructuresPath", QVariant()).toString();
}

void Settings::setCustomSymbolsPath(const QString& p) {
    QSettings s;
    s.setValue("CustomSymbolsPath", p);
}

QString Settings::getCustomSymbolsPath() {
    QSettings s;
    return s.value("CustomSymbolsPath", QVariant()).toString();
}

void Settings::setBoundaryTypesPath(const QString& p) {
    QSettings s;
    s.setValue("BoundaryTypesPath", p);
}

QString Settings::getBoundaryTypesPath() {
    QSettings s;
    return s.value("BoundaryTypesPath", QVariant()).toString();
}

void Settings::setFaciesPath(const QString& p) {
    QSettings s;
    s.setValue("FaciesPath", p);
}

QString Settings::getFaciesPath() {
    QSettings s;
    return s.value("FaciesPath", QVariant()).toString();
}

void Settings::setOutcropQualitiesPath(const QString& p) {
    QSettings s;
    s.setValue("OutcropQualitiesPath", p);
}

QString Settings::getOutcropQualitiesPath() {
    QSettings s;
    return s.value("OutcropQualitiesPath", QVariant()).toString();
}

void Settings::setImagePath(const QString& p) {
    QSettings s;
    s.setValue("ImagePath", p);
}

QString Settings::getImagePath() {
    QSettings s;
    return s.value("ImagePath", QVariant()).toString();
}

void Settings::setLanguageFile(const QString& p) {
    QSettings s;
    s.setValue("LanguageFile", p);
}

QString Settings::getLanguageFile() {
    QSettings s;
    return s.value("LanguageFile", QVariant()).toString();
}

void Settings::setDatabaseConnectionSettings(const DatabaseConnectionSettings& x) {
  QSettings s;
  s.setValue("DatabaseConnection/Host", x.getHost());
  s.setValue("DatabaseConnection/Port", x.getPort());
  s.setValue("DatabaseConnection/Database", x.getDatabase());
  s.setValue("DatabaseConnection/User", x.getUser());
  s.setValue("DatabaseConnection/DropSchema", QVariant(x.getDropSchema()).toInt());
  s.setValue("DatabaseConnection/CreateSchema", QVariant(x.getCreateSchema()).toInt());
  s.setValue("DatabaseConnection/InsertTemplateData", QVariant(x.getInsertTemplateData()).toInt());
}

DatabaseConnectionSettings Settings::getDatabaseConnectionSettings() {
  QSettings s;
  return DatabaseConnectionSettings(s.value("DatabaseConnection/Host").toString(),
				    s.value("DatabaseConnection/Port").toInt(),
				    s.value("DatabaseConnection/Database").toString(),
				    s.value("DatabaseConnection/User").toString(),
				    QString::null,
				    (bool)(s.value("DatabaseConnection/DropSchema").toInt()),
				    (bool)(s.value("DatabaseConnection/CreateSchema").toInt()),
				    (bool)(s.value("DatabaseConnection/InsertTemplateData").toInt()));
}


