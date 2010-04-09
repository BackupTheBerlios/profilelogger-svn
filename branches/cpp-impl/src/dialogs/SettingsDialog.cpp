/* 
 * File:   SettingsDialog.cpp
 * Author: jolo
 * 
 * Created on 15. Dezember 2009, 10:22
 */

#include "SettingsDialog.h"

#include <QDialogButtonBox>
#include <QLabel>
#include <QPushButton>
#include <QLayout>
#include <QApplication>
#include <QSpinBox>
#include <QFileDialog>
#include <QGroupBox>
#include <QLineEdit>

#include "ProfileLogger.h"
#include "Settings.h"

SettingsDialog::SettingsDialog(QWidget* p)
: QDialog(p) {
    setLayout(new QVBoxLayout(this));

    _settings = (static_cast<ProfileLogger*> (QApplication::instance()))->getSettings();

    QGroupBox* b = new QGroupBox(this);
    b->setTitle(tr("Settings"));
    QGridLayout* bl = new QGridLayout(b);
    b->setLayout(bl);
    int r = 0;
    int lC = 0;
    int wC = 1;
    int w2C = 2;

    layout()->addWidget(b);

    _lithologiesPatternPathW = new QLineEdit(_settings->getLithologiesPatternPath(), b);
    _lithologiesPatternPathW->setReadOnly(true);
    _beddingTypesPatternPathW = new QLineEdit(_settings->getBeddingTypesPatternPath(), b);
    _beddingTypesPatternPathW->setReadOnly(true);
    _fossilsPathW = new QLineEdit(_settings->getFossilsPath(), b);
    _fossilsPathW->setReadOnly(true);
    _customSymbolsPathW = new QLineEdit(_settings->getCustomSymbolsPath(), b);
    _customSymbolsPathW->setReadOnly(true);
    _sedimentStructuresPathW = new QLineEdit(_settings->getSedimentStructuresPath(), b);
    _sedimentStructuresPathW->setReadOnly(true);
    _boundaryTypesPathW = new QLineEdit(_settings->getBoundaryTypesPath(), b);
    _boundaryTypesPathW->setReadOnly(true);
    _faciesPathW = new QLineEdit(_settings->getFaciesPath(), b);
    _faciesPathW->setReadOnly(true);
    _imagePathW = new QLineEdit(_settings->getImagePath(), b);
    _imagePathW->setReadOnly(true);
    _outcropQualitiesPathW = new QLineEdit(_settings->getOutcropQualitiesPath(), b);
    _outcropQualitiesPathW->setReadOnly(true);
    _languageFileW = new QLineEdit(_settings->getLanguageFile(), b);
    _languageFileW->setReadOnly(true);

    _browseLithologiesPatternPathW = new QPushButton(tr("..."), b);
    _browseBeddingTypesPatternPathW = new QPushButton(tr("..."), b);
    _browseFossilsPathW = new QPushButton(tr("..."), b);
    _browseSedimentStructuresPathW = new QPushButton(tr("..."), b);
    _browseCustomSymbolsPathW = new QPushButton(tr("..."), b);
    _browseBoundaryTypesPathW = new QPushButton(tr("..."), b);
    _browseFaciesPathW = new QPushButton(tr("..."), b);
    _browseImagePathW = new QPushButton(tr("..."), b);
    _browseOutcropQualitiesPathW = new QPushButton(tr("..."), b);
    _browseLanguageFileW = new QPushButton(tr("..."), b);

    bl->addWidget(new QLabel(tr("Language File: "), b), r, lC);
    bl->addWidget(_languageFileW, r, wC);
    bl->addWidget(_browseLanguageFileW, r, w2C);
    r++;

    bl->addWidget(new QLabel(tr("Lithologies Pattern Path: "), b), r, lC);
    bl->addWidget(_lithologiesPatternPathW, r, wC);
    bl->addWidget(_browseLithologiesPatternPathW, r, w2C);
    r++;

    bl->addWidget(new QLabel(tr("Bedding Types Pattern Path: "), b), r, lC);
    bl->addWidget(_beddingTypesPatternPathW, r, wC);
    bl->addWidget(_browseBeddingTypesPatternPathW, r, w2C);
    r++;

    bl->addWidget(new QLabel(tr("Fossils Path: "), b), r, lC);
    bl->addWidget(_fossilsPathW, r, wC);
    bl->addWidget(_browseFossilsPathW, r, w2C);
    r++;

    bl->addWidget(new QLabel(tr("Sediment Structures Path: "), b), r, lC);
    bl->addWidget(_sedimentStructuresPathW, r, wC);
    bl->addWidget(_browseSedimentStructuresPathW, r, w2C);
    r++;

    bl->addWidget(new QLabel(tr("Custom Symbols Path: "), b), r, lC);
    bl->addWidget(_customSymbolsPathW, r, wC);
    bl->addWidget(_browseCustomSymbolsPathW, r, w2C);
    r++;

    bl->addWidget(new QLabel(tr("Boundary Types Path: "), b), r, lC);
    bl->addWidget(_boundaryTypesPathW, r, wC);
    bl->addWidget(_browseBoundaryTypesPathW, r, w2C);
    r++;

    bl->addWidget(new QLabel(tr("Facies Path: "), b), r, lC);
    bl->addWidget(_faciesPathW, r, wC);
    bl->addWidget(_browseFaciesPathW, r, w2C);
    r++;

    bl->addWidget(new QLabel(tr("Outcrop Qualities Path: "), b), r, lC);
    bl->addWidget(_outcropQualitiesPathW, r, wC);
    bl->addWidget(_browseOutcropQualitiesPathW, r, w2C);
    r++;

    bl->addWidget(new QLabel(tr("Image Path: "), b), r, lC);
    bl->addWidget(_imagePathW, r, wC);
    bl->addWidget(_browseImagePathW, r, w2C);
    r++;

    bl->addWidget(new QLabel(tr("Graphics View Scale Step"), b), r, lC);
    _graphicsViewScaleStepW = new QSpinBox(b);
    _graphicsViewScaleStepW->setToolTip(tr("This is the scale factor the graphic column view will be scaled on each scale action."));
    _graphicsViewScaleStepW->setRange(1, 10);
    _graphicsViewScaleStepW->setValue((int)(_settings->getGraphicsViewScaleStep() * 10));
    bl->addWidget(_graphicsViewScaleStepW, r, wC);
    r++;

    _bbW = new QDialogButtonBox(QDialogButtonBox::Close,
            Qt::Horizontal,
            this);
    layout()->addWidget(_bbW);

    connect(_browseLithologiesPatternPathW, SIGNAL(clicked()), this, SLOT(slotBrowseLithologiesPatternPath()));
    connect(_browseBeddingTypesPatternPathW, SIGNAL(clicked()), this, SLOT(slotBrowseBeddingTypesPatternPath()));
    connect(_browseFossilsPathW, SIGNAL(clicked()), this, SLOT(slotBrowseFossilsPath()));
    connect(_browseCustomSymbolsPathW, SIGNAL(clicked()), this, SLOT(slotBrowseCustomSymbolsPath()));
    connect(_browseSedimentStructuresPathW, SIGNAL(clicked()), this, SLOT(slotBrowseSedimentStructuresPath()));
    connect(_browseBoundaryTypesPathW, SIGNAL(clicked()), this, SLOT(slotBrowseBoundaryTypesPath()));
    connect(_browseFaciesPathW, SIGNAL(clicked()), this, SLOT(slotBrowseFaciesPath()));
    connect(_browseImagePathW, SIGNAL(clicked()), this, SLOT(slotBrowseImagePath()));
    connect(_graphicsViewScaleStepW, SIGNAL(valueChanged(int)), this, SLOT(slotGraphicsViewScaleStepChanged(int)));
    connect(_browseOutcropQualitiesPathW, SIGNAL(clicked()), this, SLOT(slotBrowseOutcropQualitiesPath()));
connect(_browseLanguageFileW, SIGNAL(clicked()), this, SLOT(slotBrowseLanguageFile()));
    
    connect(_bbW, SIGNAL(rejected()), this, SLOT(close()));
}

