/* 
 * File:   MainWindow.h
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 19:33
 */

#ifndef _MAINWINDOW_H
#define	_MAINWINDOW_H

#include <QMainWindow>

class QMenu;
class QTabWidget;
class QLabel;

class WorkWidget;
class ProfileCorrelationWidget;

class MainWindow: public QMainWindow {
    Q_OBJECT
public:
    MainWindow();
    virtual ~MainWindow();

    public slots:
    void slotDatabaseConnectionEstablished(const QString& s);
    void slotDatabaseConnectionLost();
    void slotDatabaseConnectionClosed();

private:
    void setupStatusBar();

    QMenu* _fileM;
    QMenu* _projectM;
    QMenu* _helpM;

    QTabWidget* _centralW;
    WorkWidget* _workW;
    ProfileCorrelationWidget* _correlationW;

    QLabel* _dbStatusW;
};

#endif	/* _MAINWINDOW_H */

