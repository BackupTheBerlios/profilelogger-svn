/* 
 * File:   StandardItemModel.h
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 20:07
 */

#ifndef _STANDARDITEMMODEL_H
#define	_STANDARDITEMMODEL_H

#include <QStandardItemModel>

class QWidget;

class DataManager;
class Postgres;
class ProfileLoggerDatabase;

class StandardItemModel : public QStandardItemModel {
    Q_OBJECT

public:
    StandardItemModel(QObject* p = 0);
    virtual ~StandardItemModel();

    void setDataManager(DataManager* m) {
      _dataManager = m;
    }

    DataManager* getDataManager() {
      return _dataManager;
    }

    Postgres* getPostgres() {
      return _postgres;
    }

    ProfileLoggerDatabase* getProfileLoggerDatabase() {
      return _profileLoggerDatabase;
    }

    QWidget* getDialogParent();

    void begin();
    void commit();
    void rollback();

signals:
    void reloaded();

 private:    
    DataManager* _dataManager;
    Postgres* _postgres;
    ProfileLoggerDatabase* _profileLoggerDatabase;
};

#endif	/* _STANDARDITEMMODEL_H */