SettingsDialog::~SettingsDialog() {
}

void SettingsDialog::slotBrowseLithologiesPatternPath() {
    QString dir = QFileDialog::getExistingDirectory(this,
            tr("Lithologies Pattern Path"),
            _settings->getLithologiesPatternPath());

    if (!dir.isEmpty()) {
        _settings->setLithologiesPatternPath(dir);
        _lithologiesPatternPathW->setText(_settings->getLithologiesPatternPath());
    }
}

void SettingsDialog::slotBrowseBeddingTypesPatternPath() {
    QString dir = QFileDialog::getExistingDirectory(this,
            tr("Bedding Types Pattern Path"),
            _settings->getBeddingTypesPatternPath());

    if (!dir.isEmpty()) {
        _settings->setBeddingTypesPatternPath(dir);
        _beddingTypesPatternPathW->setText(_settings->getBeddingTypesPatternPath());
    }
}

void SettingsDialog::slotGraphicsViewScaleStepChanged(int i) {
    _settings->setGraphicsViewScaleStep(i / 10.0);
}

void SettingsDialog::slotBrowseFossilsPath() {
    QString dir = QFileDialog::getExistingDirectory(this,
            tr("Fossils Path"),
            _settings->getFossilsPath());

    if (!dir.isEmpty()) {
        _settings->setFossilsPath(dir);
        _fossilsPathW->setText(_settings->getFossilsPath());
    }
}

