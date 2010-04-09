/*
 * File:   LithologicalUnitTypeEditorDialog.cpp
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 21:39
 */

#include "LithologicalUnitTypeEditorDialog.h"

#include <QLayout>
#include <QLabel>
#include <QGroupBox>

#include "QtPatternSelectorWidget.h"

#include "LithologicalUnitType.h"

LithologicalUnitTypeEditorDialog::LithologicalUnitTypeEditorDialog(QWidget* parent, LithologicalUnitType* p)
: DatasetEditorDialog(parent, p) {
    addMainPage(tr("Lithological Unit Type"));
    addIdLabel();
    addNameEdit();
    addDescriptionEdit();
    addButtons();

    emit showDatasetRequest(getLithologicalUnitType());
    slotShowDataset(getLithologicalUnitType());
}

LithologicalUnitTypeEditorDialog::~LithologicalUnitTypeEditorDialog() {
}

LithologicalUnitType* LithologicalUnitTypeEditorDialog::getLithologicalUnitType() {
    return (LithologicalUnitType*) getDataset();
}
