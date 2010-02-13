/*
 * File:   FossilEditorDialog.cpp
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 21:39
 */

#include "FossilEditorDialog.h"

#include "Fossil.h"
#include "Settings.h"
#include "ProfileLogger.h"

FossilEditorDialog::FossilEditorDialog(QWidget* parent, Fossil* p)
: DatasetWithFileNameEditorDialog(parent, p) {
    addMainPage(tr("Fossil"));
    addIdLabel();
    addNameEdit();
    addFileNameBrowser(tr("Symbol File"), 
		       (static_cast<ProfileLogger*> (QApplication::instance()))->getSettings()->getFossilsPath());
    addDescriptionEdit();
    addButtons();

    emit showDatasetRequest(getFossil());
    slotShowDataset(getFossil());
}

FossilEditorDialog::~FossilEditorDialog() {
}

Fossil* FossilEditorDialog::getFossil() {
    return (Fossil*) getDataset();
}
