/* 
 * File:   DatasetEditorDialog.cpp
 * Author: jolo
 * 
 * Created on 10. Dezember 2009, 21:22
 */

#include "DatasetEditorDialog.h"

#include <QDialog>

#include <QLayout>
#include <QDialogButtonBox>
#include <QGroupBox>
#include <QTabWidget>

#include "IdLabel.h"
#include "NameEdit.h"
#include "DescriptionEdit.h"
#include "Dataset.h"
#include "CustomSymbolInBedItemModel.h"

DatasetEditorDialog::DatasetEditorDialog(QWidget* p, Dataset* d)
: QDialog(p),
r(0),
lC(0),
wC(1),
_data(d),
_tabW(0),
_idW(0),
_mainPageW(0),
_nameW(0),
_descriptionW(0),
_bbW(0) {
    setLayout(new QVBoxLayout());
    _tabW = new QTabWidget(this);
    layout()->addWidget(_tabW);
    connect(this, SIGNAL(showDatasetRequest(Dataset*)), this, SLOT(slotShowDataset(Dataset*)));
}

DatasetEditorDialog::~DatasetEditorDialog() {
}

QWidget* DatasetEditorDialog::addMainPage(const QString& title) {
    _mainPageW = new QGroupBox(_tabW);
    _mainPageW->setLayout(new QGridLayout());
    _tabW->addTab(_mainPageW, title);
    return _mainPageW;
}

IdLabel* DatasetEditorDialog::addIdLabel() {
    _idW = new IdLabel(_mainPageW);
    ((QGridLayout*) (_mainPageW->layout()))->addWidget(_idW->getLabel(), r, lC);
    ((QGridLayout*) (_mainPageW->layout()))->addWidget(_idW, r, wC);
    r++;
    return _idW;
}

NameEdit* DatasetEditorDialog::addNameEdit() {
    _nameW = new NameEdit(_mainPageW);
    connect(_nameW, SIGNAL(nameChanged(const QString&)), this, SLOT(slotNameChanged(const QString&)));
    ((QGridLayout*) (_mainPageW->layout()))->addWidget(_nameW->getLabel(), r, lC);
    ((QGridLayout*) (_mainPageW->layout()))->addWidget(_nameW, r, wC);
    r++;
    return _nameW;
}

DescriptionEdit* DatasetEditorDialog::addDescriptionEdit() {
    _descriptionW = new DescriptionEdit(_mainPageW);
    connect(_descriptionW, SIGNAL(descriptionChanged(const QString&)), this, SLOT(slotDescriptionChanged(const QString&)));
    ((QGridLayout*) (_mainPageW->layout()))->addWidget(_descriptionW->getLabel(), r, lC);
    ((QGridLayout*) (_mainPageW->layout()))->addWidget(_descriptionW, r, wC);
    r++;
    return _descriptionW;
}

QDialogButtonBox* DatasetEditorDialog::addButtons() {
    _bbW = new QDialogButtonBox(QDialogButtonBox::Ok,
            Qt::Horizontal,
            this);
    connect(_bbW, SIGNAL(accepted()), this, SLOT(close()));
    layout()->addWidget(_bbW);
    return _bbW;
}

void DatasetEditorDialog::slotNameChanged(const QString& s) {
    if (_data) {
        _data->setName(s);
    }
}

void DatasetEditorDialog::slotDescriptionChanged(const QString& s) {
    if (_data) {
        _data->setDescription(s);
    }
}

void DatasetEditorDialog::slotShowDataset(Dataset* d) {
    _data = d;

    if (!_data) {
        clear();
        return;
    }

    if (_idW) {
        _idW->setId(_data->getId());
    }

    if (_nameW) {
        _nameW->setText(_data->getName());
    }

    if (_descriptionW) {
        _descriptionW->setText(_data->getDescription());
    }
}

void DatasetEditorDialog::clear() {
    if (_idW) {
        _idW->setId(0);
    }

    if (_nameW) {
        _nameW->clear();
    }

    if (_descriptionW) {
        _descriptionW->clear();
    }
}

void DatasetEditorDialog::reject() {
    // ignore
}

void DatasetEditorDialog::close() {
    done(QDialog::Accepted);
}
