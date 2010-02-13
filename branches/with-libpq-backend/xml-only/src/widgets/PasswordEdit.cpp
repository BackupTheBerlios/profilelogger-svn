#include "PasswordEdit.h"

PasswordEdit::PasswordEdit(QWidget *p)
  : QLineEdit(p)
{
  setEchoMode(QLineEdit::Password);
}
