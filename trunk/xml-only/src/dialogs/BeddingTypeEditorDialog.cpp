/*
 * File:   BeddingTypeEditorDialog.cpp
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 21:39
 */

#include "BeddingTypeEditorDialog.h"

#include "BeddingType.h"
#include "Settings.h"
#include "ProfileLogger.h"

BeddingTypeEditorDialog::BeddingTypeEditorDialog(QWidget* parent, BeddingType* p)
: DatasetWithFileNameEditorDialog(parent, p) {
    addMainPage(tr("Bedding Type"));
    addIdLabel();
    addNameEdit();
    addFileNameBrowser(tr("Bedding Type Pattern File"),
            (static_cast<ProfileLogger*> (QApplication::instance()))->getSettings()->getBeddingTypesPatternPath());
    addDescriptionEdit();
    addButtons();

    emit showDatasetRequest(getBeddingType());
    slotShowDataset(getBeddingType());
}

BeddingTypeEditorDialog::~BeddingTypeEditorDialog() {
}

BeddingType* BeddingTypeEditorDialog::getBeddingType() {
    return (BeddingType*) getDataset();
}
