#include "ProfileLogger.h"

#include <QtGui/QMessageBox>

#include "../Postgres/PostgresConnection.h"
#include "../Postgres/PostgresConnectionSettings.h"
#include "../Dialogs/DatabaseConnectionDialog.h"
#include "../Dialogs/DatabaseErrorDialog.h"

#include "../DatabaseModel/Database.h"
#include "../DatabaseModel/Schema.h"
#include "../DatabaseModel/Sequence.h"
#include "../DatabaseModel/Table.h"
#include "../DatabaseModel/TableColumn.h"
#include "../DatabaseModel/PrimaryKey.h"
#include "../DatabaseModel/ForeignKey.h"

ProfileLogger::ProfileLogger(int& argc, char** argv)
    : QApplication(argc, argv),
      _pgConn(0),
      _db(0)
{
    QCoreApplication::setOrganizationName("Johannes Lochmann");
    QCoreApplication::setOrganizationDomain("profilelogger.berlios.de");
    QCoreApplication::setApplicationName("ProfileLogger");

    _pgConn = new PostgresConnection(this);
    _db = new Database(this, "ProfileLogger");

    setupActions();
    setupDatabaseModel();
}

ProfileLogger::~ProfileLogger()
{}

void ProfileLogger::setupActions() {
    _actions["quit"] = new QAction(tr("&Quit"), this);
    _actions["quit"]->setShortcut(QKeySequence("Ctrl+q"));
    connect(_actions["quit"], SIGNAL(activated()), this, SLOT(quit()));

    _actions["preferences"] = new QAction(tr("&Settings..."), this);
    connect(_actions["preferences"], SIGNAL(activated()), this, SLOT(slotPreferences()));

    _actions["open database"] = new QAction(tr("Open Database..."), this);
    _actions["open database"]->setShortcut(QKeySequence("Ctrl+o"));
    connect(_actions["open database"], SIGNAL(activated()), this, SLOT(slotOpenDatabase()));
  
    _actions["close database"] = new QAction(tr("Close Database..."), this);
    _actions["close database"]->setShortcut(QKeySequence("Ctrl+o"));
    connect(_actions["close database"], SIGNAL(activated()), this, SLOT(slotCloseDatabase()));
  
}

QList<QAction*> ProfileLogger::getFileActions() {
    QList<QAction*> ret;
    ret << _actions["quit"];
    ret << _actions["preferences"];
    return ret;
}

QList<QAction*> ProfileLogger::getDatabaseActions() {
    QList<QAction*> ret;
    ret << _actions["open database"];
    ret << _actions["close database"];
    return ret;
}

void ProfileLogger::slotPreferences() {
}

void ProfileLogger::slotOpenDatabase()
{
    Settings ss;

    DatabaseConnectionDialog* dlg = new DatabaseConnectionDialog(activeWindow(), 
								 ss.getDatabaseConnectionSettings());
    if (QDialog::Accepted != dlg->exec()) {
	return;
    }

    ss.save(dlg->getPostgresConnectionSettings());
    PostgresConnectionSettings tmp = ss.getDatabaseConnectionSettings();
    tmp.setPassword(dlg->getPassword());
    
    try {
	_pgConn->openDatabase(tmp);
    }
    catch(DatabaseError e) {
	DatabaseErrorDialog dlg(activeWindow(), e);
	dlg.exec();
    }

    if (tmp.getDropSchema()) {
	dropSchema();
    }
    
    if (tmp.getCreateSchema()) {
	createSchema();
    }

    if (tmp.getInsertTemplateData()) {
	insertTemplateData();
    }
}

void ProfileLogger::slotCloseDatabase()
{}

void ProfileLogger::dropSchema() 
{
    try {
	_pgConn->begin();
	_pgConn->dropSchema(_db);
	_pgConn->commit();
    }
    catch(DatabaseError e) {
	DatabaseErrorDialog dlg(activeWindow(), e);
	dlg.exec();

	rollbackOrExit();
    }
}

void ProfileLogger::createSchema()
{
    try {
	_pgConn->begin();
	_pgConn->createSchema(_db);
	_pgConn->commit();
    }
    catch(DatabaseError e) {
	DatabaseErrorDialog dlg(activeWindow(), e);
	dlg.exec();

	rollbackOrExit();
    }
}

void ProfileLogger::insertTemplateData()
{
}

PostgresConnection* ProfileLogger::getDatabaseConnection() const 
{
    return _pgConn;
}

void ProfileLogger::setupDatabaseModel()
{
    Schema* schema = _db->createSchema("data");
}

void ProfileLogger::rollbackOrExit()
{
    try {
	_pgConn->rollback();
    }
    catch(DatabaseError e2) {
	DatabaseErrorDialog dlg(activeWindow(), e2);
	dlg.exec();

	QMessageBox::critical(activeWindow(),
			      tr("Program will end."),
			      tr("Program will exit after not recoverable error."));
	    
	quit();
    }

}
