/*
 * File:   SampleEditorDialog.cpp
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 21:39
 */

#include "SampleEditorDialog.h"

#include <QLayout>
#include <QLabel>
#include <QGroupBox>

#include "QtPatternSelectorWidget.h"

#include "Sample.h"

SampleEditorDialog::SampleEditorDialog(QWidget* parent, Sample* p)
: DatasetEditorDialog(parent, p) {
    addMainPage(tr("Sample"));
    addIdLabel();
    addNameEdit();
    addDescriptionEdit();
    addButtons();

    emit showDatasetRequest(getSample());
    slotShowDataset(getSample());
}

SampleEditorDialog::~SampleEditorDialog() {
}

Sample* SampleEditorDialog::getSample() {
    return (Sample*) getDataset();
}
