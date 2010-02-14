#ifndef DBWORKWIDGET_H
#define DBWORKWIDGET_H

#include <QWidget>

class ProjectItemModel;
class ProjectView;

class DbWorkWidget: public QWidget {
  Q_OBJECT
    public:
  DbWorkWidget(QWidget* p);
  virtual ~DbWorkWidget() {}

  public slots:
  void slotDatabaseConnected(const QString& n);
  void slotDatabaseLost();
  void slotDatabaseClosed();

 private:
  ProjectItemModel* _projectsM;
  ProjectView* _projectsV;
};

#endif
