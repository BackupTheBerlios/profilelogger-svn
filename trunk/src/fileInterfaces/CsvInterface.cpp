/* 
 * File:   CsvInterface.cpp
 * Author: jolo
 * 
 * Created on 28. Januar 2010, 08:43
 */


#include "CsvInterface.h"

#include <QFile>
#include <QTextStream>
#include <QMessageBox>
#include <QApplication>

#include "ProfileLogger.h"
#include "MainWindow.h"

CsvInterface::CsvInterface(QObject* p)
: QObject(p) {
}

CsvInterface::~CsvInterface() {
}

void CsvInterface::setFileName(const QString& s) {
    _fileName = s;
}

QList<QStringList> CsvInterface::getData(const QString& sepChar) {
    QList<QStringList> ret;

    QFile f(_fileName);

    if (!f.open(QFile::ReadOnly)) {
        QMessageBox::critical((static_cast<ProfileLogger*> (QApplication::instance()))->getMainWindow(),
                tr("Could Not Open File"),
                tr("Could not open file: %1: %2").arg(_fileName).arg(f.errorString()));
        return ret;
    }

    QTextStream strm(&f);

    while (!f.atEnd()) {
        QString l = f.readLine();
        ret << l.split(sepChar);
    }

    return ret;
}
