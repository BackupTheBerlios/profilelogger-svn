#ifndef PROFILE_CORRELATION_WIDGET_H
#define PROFILE_CORRELATION_WIDGET_H

#include <QWidget>

class QSplitter;

class Project;

class ProfileCorrelationItemModel;
class ProfileCorrelationItemView;

class BedCorrelationItemModel;
class BedCorrelationItemView;
class BedCorrelationView;

class ProfileCorrelationWidget: public QWidget {
  Q_OBJECT
    public:
  ProfileCorrelationWidget(QWidget* p);
  virtual ~ProfileCorrelationWidget();

  public slots:
  void slotCurrentProjectChanged(Project* p);

 private:
  Project* _project;

  QSplitter* _splitterW;
  ProfileCorrelationItemModel* _correlationsM;
  ProfileCorrelationItemView* _correlationsV;

  BedCorrelationItemModel* _bedCorrelationsM;
  BedCorrelationItemView* _bedCorrelationsV;

  BedCorrelationView* _graphicsV;
};

#endif
