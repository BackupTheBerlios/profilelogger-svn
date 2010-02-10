/* 
 * File:   FileNameBrowserWidget.cpp
 * Author: jolo
 * 
 * Created on 17. Dezember 2009, 13:40
 */

#include "FileNameBrowserWidget.h"
#include "ProfileLogger.h"

#include <QLayout>
#include <QLineEdit>
#include <QPushButton>
#include <QFileDialog>
#include <QApplication>
#include <QSvgWidget>

#include "Settings.h"

FileNameBrowserWidget::FileNameBrowserWidget(QWidget* p,
        const QString& filter)
: QWidget(p),
_defaultPath(QString::null),
_filter(filter) {
    setLayout(new QHBoxLayout(this));
    _previewW = new QSvgWidget(this);
    _previewW->setSizePolicy(QSizePolicy::MinimumExpanding, QSizePolicy::MinimumExpanding);
    _displayW = new QLineEdit(this);
    _displayW->setReadOnly(true);
    _browseW = new QPushButton(tr("..."), this);
    _removeW = new QPushButton(tr("Remove"), this);

    layout()->addWidget(_previewW);
    layout()->addWidget(_displayW);
    layout()->addWidget(_browseW);
    layout()->addWidget(_removeW);

    connect(_browseW, SIGNAL(clicked()), this, SLOT(slotBrowse()));
    connect(_removeW, SIGNAL(clicked()), this, SLOT(slotRemoveFileName()));
    connect(this, SIGNAL(fileNameChanged(const QString&)), this, SLOT(setFileName(const QString&)));
}

FileNameBrowserWidget::~FileNameBrowserWidget() {
}

void FileNameBrowserWidget::setDefaultPath(const QString& s) {
    _defaultPath = s;
}

void FileNameBrowserWidget::slotBrowse() {
    QString n = QFileDialog::getOpenFileName(this,
            tr("Scalable Vector Graphics File"),
            _defaultPath,
            _filter);
    if (n.isEmpty()) {
        return;
    }

    QFileInfo fi(n);

    emit fileNameChanged(fi.fileName());
}

void FileNameBrowserWidget::slotRemoveFileName() {
    _displayW->clear();
    emit fileNameChanged(QString::null);
}

void FileNameBrowserWidget::setFileName(const QString& s) {
    _displayW->setText(s);
    _previewW->load(QFileInfo(_defaultPath, s).absoluteFilePath());
}
