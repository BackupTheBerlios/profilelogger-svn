#include "PostgresConnectionSettings.h"

PostgresConnectionSettings::PostgresConnectionSettings(const QString& host,
						       const int port,
						       const QString& database,
						       const QString& login,
						       const QString& password,
						       const bool dropSchema,
						       const bool createSchema,
						       const bool insertTemplateData)
    : _host(host),
      _port(port),
      _database(database),
      _login(login),
      _password(password),
      _dropSchema(dropSchema),
      _createSchema(createSchema),
      _insertTemplateData(insertTemplateData)
{
}

PostgresConnectionSettings::~PostgresConnectionSettings()
{
}

void PostgresConnectionSettings::setHost(const QString& h) 
{
    _host = h;
}

void PostgresConnectionSettings::setPort(int p) 
{
    _port = p;
}

void PostgresConnectionSettings::setDatabase(const QString& d)
{
    _database = d;
}

void PostgresConnectionSettings::setLogin(const QString& l)
{
    _login = l;
}

void PostgresConnectionSettings::setPassword(const QString& p) 
{
    _password = p;
}

void PostgresConnectionSettings::setDropSchema(const bool b) 
{
    _dropSchema = b;
}

void PostgresConnectionSettings::setCreateSchema(const bool b)
{
    _createSchema = b;
}

void PostgresConnectionSettings::setInsertTemplateData(const bool b)
{
    _insertTemplateData = b;
}

QString PostgresConnectionSettings::getHost() const 
{
    return _host;
}

int PostgresConnectionSettings::getPort() const 
{
    return _port;
}

QString PostgresConnectionSettings::getDatabase() const
{
    return _database;
}

QString PostgresConnectionSettings::getLogin() const 
{
    return _login;
}

QString PostgresConnectionSettings::getPassword() const 
{
    return _password;
}

QString PostgresConnectionSettings::makeConnectionString() const 
{
    return QString("hostaddr = '%1' port = '%2' dbname = '%3' user = '%4' password = '%5' connect_timeout = '10'")
	.arg(getHost())
	.arg(getPort())
	.arg(getDatabase())
	.arg(getLogin())
	.arg(getPassword());
}

bool PostgresConnectionSettings::getDropSchema() const 
{
    return _dropSchema;
}

bool PostgresConnectionSettings::getCreateSchema() const 
{
    return _createSchema;
}

bool PostgresConnectionSettings::getInsertTemplateData() const 
{
    return _insertTemplateData;
}
