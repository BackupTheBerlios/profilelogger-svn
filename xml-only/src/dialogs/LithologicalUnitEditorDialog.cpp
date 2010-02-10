/*
 * File:   LithologicalUnitEditorDialog.cpp
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 21:39
 */

#include "LithologicalUnitEditorDialog.h"

#include <QLayout>
#include <QLabel>
#include <QGroupBox>

#include "LithologicalUnit.h"
#include "LithologicalUnitTypeView.h"
#include "ProfileLogger.h"

LithologicalUnitEditorDialog::LithologicalUnitEditorDialog(QWidget* parent, LithologicalUnit* p)
: DatasetEditorDialog(parent, p) {
    addMainPage(tr("Lithological Unit"));
    addIdLabel();
    addNameEdit();

    _typeV = new LithologicalUnitTypeView(getMainPage(),
            (static_cast<ProfileLogger*>(QApplication::instance()))->getLithologicalUnitTypeItemModel());

    QGridLayout* l = static_cast<QGridLayout*>(getMainPage()->layout());
    QLabel* lbl = new QLabel(tr("Unit Type"), getMainPage());
    lbl->setAlignment(Qt::AlignTop);
    
    l->addWidget(lbl, r, lC);
    l->addWidget(_typeV, r, wC);
    r++;
    
    addDescriptionEdit();
    addButtons();

    connect(_typeV, SIGNAL(currentLithologicalUnitTypeChanged(LithologicalUnitType*)),
            this, SLOT(slotLithologicalUnitTypeChanged(LithologicalUnitType*)));

    _typeV->selectLithologicalUnitType(getLithologicalUnit()->getLithologicalUnitType());
    emit showDatasetRequest(getLithologicalUnit());
    slotShowDataset(getLithologicalUnit());
}

LithologicalUnitEditorDialog::~LithologicalUnitEditorDialog() {
}

LithologicalUnit* LithologicalUnitEditorDialog::getLithologicalUnit() {
    return (LithologicalUnit*) getDataset();
}

void LithologicalUnitEditorDialog::slotLithologicalUnitTypeChanged(LithologicalUnitType* t) {
    getLithologicalUnit()->setLithologicalUnitType(t);
}
