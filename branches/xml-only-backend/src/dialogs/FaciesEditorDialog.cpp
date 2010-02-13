/*
 * File:   FaciesEditorDialog.cpp
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 21:39
 */

#include "FaciesEditorDialog.h"

#include "Facies.h"
#include "ProfileLogger.h"
#include "Settings.h"

FaciesEditorDialog::FaciesEditorDialog(QWidget* parent, Facies* p)
: DatasetWithFileNameEditorDialog(parent, p) {
    addMainPage(tr("Facies"));
    addIdLabel();
    addNameEdit();
    addFileNameBrowser(tr("Pattern File"),
            (static_cast<ProfileLogger*> (QApplication::instance()))->getSettings()->getFaciesPath());
    addDescriptionEdit();
    addButtons();

    emit showDatasetRequest(getFacies());
    slotShowDataset(getFacies());
}

FaciesEditorDialog::~FaciesEditorDialog() {
}

Facies* FaciesEditorDialog::getFacies() {
    return (Facies*) getDataset();
}
