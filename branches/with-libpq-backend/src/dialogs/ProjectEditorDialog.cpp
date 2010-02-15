#include "ProjectEditorDialog.h"

#include <QLayout>
#include <QApplication>

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

void ProjectEditorDialog::accept() {
  try {
      (static_cast<ProfileLogger*>(QApplication::instance()))->getPostgres()->begin();
      ProjectManager* m = new ProjectManager(this,
					     (static_cast<ProfileLogger*>(QApplication::instance()))->getPostgres(),
					     (static_cast<ProfileLogger*>(QApplication::instance()))->getProfileLoggerDatabase());
      m->save(getProject());
      (static_cast<ProfileLogger*>(QApplication::instance()))->getPostgres()->commit();
      done(QDialog::Accepted);
    }
    catch(DatabaseError e) {
      DatabaseErrorDialog dlg(QApplication::activeWindow(), e);
      dlg.exec();

      try {
	(static_cast<ProfileLogger*>(QApplication::instance()))->getPostgres()->rollback();
      }
      catch(DatabaseError e) {
	DatabaseErrorDialog dlg(QApplication::activeWindow(), e);
	dlg.exec();
      }
    }
}
