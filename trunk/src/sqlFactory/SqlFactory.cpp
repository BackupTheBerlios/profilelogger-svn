#include "SqlFactory.h"

#include "Database.h"
#include "Schema.h"
#include "Sequence.h"
#include "Table.h"
#include "UniqueConstraint.h"
#include "TextNotEmptyCheckConstraint.h"
#include "PrimaryKey.h"
#include "TableColumn.h"
#include "ForeignKey.h"

SqlFactory::SqlFactory(QObject* p)
  : QObject(p)
{}

SqlFactory::~SqlFactory()
{}

QString SqlFactory::quoteIdentifier(const QString& s) {
  return s;
}

QStringList SqlFactory::make(Database* db) {
  QStringList ret;
  ret << QString("CREATE DATABASE %1").arg(quoteIdentifier(db->getQualifiedName()));
  return ret;
}

QStringList SqlFactory::make(Schema* s) {
  QStringList ret;
  ret << QString("CREATE SCHEMA %1").arg(quoteIdentifier(s->getQualifiedName()));
  return ret;
}

QStringList SqlFactory::drop(Schema* s) {
  QStringList ret;
  ret << QString("DROP SCHEMA %1 CASCADE").arg(quoteIdentifier(s->getQualifiedName()));
  return ret;
}

QStringList SqlFactory::make(Sequence* s) {
  QStringList ret;
  ret << QString("CREATE SEQUENCE %1").arg(quoteIdentifier(s->getQualifiedName()));
  return ret;
}

QStringList SqlFactory::make(Table* t) {
  QStringList ret;
  ret << QString("CREATE TABLE %1()").arg(quoteIdentifier(t->getQualifiedName()));

  for (QList<TableColumn*>::iterator it = t->getFirstTableColumn(); it != t->getLastTableColumn(); it++) {
    TableColumn* c = *it;

    if (c) {
      QString typeName = "ERROR_TYPE_NAME_NOT_SET_IN_CODE";
      switch(c->getDataType()) {
      case(Database::DataTypeInt): typeName = "INTEGER"; break;
      case(Database::DataTypeText): typeName = "TEXT"; break;
      case(Database::DataTypeDouble): typeName = "DOUBLE"; break;
      case(Database::DataTypeBool): typeName = "BOOLEAN"; break;
      default: break;
      };

      ret << QString("ALTER TABLE %1 ADD COLUMN %2 %3")
	.arg(quoteIdentifier(c->getTable()->getQualifiedName()))
	.arg(quoteIdentifier(c->getName()))
	.arg(typeName);
    }
  }
  return ret;
}

QStringList SqlFactory::make(UniqueConstraint* u) {
  QStringList ret;
  QStringList cols;
  for (QList<TableColumn*>::iterator it = u->getFirstColumn(); it != u->getLastColumn(); it++) {
    cols << quoteIdentifier((*it)->getName());
  }

  ret << QString("ALTER TABLE %1 ADD CONSTRAINT %2 UNIQUE(%3)")
    .arg(quoteIdentifier(u->getTable()->getQualifiedName()))
    .arg(quoteIdentifier(u->getName()))
    .arg(cols.join(", "));

  return ret;
}

QStringList SqlFactory::make(TextNotEmptyCheckConstraint* c) {
  QStringList ret;
  QStringList expr;
  for (QList<TableColumn*>::iterator it = c->getFirstColumn(); it != c->getLastColumn(); it++) {
    TableColumn* col = *it;
    expr << QString("%1 <> ''").arg(quoteIdentifier(col->getName()))
	 << QString("%1 IS NOT NULL").arg(quoteIdentifier(col->getName()));
  }

  ret << QString("ALTER TABLE %1 ADD CONSTRAINT %2 CHECK(%3)")
    .arg(quoteIdentifier(c->getTable()->getQualifiedName()))
    .arg(quoteIdentifier(c->getName()))
    .arg(expr.join(" AND "));

  return ret;
}

QStringList SqlFactory::make(PrimaryKey* p) {
  QStringList ret;
  QStringList cols;
  for (QList<TableColumn*>::iterator it = p->getFirstColumn(); it != p->getLastColumn(); it++) {
    cols << quoteIdentifier((*it)->getName());
  }

  ret << QString("ALTER TABLE %1 ADD CONSTRAINT %2 PRIMARY KEY(%3)")
    .arg(quoteIdentifier(p->getTable()->getQualifiedName()))
    .arg(quoteIdentifier(p->getName()))
    .arg(cols.join(", "));

  return ret;
}

