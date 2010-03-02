#ifndef PROFILELOGGER_H
#define PROFILELOGGER_H

#include <QApplication>

#include "Settings.h"

#include <QMap>
#include <QAction>
#include <QMap>

class PostgresConnection;
class Database;

class ProfileLogger: public QApplication {
    Q_OBJECT
	public:
    ProfileLogger(int& argc, char** argv);
    virtual ~ProfileLogger();

    Settings* getSettings() {
	return &_settings;
    }

    QList<QAction*> getFileActions();
    QList<QAction*>getDatabaseActions();

    PostgresConnection* getDatabaseConnection() const;
    
    public slots:
    void slotPreferences();
    void slotOpenDatabase();
    void slotCloseDatabase();
  
private:
    void rollbackOrExit();
    
    void dropSchema();
    void createSchema();
    void insertTemplateData();
    
    void setupActions();
    void setupDatabaseModel();
    
    Settings _settings;
    QMap<QString, QAction*> _actions;

    PostgresConnection* _pgConn;
    Database* _db;
};

#endif
