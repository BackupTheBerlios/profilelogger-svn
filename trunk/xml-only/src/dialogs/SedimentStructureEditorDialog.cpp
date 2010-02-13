/*
 * File:   SedimentStructureEditorDialog.cpp
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 21:39
 */

#include "SedimentStructureEditorDialog.h"

#include "SedimentStructure.h"
#include "Settings.h"
#include "ProfileLogger.h"

SedimentStructureEditorDialog::SedimentStructureEditorDialog(QWidget* parent, SedimentStructure* p)
: DatasetWithFileNameEditorDialog(parent, p) {
    addMainPage(tr("Sediment Structure"));
    addIdLabel();
    addNameEdit();
    addFileNameBrowser(tr("Symbol File"), 
		       (static_cast<ProfileLogger*> (QApplication::instance()))->getSettings()->getSedimentStructuresPath());
    addDescriptionEdit();
    addButtons();

    emit showDatasetRequest(getSedimentStructure());
    slotShowDataset(getSedimentStructure());
}

SedimentStructureEditorDialog::~SedimentStructureEditorDialog() {
}

SedimentStructure* SedimentStructureEditorDialog::getSedimentStructure() {
    return (SedimentStructure*) getDataset();
}
