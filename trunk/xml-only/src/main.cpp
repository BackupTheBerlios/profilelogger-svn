/*
 * File:   main.cpp
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 19:32
 */

#include <QApplication>

#include "ProfileLogger.h"
#include "MainWindow.h"

int main(int argc, char *argv[]) {
    ProfileLogger app(argc, argv);
    app.loadTranslation();

    QObject::connect(QApplication::instance(), SIGNAL(lastWindowClosed()), QApplication::instance(), SLOT(quit()));
    
    MainWindow* w = new MainWindow();
    w->show();

    app.setMainWindow(w);
    
    return app.exec();
}
