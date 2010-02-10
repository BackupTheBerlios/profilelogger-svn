#ifndef HOST_EDIT_H
#define HOST_EDIT_H

#include <QLineEdit>

class HostEdit: public QLineEdit {
  Q_OBJECT
    public:
  HostEdit(QWidget* p = 0);
  virtual ~HostEdit() {}
};

#endif
