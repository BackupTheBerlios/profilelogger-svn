#ifndef DATABASECONNECTIONSETTINGS_H
#define DATABASECONNECTIONSETTINGS_H

#include <QString>

class DatabaseConnectionSettings {
 public:
  DatabaseConnectionSettings(const QString& host = "localhost",
			     int port = 5432,
			     const QString& dbName = "profilelogger",
			     const QString& user = "jolo",
			     const QString& pass = QString::null,
			     bool dropSchema = false,
			     bool createSchema = false,
			     bool insertTemplateData = false);
  virtual ~DatabaseConnectionSettings() {}

  void setHost(const QString& n) {
    _host = n;
  }

  void setPort(const int port) {
    _port = port;
  }

  void setDatabase(const QString& n) {
    _dbName = n;
  }

  void setUser(const QString& n) {
    _user = n;
  }

  void setPassword(const QString& n) {
    _pass = n;
  }

  void setDropSchema(const bool b) {
    _dropSchema = b;
  }

  void setCreateSchema(const bool b) {
    _createSchema = b;
  }
  
  void setInsertTemplateData(const bool b) {
    _insertTemplateData = b;
  }

  QString getHost() const {
    return _host;
  }

  int getPort() const {
    return _port;
  }

  QString getDatabase() const {
    return _dbName;
  }
  
  QString getUser() const {
    return _user;
  }

  QString getPassword() const {
    return _pass;
  }

  bool getDropSchema() const {
    return _dropSchema;
  }

  bool getCreateSchema() const {
    return _createSchema;
  }

  bool getInsertTemplateData() const {
    return _insertTemplateData;
  }

  QString makeConnectionString() const;

 private:
  QString _host;
  int _port;
  QString _dbName;
  QString _user;
  QString _pass;
  bool _dropSchema;
  bool _createSchema;
  bool _insertTemplateData;
};

#endif
