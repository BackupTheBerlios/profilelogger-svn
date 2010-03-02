#ifndef PASSWORD_EDIT_H
#define PASSWORD_EDIT_H

#include <QLineEdit>

class PasswordEdit: public QLineEdit {
  Q_OBJECT
    public:
  PasswordEdit(QWidget* p = 0);
  virtual ~PasswordEdit() {}
};

#endif
