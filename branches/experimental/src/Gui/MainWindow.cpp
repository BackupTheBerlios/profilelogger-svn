#include "MainWindow.h"

#include "../App/ProfileLogger.h"
#include "../Postgres/PostgresConnection.h"

#include <QtGui/QMenu>
#include <QtGui/QMenuBar>
#include <QtGui/QToolBar>
#include <QtGui/QAction>
#include <QtGui/QLabel>
#include <QtGui/QStatusBar>

MainWindow::MainWindow(QWidget* p)
    : QMainWindow(p)
{
    setupGui();
}

MainWindow::~MainWindow() {}

void MainWindow::setupGui() {
    setupStatusBar();
    setupMenuBar();
    setupToolBar();
}

void MainWindow::setupStatusBar() {
    _dbStatusW = new QLabel(tr("Database Status"), statusBar());
    statusBar()->addPermanentWidget(_dbStatusW);

    connect(getProfileLogger()->getDatabaseConnection(),
	    SIGNAL(connectionEstablished(const QString&)),
	    this,
	    SLOT(slotDatabaseConnectionEstablished(const QString&)));
    connect(getProfileLogger()->getDatabaseConnection(),
	    SIGNAL(connectionClosed()),
	    this,
	    SLOT(slotDatabaseConnectionClosed()));
}

void MainWindow::setupMenuBar() {
    QMenu* fM = new QMenu(tr("&File"), menuBar());
    QMenu* dbM = new QMenu(tr("&Database"), menuBar());

    addActionsToMenu(getProfileLogger()->getFileActions(), fM);
    addActionsToMenu(getProfileLogger()->getDatabaseActions(), dbM);
  
    menuBar()->addMenu(fM);
    menuBar()->addMenu(dbM);
}

void MainWindow::addActionsToMenu(QList<QAction*> actions, QMenu* menu) 
{  
    for (QList<QAction*>::iterator it = actions.begin(); it != actions.end(); it++) {
	menu->addAction(*it);
    }
}

void MainWindow::setupToolBar() {
}

ProfileLogger* MainWindow::getProfileLogger() {
    return static_cast<ProfileLogger*>(QApplication::instance());
}

void MainWindow::slotDatabaseConnectionEstablished(const QString& m) 
{
    _dbStatusW->setText(tr("Connected: %1").arg(m));
}

void MainWindow::slotDatabaseConnectionClosed()
{
    _dbStatusW->setText(tr("Not Connected To Database"));
}
