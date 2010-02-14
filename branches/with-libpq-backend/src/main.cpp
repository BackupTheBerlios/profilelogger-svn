/*
 * File:   main.cpp
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 19:32
 */

#include <QApplication>

#include "ProfileLogger.h"
#include "MainWindow.h"

#include "DatabaseError.h"
#include "DatabaseErrorDialog.h"

int main(int argc, char *argv[]) {
  try {
    ProfileLogger app(argc, argv);
    app.loadTranslation();

    QObject::connect(QApplication::instance(), SIGNAL(lastWindowClosed()), QApplication::instance(), SLOT(quit()));
    
    MainWindow* w = new MainWindow();
    w->show();

    app.setMainWindow(w);
    
    return app.exec();
  } catch(DatabaseError e) {
    DatabaseErrorDialog dlg(0, e);
    dlg.exec();

    exit(-1);
  }
}
