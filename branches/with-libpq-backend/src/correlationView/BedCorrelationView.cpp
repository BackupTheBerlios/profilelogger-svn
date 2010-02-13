#include "BedCorrelationView.h"

#include <QApplication>

#include "ProfileLogger.h"
#include "Project.h"

BedCorrelationView::BedCorrelationView(QWidget* p)
  : QGraphicsView(p),
    _project(0),
    _corr(0) {
  slotCurrentProjectChanged((static_cast<ProfileLogger*> (QApplication::instance()))->getProject());
  setEnabled(_project && _corr);
}

BedCorrelationView::~BedCorrelationView() {}

void BedCorrelationView::slotCurrentProjectChanged(Project* p) {
  _project = p;
  setEnabled(_project && _corr);
}

void BedCorrelationView::slotCurrentProfileCorrelationChanged(ProfileCorrelation* c) {
  _corr = c;
  setEnabled(_project && _corr);
}

