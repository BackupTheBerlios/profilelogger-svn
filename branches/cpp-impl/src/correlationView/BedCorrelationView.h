#ifndef BED_CORRELATION_VIEW_H
#define BED_CORRELATION_VIEW_H

#include <QGraphicsView>

class Project;
class ProfileCorrelation;

class BedCorrelationView: public QGraphicsView {
  Q_OBJECT
    public:
  BedCorrelationView(QWidget* p = 0);
  virtual ~BedCorrelationView();

  public slots:
  virtual void slotCurrentProjectChanged(Project* p);
  virtual void slotCurrentProfileCorrelationChanged(ProfileCorrelation* c);

 private:
  Project* _project;
  ProfileCorrelation* _corr;
};

#endif
