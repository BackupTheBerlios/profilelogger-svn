/* 
 * File:   Settings.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 09:29
 */

#ifndef _SETTINGS_H
#define	_SETTINGS_H

#include <QObject>

#include <QString>
#include <QDir>

class Settings: public QObject {
    Q_OBJECT
public:
    Settings(QObject* parent = 0);
    virtual ~Settings();

    void setLastFile(const QString& s);
    QString getLastFile();
    QString getDefaultFileName() { return QDir::homePath() + "/ProfileLoggerProject.xml"; }

    void setBeddingTypesPatternPath(const QString& s);
    QString getBeddingTypesPatternPath();
    
    void setLithologiesPatternPath(const QString& s);
    QString getLithologiesPatternPath();

    void setFossilsPath(const QString& s);
    QString getFossilsPath();

    void setSedimentStructuresPath(const QString& s);
    QString getSedimentStructuresPath();

    void setCustomSymbolsPath(const QString& s);
    QString getCustomSymbolsPath();

    void setBoundaryTypesPath(const QString& s);
    QString getBoundaryTypesPath();
    
    void setGraphicsViewScaleStep(qreal r);
    qreal getGraphicsViewScaleStep();

    void setFaciesPath(const QString& s);
    QString getFaciesPath();

    void setOutcropQualitiesPath(const QString& s);
    QString getOutcropQualitiesPath();
    
    void setImagePath(const QString& s);
    QString getImagePath();

    void setLanguageFile(const QString& f);
    QString getLanguageFile();
};

#endif	/* _SETTINGS_H */

