#include "ProjectEditorDialog.h"

#include <QLayout>

#include "Project.h"
#include "Settings.h"
#include "ProfileLogger.h"

ProjectEditorDialog::ProjectEditorDialog(QWidget* parent, Project* p)
: DatasetEditorDialog(parent, p) {
    addMainPage(tr("Project"));
    addIdLabel();
    addNameEdit();
    addDescriptionEdit();
    addButtons();

    emit showDatasetRequest(getProject());
    slotShowDataset(getProject());
}

ProjectEditorDialog::~ProjectEditorDialog() {
}

Project* ProjectEditorDialog::getProject() {
    return (Project*) getDataset();
}
