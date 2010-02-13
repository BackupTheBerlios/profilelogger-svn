#include "AbstractDatabaseError.h"

AbstractDatabaseError::AbstractDatabaseError(const QString& dbMsg)
  : std::exception(),
    _dbMsg(dbMsg)
{}

AbstractDatabaseError::~AbstractDatabaseError() throw()
{}
