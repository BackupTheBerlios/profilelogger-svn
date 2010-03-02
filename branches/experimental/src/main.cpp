#include "App/ProfileLogger.h"
#include "Gui/MainWindow.h"
#include "DataModel/Dataset.h"

int main(int argc, char** argv) {
  ProfileLogger a(argc, argv);
  MainWindow w;
  Dataset d(0, 1);
  w.show();
  a.connect(&a, SIGNAL(lastWindowClosed()), &a, SLOT(quit()));
  return a.exec();
}
