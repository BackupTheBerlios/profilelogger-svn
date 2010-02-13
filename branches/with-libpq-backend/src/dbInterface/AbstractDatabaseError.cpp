#include "AbstractDatabaseError.h"

AbstractDatabaseError::AbstractDatabaseError(const QString& msg)
  : _msg(msg)
{}

QString AbstractDatabaseError::text() const {
  return _msg;
}
