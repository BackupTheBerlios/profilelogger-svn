#include "DbWorkWidget.h"

#include <QLayout>
#include <QApplication>
#include <QSplitter>

#include "ProfileLogger.h"
#include "ProjectItemModel.h"
#include "ProfileItemModel.h"
#include "ProjectView.h"
#include "ProfileItemView.h"
#include "Postgres.h"

DbWorkWidget::DbWorkWidget(QWidget* p)
  : QWidget(p) {
  setLayout(new QVBoxLayout(this));
  _splW = new QSplitter(this);
  layout()->addWidget(_splW);

  _projectsM = (static_cast<ProfileLogger*>(QApplication::instance()))->getProjectItemModel();
  _projectsV = new ProjectView(_splW, _projectsM);

  _profilesM = (static_cast<ProfileLogger*>(QApplication::instance()))->getProfileItemModel();
  _profilesV = new ProfileItemView(_splW, _profilesM);

  _splW->addWidget(_projectsV);
  _splW->addWidget(_profilesV);

  connect((static_cast<ProfileLogger*>(QApplication::instance()))->getPostgres(), SIGNAL(connectionEstablished(const QString&)),
	  this, SLOT(slotDatabaseConnected(const QString&)));
  connect((static_cast<ProfileLogger*>(QApplication::instance()))->getPostgres(), SIGNAL(connectionClosed()),
	  this, SLOT(slotDatabaseClosed()));
  connect((static_cast<ProfileLogger*>(QApplication::instance()))->getPostgres(), SIGNAL(connectionLost()),
	  this, SLOT(slotDatabaseLost()));

  connect(_projectsV, SIGNAL(currentProjectChanged(Project*)), _profilesM, SLOT(slotCurrentProjectChanged(Project*)));

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

