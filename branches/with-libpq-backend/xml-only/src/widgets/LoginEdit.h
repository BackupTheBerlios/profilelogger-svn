#ifndef LOGIN_EDIT_H
#define LOGIN_EDIT_H

#include <QLineEdit>

class LoginEdit: public QLineEdit {
  Q_OBJECT
    public:
  LoginEdit(QWidget* p = 0);
  virtual ~LoginEdit() {}
};

#endif
