#include "DbWorkWidget.h"

#include <QLayout>
#include <QApplication>

#include "ProfileLogger.h"
#include "ProjectItemModel.h"
#include "ProjectView.h"
#include "Postgres.h"

DbWorkWidget::DbWorkWidget(QWidget* p)
  : QWidget(p) {
  setLayout(new QVBoxLayout(this));
  _projectsM = (static_cast<ProfileLogger*>(QApplication::instance()))->getProjectItemModel();
  _projectsV = new ProjectView(this, _projectsM);

  layout()->addWidget(_projectsV);

  connect((static_cast<ProfileLogger*>(QApplication::instance()))->getPostgres(), SIGNAL(connectionEstablished(const QString&)),
	  this, SLOT(slotDatabaseConnected(const QString&)));
  connect((static_cast<ProfileLogger*>(QApplication::instance()))->getPostgres(), SIGNAL(connectionClosed()),
	  this, SLOT(slotDatabaseClosed()));
  connect((static_cast<ProfileLogger*>(QApplication::instance()))->getPostgres(), SIGNAL(connectionLost()),
	  this, SLOT(slotDatabaseLost()));

  setEnabled(false);
}

void DbWorkWidget::slotDatabaseConnected(const QString& n) {
  (void) n;
  setEnabled(true);
}

void DbWorkWidget::slotDatabaseLost() {
  setEnabled(false);
}

void DbWorkWidget::slotDatabaseClosed() {
  setEnabled(false);
}

