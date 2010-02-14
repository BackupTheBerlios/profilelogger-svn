#include "DatabaseConnectionSettings.h"

DatabaseConnectionSettings::DatabaseConnectionSettings(const QString& host,
						       const int port,
						       const QString& database,
						       const QString& user,
						       const QString& pass,
						       const bool dropSchema,
						       const bool createSchema,
						       const bool insertTemplateData)
  : _host(host),
    _port(port),
    _dbName(database),
    _user(user),
    _pass(pass),
    _dropSchema(dropSchema),
    _createSchema(createSchema),
    _insertTemplateData(insertTemplateData)
{}

QString DatabaseConnectionSettings::makeConnectionString() const {
  return QString("hostaddr = '%1' port = '%2' dbname = '%3' user = '%4' password = '%5' connect_timeout = '10'")
    .arg(getHost())
    .arg(getPort())
    .arg(getDatabase())
    .arg(getUser())
    .arg(getPassword());
}

QString DatabaseConnectionSettings::makeInfoString() const {
  return QString("%1@%2:%3/%4")
    .arg(getUser())
    .arg(getHost())
    .arg(getPort())
    .arg(getDatabase());
}
