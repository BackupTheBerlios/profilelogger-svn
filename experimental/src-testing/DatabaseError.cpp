#include "DatabaseError.h"

DatabaseError::DatabaseError(const QString& msg,
			     const QString& sql,
			     const QString& dbMsg)
  : _msg(msg),
    _sql(sql),
    _dbMsg(dbMsg)
{}
