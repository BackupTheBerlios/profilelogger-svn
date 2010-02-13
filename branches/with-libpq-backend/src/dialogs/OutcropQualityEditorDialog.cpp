/*
 * File:   OutcropQualityEditorDialog.cpp
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 21:39
 */

#include "OutcropQualityEditorDialog.h"

#include "OutcropQuality.h"
#include "ProfileLogger.h"
#include "Settings.h"

OutcropQualityEditorDialog::OutcropQualityEditorDialog(QWidget* parent, OutcropQuality* p)
: DatasetWithFileNameEditorDialog(parent, p) {
    addMainPage(tr("Outcrop Quality"));
    addIdLabel();
    addNameEdit();
    addFileNameBrowser(tr("Pattern File"),
            (static_cast<ProfileLogger*>(QApplication::instance()))->getSettings()->getOutcropQualitiesPath());
    addDescriptionEdit();
    addButtons();

    emit showDatasetRequest(getOutcropQuality());
    slotShowDataset(getOutcropQuality());
}

OutcropQualityEditorDialog::~OutcropQualityEditorDialog() {
}

OutcropQuality* OutcropQualityEditorDialog::getOutcropQuality() {
    return (OutcropQuality*) getDataset();
}
