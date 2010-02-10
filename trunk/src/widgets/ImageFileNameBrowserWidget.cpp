/*
 * File:   ImageFileNameBrowserWidget.cpp
 * Author: jolo
 *
 * Created on 17. Dezember 2009, 13:40
 */

#include "ImageFileNameBrowserWidget.h"
#include "ProfileLogger.h"

#include <QLayout>
#include <QLineEdit>
#include <QPushButton>
#include <QFileDialog>
#include <QApplication>
#include <QSvgWidget>
#include <QLabel>

#include "Settings.h"

ImageFileNameBrowserWidget::ImageFileNameBrowserWidget(QWidget* p,
        const QString& filter)
: QWidget(p),
_defaultPath(QString::null),
_filter(filter) {
    setLayout(new QHBoxLayout(this));
    _previewW = new QLabel(this);
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
    connect(_removeW, SIGNAL(clicked()), this, SLOT(slotRemoveImageFileName()));
    connect(this, SIGNAL(fileNameChanged(const QString&)), this, SLOT(setImageFileName(const QString&)));
}

ImageFileNameBrowserWidget::~ImageFileNameBrowserWidget() {
}

void ImageFileNameBrowserWidget::setDefaultPath(const QString& s) {
    _defaultPath = s;
}

void ImageFileNameBrowserWidget::slotBrowse() {
    QString n = QFileDialog::getOpenFileName(this,
            tr("Image File"),
            _defaultPath,
            _filter);
    if (n.isEmpty()) {
        return;
    }

    QFileInfo fi(n);

    emit fileNameChanged(fi.fileName());
}

void ImageFileNameBrowserWidget::slotRemoveImageFileName() {
    _displayW->clear();
    _previewW->setText(QString::null);
    emit fileNameChanged(QString::null);
}

void ImageFileNameBrowserWidget::setImageFileName(const QString& s) {
    _displayW->setText(s);
    QPixmap p;
    p.load(QFileInfo(_defaultPath, s).absoluteFilePath());
    _previewW->setPixmap(p.scaled(QSize(300, 300), Qt::KeepAspectRatio));
}
