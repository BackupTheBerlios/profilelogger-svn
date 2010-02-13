#include "DbInterfacePart.h"

#include <QStringList>

DbInterfacePart::DbInterfacePart(QObject* p,
				 const QString& n)
  : QObject(p),
    _name(n) 
{
}

DbInterfacePart::~DbInterfacePart()
{}
