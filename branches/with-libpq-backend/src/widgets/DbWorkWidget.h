#ifndef DBWORKWIDGET_H
#define DBWORKWIDGET_H

#include <QWidget>

class ProjectItemModel;
class ProjectView;

class ProfileItemModel;
class ProfileItemView;
class ManagementToolBox;

class QSplitter;

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
  QSplitter* _splW;

  ProjectItemModel* _projectsM;
  ProjectView* _projectsV;

  ProfileItemModel* _profilesM;
  ProfileItemView* _profilesV;

  ManagementToolBox* _tbW;
};

#endif
