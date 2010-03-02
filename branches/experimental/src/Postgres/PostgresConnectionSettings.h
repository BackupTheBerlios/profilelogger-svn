#ifndef POSTGRES_CONNECTION_SETTINGS_H
#define POSTGRES_CONNECTION_SETTINGS_H

#include <QString>

class PostgresConnectionSettings 
{
public:
    PostgresConnectionSettings(const QString& host = "localhost",
			       const int port = 5432,
			       const QString& database = "profilelogger",
			       const QString& login = "jolo",
			       const QString& password = "",
			       const bool dropSchema = false,
			       const bool createSchema = false,
			       const bool insertTemplateData = false);
    virtual ~PostgresConnectionSettings();
    
    void setHost(const QString& n);
    void setPort(int p);
    void setDatabase(const QString& n);
    void setLogin(const QString& n);
    void setPassword(const QString& n);
    void setDropSchema(const bool b);
    void setCreateSchema(const bool b);
    void setInsertTemplateData(const bool b);
    
    QString getHost() const;
    int getPort() const;
    QString getDatabase() const;
    QString getLogin() const;
    QString getPassword() const;
    bool getDropSchema() const;
    bool getCreateSchema() const;
    bool getInsertTemplateData() const;
    
    QString makeConnectionString() const;
    
private:
    QString _host;
    int _port;
    QString _database;
    QString _login;
    QString _password;
    bool _dropSchema;
    bool _createSchema;
    bool _insertTemplateData;
};
#endif
