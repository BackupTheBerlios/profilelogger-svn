#include "ProfileCorrelationWidget.h"

#include <QApplication>
#include <QSplitter>
#include <QLayout>

#include "ProfileLogger.h"
   
#include "ProfileCorrelationItemModel.h"
#include "ProfileCorrelationItemView.h"
#include "BedCorrelationView.h"

#include "BedCorrelationItemModel.h"
#include "BedCorrelationItemView.h"

ProfileCorrelationWidget::ProfileCorrelationWidget(QWidget* p)
  : QWidget(p),
    _project(0) {
  setEnabled(false);
  setLayout(new QHBoxLayout(this));

  _splitterW = new QSplitter(this);

  _correlationsM =  (static_cast<ProfileLogger*> (QApplication::instance()))->getProfileCorrelationItemModel();
  _correlationsV = new ProfileCorrelationItemView(_splitterW, _correlationsM);
  _graphicsV = new BedCorrelationView(_splitterW);

  _bedCorrelationsM = (static_cast<ProfileLogger*> (QApplication::instance()))->getBedCorrelationItemModel();
  _bedCorrelationsV = new BedCorrelationItemView(_splitterW, _bedCorrelationsM);

  _splitterW->addWidget(_correlationsV);
  _splitterW->addWidget(_bedCorrelationsV);
  _splitterW->addWidget(_graphicsV);

  connect((static_cast<ProfileLogger*> (QApplication::instance())), SIGNAL(currentProjectChanged(Project*)), this, SLOT(slotCurrentProjectChanged(Project*)));
  connect((static_cast<ProfileLogger*> (QApplication::instance())), SIGNAL(currentProjectChanged(Project*)), _graphicsV, SLOT(slotCurrentProjectChanged(Project*)));
  connect(_correlationsV, SIGNAL(currentProfileCorrelationChanged(ProfileCorrelation*)), _bedCorrelationsM, SLOT(slotCurrentProfileCorrelationChanged(ProfileCorrelation*)));
  connect(_correlationsV, SIGNAL(currentProfileCorrelationChanged(ProfileCorrelation*)), _bedCorrelationsV, SLOT(slotCurrentProfileCorrelationChanged(ProfileCorrelation*)));
  connect(_correlationsV, SIGNAL(currentProfileCorrelationChanged(ProfileCorrelation*)), _graphicsV, SLOT(slotCurrentProfileCorrelationChanged(ProfileCorrelation*)));

  layout()->addWidget(_splitterW);
}

ProfileCorrelationWidget::~ProfileCorrelationWidget() {}

void ProfileCorrelationWidget::slotCurrentProjectChanged(Project *p) {
  setEnabled(p);
  _project = p;
}
