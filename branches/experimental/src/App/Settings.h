#ifndef SETTINGS_H
#define SETTINGS_H

#include "../Postgres/PostgresConnectionSettings.h"

class Settings {
public: 
    Settings();
    virtual ~Settings();

    void save(const PostgresConnectionSettings& s);
    PostgresConnectionSettings getDatabaseConnectionSettings() const;
};

#endif
