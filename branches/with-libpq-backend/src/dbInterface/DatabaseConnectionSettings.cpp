#include "DatabaseConnectionSettings.h"

DatabaseConnectionSettings::DatabaseConnectionSettings(const QString& host,
						       int port,
						       const QString& db,
						       const QString& user,
						       const QString& pass,
						       bool drop,
						       bool create,
						       bool insertTemplateData)
  : _host(host),
    _port(port),
    _db(db),
    _user(user),
    _pass(pass),
    _drop(drop),
    _create(create),
    _insertTemplateData(insertTemplateData)
{}

QString DatabaseConnectionSettings::makeConnectionString() const {
  return QString("QPSQL://%1@%2:%3/%4")
    .arg(getUser())
    .arg(getHost())
    .arg(getPort())
    .arg(getDatabase());
}

