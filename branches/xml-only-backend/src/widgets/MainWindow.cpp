/* 
 * File:   MainWindow.cpp
 * Author: jolo
 * 
 * Created on 10. Dezember 2009, 19:33
 */

#include "MainWindow.h"

#include <QMenu>
#include <QAction>
#include <QApplication>
#include <QMenuBar>
#include <QApplication>
#include <QTabWidget>
#include <QDebug>
#include <QStatusBar>
#include <QLabel>

#include "ProfileLogger.h"

#include "WorkWidget.h"
#include "ProfileCorrelationWidget.h"

MainWindow::MainWindow()
  : QMainWindow() {
  setupStatusBar();
  _fileM = new QMenu(tr("&File"), this);
  _projectM = new QMenu(tr("&Project"), this);
  _helpM = new QMenu(tr("&Help"), this);

  _centralW = new QTabWidget(this);

  setCentralWidget(_centralW);

  _fileM->addAction((static_cast<ProfileLogger*> (QApplication::instance()))->getSettingsAction());
  _fileM->addAction((static_cast<ProfileLogger*> (QApplication::instance()))->getQuitAction());

  _projectM->addAction((static_cast<ProfileLogger*> (QApplication::instance()))->getNewProjectAction());
  _projectM->addAction((static_cast<ProfileLogger*> (QApplication::instance()))->getSaveProjectAction());
  _projectM->addAction((static_cast<ProfileLogger*> (QApplication::instance()))->getSaveProjectAsAction());
  _projectM->addAction((static_cast<ProfileLogger*> (QApplication::instance()))->getOpenProjectAction());
  _projectM->addAction((static_cast<ProfileLogger*> (QApplication::instance()))->getOpenLastProjectAction());

  _helpM->addAction((static_cast<ProfileLogger*> (QApplication::instance()))->getAboutAction());
  _helpM->addAction((static_cast<ProfileLogger*> (QApplication::instance()))->getAboutQtAction());

  menuBar()->addMenu(_fileM);
  menuBar()->addMenu(_projectM);
  menuBar()->addMenu(_helpM);

  _workW = new WorkWidget(centralWidget());
  _correlationW = new ProfileCorrelationWidget(centralWidget());

  (static_cast<QTabWidget*>(centralWidget()))->addTab(_workW, tr("Profile Management"));
  (static_cast<QTabWidget*>(centralWidget()))->addTab(_correlationW, tr("Profile Correlation"));
}

MainWindow::~MainWindow() {
}

void MainWindow::slotDatabaseConnectionEstablished(const QString& s) {
  qDebug() << "bin da: " << s;
  _centralW->setEnabled(true);
  _dbStatusW->setText(tr("Online: %1").arg(s));
}

void MainWindow::slotDatabaseConnectionLost() {
  _centralW->setEnabled(false);
  _dbStatusW->setText("Database Connection Lost.");
}

void MainWindow::slotDatabaseConnectionClosed() {
  _centralW->setEnabled(false);
  _dbStatusW->setText("Not Connected To Any Database.");
}

void MainWindow::setupStatusBar() {
  _dbStatusW = new QLabel(tr("Database Connection Status"), statusBar());
  statusBar()->addWidget(_dbStatusW);
}
