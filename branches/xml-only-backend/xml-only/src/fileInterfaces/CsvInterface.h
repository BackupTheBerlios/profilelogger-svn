/* 
 * File:   CsvInterface.h
 * Author: jolo
 *
 * Created on 28. Januar 2010, 08:43
 */

#ifndef _CSVINTERFACE_H
#define	_CSVINTERFACE_H

#include <QObject>

#include <QString>
#include <QStringList>
#include <QList>

class CsvInterface : public QObject {
    Q_OBJECT
public:
    CsvInterface(QObject* p);
    virtual ~CsvInterface();

    QString getFileName() const {
        return _fileName;
    }

    QList<QStringList> getData(const QString& fieldSepChar);
    
public slots:
    void setFileName(const QString& s);

private:
    QString _fileName;
};

#endif	/* _CSVINTERFACE_H */