QStringList SqlFactory::make(ForeignKey* f) {
  QStringList ret;
  ret << QString("ALTER TABLE %1 ADD CONSTRAINT %2 FOREIGN KEY (%3) REFERENCES %4 (%5)")
    .arg(quoteIdentifier(f->getTable()->getQualifiedName()))
    .arg(quoteIdentifier(f->getName()))
    .arg(quoteIdentifier(f->getLocalColumn()->getName()))
    .arg(quoteIdentifier(f->getReferencedColumn()->getTable()->getQualifiedName()))
    .arg(quoteIdentifier(f->getReferencedColumn()->getName()));
  return ret;
}

QString SqlFactory::makeDefaultFromSequence(TableColumn* c) {
  if (!c->hasSequence()) {
    return tr("-- column %1 has no sequence").arg(c->getQualifiedName());
  }

  return QString("ALTER TABLE %1 ALTER COLUMN %2 SET DEFAULT nextval('%3')")
    .arg(c->getTable()->getQualifiedName())
    .arg(c->getName())
    .arg(c->getSequence()->getQualifiedName());
}

QString SqlFactory::makeDefaultText(TableColumn* c) {
  return QString("ALTER TABLE %1 ALTER COLUMN %2 SET DEFAULT '%3'")
    .arg(c->getTable()->getQualifiedName())
    .arg(c->getName())
    .arg(c->getDefaultText());
}

QString SqlFactory::makeDefaultInt(TableColumn* c) {
  return QString("ALTER TABLE %1 ALTER COLUMN %2 SET DEFAULT %3")
    .arg(c->getTable()->getQualifiedName())
    .arg(c->getName())
    .arg(c->getDefaultInt());
}

QString SqlFactory::makeDefaultDouble(TableColumn* c) {
  return QString("ALTER TABLE %1 ALTER COLUMN %2 SET DEFAULT %3")
    .arg(c->getTable()->getQualifiedName())
    .arg(c->getName())
    .arg(c->getDefaultDouble());
}

QString SqlFactory::makeDefaultFromConstant(TableColumn* c) {
  QString k = tr("CONSTANT_MISSING_IN_SqlFactory::makeDefaultFromConstant");

  switch(c->getDefaultConstant()) {
  case(Database::CURRENT_DATE): k = "CURRENT_DATE"; break;
  case(Database::CURRENT_TIMESTAMP): k = "CURRENT_TIMESTAMP"; break;
  case(Database::CURRENT_USER): k = "CURRENT_USER"; break;
  default: break;
  }

  return QString("ALTER TABLE %1 ALTER COLUMN %2 SET DEFAULT %3")
    .arg(c->getTable()->getQualifiedName())
    .arg(c->getName())
    .arg(k);
}

QString SqlFactory::makeSelectAll(Table* t,
				  QList<TableColumn*> order) {
  QStringList cols;
  QStringList o;

  for (QList<TableColumn*>::iterator it = t->getFirstTableColumn();
       it != t->getLastTableColumn();
       it++) {
    cols << (*it)->getName();
  }

  for (QList<TableColumn*>::iterator it = order.begin();
       it != order.end();
       it++) {
    o << (*it)->getName();
  }

  if (cols.size() < 0) {
    return QString("SELECT %1 FROM %2")
      .arg(cols.join(", "))
      .arg(t->getQualifiedName());
  } else {
    return QString("SELECT %1 FROM %2 ORDER BY %3")
      .arg(cols.join(", "))
      .arg(t->getQualifiedName());
  }
}

QString SqlFactory::makeDelete(Table* t, 
			       TableColumn* idCol, 
			       const QString& idPlaceholder) {
  return QString("DELETE FROM %1 WHERE %2 = %3")
    .arg(t->getQualifiedName())
    .arg(idCol->getName())
    .arg(idPlaceholder);
}

QString SqlFactory::makeInsert(Table* t, 
			       QList<TableColumn*> cols, 
			       QStringList placeholders) {
  QStringList c;

  for (QList<TableColumn*>::iterator it = cols.begin();
       it != cols.end();
       it++) {
    c << (*it)->getName();
  }

  return QString("INSERT INTO %1(%2) VALUES(%3)")
    .arg(t->getQualifiedName())
    .arg(c.join(", "))
    .arg(placeholders.join(", "));
}

QString SqlFactory::makeUpdate(Table* t, 
			       QList<TableColumn*> valueCols, 
			       QList<QString> valuePlaceholders, 
			       TableColumn* idCol,
			       const QString& idPlaceholder) {
  QStringList kv;

  for (int i = 0; i < valueCols.size(); i++) {
    kv << QString ("%1 = %2")
      .arg(valueCols.at(i)->getName())
      .arg(valuePlaceholders.at(i));
  }

  return QString("UPDATE %1 SET %2 WHERE %3 = %4")
    .arg(t->getQualifiedName())
    .arg(kv.join(", "))
    .arg(idCol->getName())
    .arg(idPlaceholder);
}

