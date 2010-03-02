#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QtGui/QMainWindow>

class QLabel;

class ProfileLogger;

class MainWindow: public QMainWindow
{
    Q_OBJECT
	public:
    MainWindow(QWidget* p = 0);
    virtual ~MainWindow();

    public slots:
    void slotDatabaseConnectionEstablished(const QString& msg);
    void slotDatabaseConnectionClosed();
    
private:
    void addActionsToMenu(QList<QAction*> actions, QMenu* menu);
  
    ProfileLogger* getProfileLogger();

    void setupGui();
    void setupStatusBar();
    void setupMenuBar();
    void setupToolBar();

    QLabel* _dbStatusW;
};

#endif
