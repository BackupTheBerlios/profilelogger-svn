/*
 * File:   BoundaryTypeEditorDialog.cpp
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 21:39
 */

#include "BoundaryTypeEditorDialog.h"

#include "BoundaryType.h"
#include "ProfileLogger.h"
#include "Settings.h"

BoundaryTypeEditorDialog::BoundaryTypeEditorDialog(QWidget* parent, BoundaryType* p)
: DatasetWithFileNameEditorDialog(parent, p) {
    addMainPage(tr("Boundary Type"));
    addIdLabel();
    addNameEdit();
    addFileNameBrowser(tr("Pattern File"),
            (static_cast<ProfileLogger*> (QApplication::instance()))->getSettings()->getBoundaryTypesPath());
    addDescriptionEdit();
    addButtons();

    emit showDatasetRequest(getBoundaryType());
    slotShowDataset(getBoundaryType());
}

BoundaryTypeEditorDialog::~BoundaryTypeEditorDialog() {
}

BoundaryType* BoundaryTypeEditorDialog::getBoundaryType() {
    return (BoundaryType*) getDataset();
}
