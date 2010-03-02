#include "Settings.h"

#include <QSettings>

#include "../Postgres/PostgresConnectionSettings.h"

Settings::Settings()
{
}

Settings::~Settings()
{}

void Settings::save(const PostgresConnectionSettings& x) 
{
    QSettings s;
    s.setValue("DatabaseConnection/Host", x.getHost());
    s.setValue("DatabaseConnection/Port", x.getPort());
    s.setValue("DatabaseConnection/Database", x.getDatabase());
    s.setValue("DatabaseConnection/User", x.getLogin());
    s.setValue("DatabaseConnection/DropSchema", QVariant(x.getDropSchema()).toInt());
    s.setValue("DatabaseConnection/CreateSchema", QVariant(x.getCreateSchema()).toInt());
    s.setValue("DatabaseConnection/InsertTemplateData", QVariant(x.getInsertTemplateData()).toInt());
}

PostgresConnectionSettings Settings::getDatabaseConnectionSettings() const
{
    QSettings s;
    return PostgresConnectionSettings(s.value("DatabaseConnection/Host").toString(),
				      s.value("DatabaseConnection/Port").toInt(),
				      s.value("DatabaseConnection/Database").toString(),
				      s.value("DatabaseConnection/User").toString(),
				      QString::null,
				      (bool)(s.value("DatabaseConnection/DropSchema").toInt()),
				      (bool)(s.value("DatabaseConnection/CreateSchema").toInt()),
				      (bool)(s.value("DatabaseConnection/InsertTemplateData").toInt()));
}

