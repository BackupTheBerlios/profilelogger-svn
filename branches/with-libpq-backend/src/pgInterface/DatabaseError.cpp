#include "DatabaseError.h"

DatabaseError::DatabaseError(const QString& msg,
			     const QString& sql,
			     const QString& dbMsg)
  : AbstractDatabaseError(dbMsg),
    _sql(sql),
    _msg(msg)
{}

DatabaseError::~DatabaseError() throw()
{}
