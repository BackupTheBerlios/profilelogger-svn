#ifndef DATABASE_CONNECTION_SETTINGS_H
#define DATABASE_CONNECTION_SETTINGS_H

#include <QString>

class DatabaseConnectionSettings {
 public:
  DatabaseConnectionSettings(const QString& host = "localhost",
			     int port = 5432,
			     const QString& db = "profilelogger",
			     const QString& user = "jolo",
			     const QString& pass = QString::null,
			     bool drop = false,
			     bool create = false,
			     bool insertTemplateData = false);
  virtual ~DatabaseConnectionSettings() {}

  void setHost(const QString& h) {
    _host = h;
  }
  
  void setPort(int p) {
    _port = p;
  }

  void setDatabase(const QString& d) {
    _db = d;
  }

  void setUser(const QString& s) {
    _user = s;
  }

  void setPassword(const QString& p) {
    _pass = p;
  }

  void setDropSchema(bool b) {
    _drop = b;
  }
  
  void setCreateSchema(bool b) {
    _create = b;
  }

  void setInsertTemplateData(bool b) {
    _insertTemplateData = b;
  }

  QString getHost() const {
    return _host;
  }
  
  int getPort() const {
    return _port;
  }

  QString getDatabase() const {
    return _db;
  }

  QString getUser() const {
    return _user;
  }

  QString getPassword() const {
    return _pass;
  }

  bool getDropSchema() const {
    return _drop;
  }

  bool getCreateSchema() const {
    return _create;
  }

  bool getInsertTemplateData() const {
    return _insertTemplateData;
  }

  QString makeConnectionString() const;

 private:
  QString _host;
  int _port;
  QString _db;
  QString _user;
  QString _pass;
  bool _drop;
  bool _create;
  bool _insertTemplateData;
};

#endif
