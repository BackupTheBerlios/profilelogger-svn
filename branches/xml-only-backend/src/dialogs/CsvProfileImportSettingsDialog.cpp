/* 
 * File:   CsvProfileImportSettingsDialog.cpp
 * Author: jolo
 * 
 * Created on 27. Januar 2010, 21:11
 */

#include "CsvProfileImportSettingsDialog.h"

#include <QWidget>
#include <QLayout>
#include <QDialogButtonBox>
#include <QLabel>
#include <QLineEdit>
#include <QPushButton>
#include <QCheckBox>
#include <QFileDialog>

#include "CsvProfileImportSettings.h"

CsvProfileImportSettingsDialog::CsvProfileImportSettingsDialog(QWidget* p, CsvProfileImportSettings* s)
: QDialog(p),
_settings(s) {
    setLayout(new QVBoxLayout(this));
    setupContentWidget();
    _bbW = new QDialogButtonBox(QDialogButtonBox::Ok | QDialogButtonBox::Cancel,
            Qt::Horizontal,
            this);
    
    layout()->addWidget(_bbW);

    connect(_bbW, SIGNAL(accepted()), this, SLOT(slotAccept()));
    connect(_bbW, SIGNAL(rejected()), this, SLOT(slotReject()));

    showData();
}

CsvProfileImportSettingsDialog::~CsvProfileImportSettingsDialog() {
}

void CsvProfileImportSettingsDialog::setupContentWidget() {
    QWidget* w = new QWidget(this);
    QGridLayout* wl = new QGridLayout(w);
    int lC = 0;
    int wC = 1;
    int r = 0;

    QWidget* browseW = new QWidget(w);
    browseW->setLayout(new QHBoxLayout(browseW));

    _fileNameW = new QLineEdit(browseW);
    _fileNameW->setReadOnly(true);
    _browseFileNameW = new QPushButton(tr("..."), browseW);
    browseW->layout()->addWidget(_fileNameW);
    browseW->layout()->addWidget(_browseFileNameW);

    _ignoreFirstLineW = new QCheckBox(tr("Ignore first line"), w);
    _fieldSepW = new QLineEdit(w);
    _quoteCharW = new QLineEdit(w);

    wl->addWidget(new QLabel(tr("File"), w), r, lC);
    wl->addWidget(browseW, r, wC);
    r++;

    wl->addWidget(_ignoreFirstLineW, r, wC);
    r++;

    wl->addWidget(new QLabel(tr("Field Separator"), w), r, lC);
    wl->addWidget(_fieldSepW);
    r++;

    wl->addWidget(new QLabel(tr("String Enclosed in"), w), r, lC);
    wl->addWidget(_quoteCharW);

    connect(_browseFileNameW, SIGNAL(clicked()), this, SLOT(slotBrowseFile()));
    connect(_fieldSepW, SIGNAL(textChanged(const QString&)), this, SLOT(slotFieldSeparatorChanged(const QString&)));
    connect(_quoteCharW, SIGNAL(textChanged(const QString&)), this, SLOT(slotQuoteCharChanged(const QString&)));
    
    layout()->addWidget(w);
}

void CsvProfileImportSettingsDialog::slotAccept() {
    done(QDialog::Accepted);
}

void CsvProfileImportSettingsDialog::slotReject() {
    done(QDialog::Rejected);
}

void CsvProfileImportSettingsDialog::slotBrowseFile() {
    QFileInfo fi(_settings->getFileName());

    QString fn = QFileDialog::getOpenFileName(this,
            tr("Select File"), fi.absolutePath(),
            tr("CSV Files (*.csv *.CSV"));

    _settings->setFileName(fn);
    _fileNameW->setText(fn);
}

void CsvProfileImportSettingsDialog::slotFieldSeparatorChanged(const QString& s) {
    _settings->setSepChar(s);
}

void CsvProfileImportSettingsDialog::slotIgnoreFirstLineToggled(bool b) {
    _settings->setIgnoreFirstLine(b);
}

void CsvProfileImportSettingsDialog::slotQuoteCharChanged(const QString& s) {
    _settings->setStringSepChar(s);
}

void CsvProfileImportSettingsDialog::showData() {
    if (!_settings) {
        return;
    }

    _fileNameW->setText(_settings->getFileName());

    if (_settings->getIgnoreFirstLine()) {
        _ignoreFirstLineW->setCheckState(Qt::Checked);
    } else {
        _ignoreFirstLineW->setCheckState(Qt::Unchecked);
    }

    _fieldSepW->setText(_settings->getSepChar());
    _quoteCharW->setText(_settings->getStringSepChar());
}