void SettingsDialog::slotBrowseSedimentStructuresPath() {
    QString dir = QFileDialog::getExistingDirectory(this,
            tr("Sediment Structures Path"),
            _settings->getSedimentStructuresPath());

    if (!dir.isEmpty()) {
        _settings->setSedimentStructuresPath(dir);
        _sedimentStructuresPathW->setText(_settings->getSedimentStructuresPath());
    }
}

void SettingsDialog::slotBrowseCustomSymbolsPath() {
    QString dir = QFileDialog::getExistingDirectory(this,
            tr("Custom Symbols Path"),
            _settings->getCustomSymbolsPath());

    if (!dir.isEmpty()) {
        _settings->setCustomSymbolsPath(dir);
        _customSymbolsPathW->setText(_settings->getCustomSymbolsPath());
    }
}

void SettingsDialog::slotBrowseBoundaryTypesPath() {
    QString dir = QFileDialog::getExistingDirectory(this,
            tr("Boundary Types Path"),
            _settings->getBoundaryTypesPath());

    if (!dir.isEmpty()) {
        _settings->setBoundaryTypesPath(dir);
        _boundaryTypesPathW->setText(_settings->getBoundaryTypesPath());
    }
}

void SettingsDialog::slotBrowseFaciesPath() {
    QString dir = QFileDialog::getExistingDirectory(this,
            tr("Facies Path"),
            _settings->getFaciesPath());

    if (!dir.isEmpty()) {
        _settings->setFaciesPath(dir);
        _faciesPathW->setText(_settings->getFaciesPath());
    }
}

void SettingsDialog::slotBrowseImagePath() {
    QString dir = QFileDialog::getExistingDirectory(this,
            tr("Image Path"),
            _settings->getImagePath());

    if (!dir.isEmpty()) {
        _settings->setImagePath(dir);
        _imagePathW->setText(_settings->getImagePath());
    }
}

void SettingsDialog::slotBrowseOutcropQualitiesPath() {
    QString dir = QFileDialog::getExistingDirectory(this,
            tr("Outcrop Qualities Path"),
            _settings->getOutcropQualitiesPath());

    if (!dir.isEmpty()) {
        _settings->setOutcropQualitiesPath(dir);
        _outcropQualitiesPathW->setText(_settings->getOutcropQualitiesPath());
    }
}

void SettingsDialog::slotBrowseLanguageFile() {
    QString f = QFileDialog::getOpenFileName(this,
            tr("Language File"),
tr("Language Files (*.qm)"));

    if (!f.isEmpty()) {
        _settings->setLanguageFile(f);
        _languageFileW->setText(_settings->getLanguageFile());
    }
}
