/*
 * File:   ProfileCorrelationEditorDialog.cpp
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 21:39
 */

#include "ProfileCorrelationEditorDialog.h"

#include <QLayout>

#include "ProfileCorrelation.h"
#include "Settings.h"
#include "ProfileLogger.h"
#include "GrainSizeSelectorWidget.h"

ProfileCorrelationEditorDialog::ProfileCorrelationEditorDialog(QWidget* parent, ProfileCorrelation* p)
: DatasetEditorDialog(parent, p) {
    addMainPage(tr("ProfileCorrelation"));
    addIdLabel();
    addNameEdit();
    addDescriptionEdit();
    addButtons();

    emit showDatasetRequest(getProfileCorrelation());
}

ProfileCorrelationEditorDialog::~ProfileCorrelationEditorDialog() {
}

ProfileCorrelation* ProfileCorrelationEditorDialog::getProfileCorrelation() {
    return (ProfileCorrelation*) getDataset();
}
