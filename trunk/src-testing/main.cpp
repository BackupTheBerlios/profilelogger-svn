#include <QApplication>
#include <QDebug>

#include "Postgres.h"

#include "DatabaseError.h"

int main(int argc, char** argv) {
  Postgres pg(0);
  try {
    pg.connect();
    pg.begin();
    pg.declareCursor("databases", "select * from pg_database");
    PGresult* res = pg.fetchAllInCursor("databases");
    
    for (int r = 0; r < pg.getRowCount(res); r++) {
      qDebug() << "ROW: " << r;
      QMap<QString, QVariant> row = pg.getRow(res, r);
      for (QMap<QString, QVariant>::iterator it = row.begin(); it != row.end(); it++) {
	qDebug() << QString("%1: %2").arg(it.key()).arg(it.value().toString());
      }
    }
    pg.closeCursor("databases");
    pg.clearResult(res);
    pg.commit();
    pg.close();
  } catch(DatabaseError e) {
    qDebug() << e.text();
    pg.close();
    exit(1);
  }

  exit(0);
};
