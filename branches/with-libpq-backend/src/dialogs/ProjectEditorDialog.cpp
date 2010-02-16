#include "ProjectEditorDialog.h"

#include <QLayout>
#include <QApplication>
#include <QDebug>

#include "Project.h"
#include "Settings.h"
#include "ProfileLogger.h"
#include "ProfileLogger.h"
#include "DatabaseError.h"
#include "DatabaseErrorDialog.h"
#include "Postgres.h"
#include "ProjectManager.h"

ProjectEditorDialog::ProjectEditorDialog(QWidget* parent, Project* p)
  : DatasetEditorDialog(parent, p) {
  setDataManager(new ProjectManager(this,
				    getPostgres(),
				    getProfileLoggerDatabase()));

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

ProjectManager* ProjectEditorDialog::getProjectManager() {
  return (ProjectManager*)getDataManager();
}

void ProjectEditorDialog::accept() {
  try {
    begin();
    getProjectManager()->save(getProject());
    commit();
    done(QDialog::Accepted);
  }
  catch(DatabaseError e) {
    DatabaseErrorDialog dlg(QApplication::activeWindow(), e);
    dlg.exec();

    try {
      rollback();
    }
    catch(DatabaseError e) {
      DatabaseErrorDialog dlg(QApplication::activeWindow(), e);
      dlg.exec();
    }
  }
}
