#include "DatabaseConnectionDialog.h"

#include <QLayout>
#include <QLineEdit>
#include <QSpinBox>
#include <QCheckBox>
#include <QDialogButtonBox>
#include <QGroupBox>
#include <QLabel>
#include <QApplication>

#include "HostEdit.h"
#include "LoginEdit.h"
#include "PasswordEdit.h"
#include "DatabaseConnectionSettings.h"
#include "Settings.h"
#include "ProfileLogger.h"

DatabaseConnectionDialog::DatabaseConnectionDialog(QWidget* p)
  : QDialog(p) {
  setLayout(new QVBoxLayout(this));
  QGroupBox* b = new QGroupBox(tr("Database Connection"), this);
  _bb = new QDialogButtonBox(QDialogButtonBox::Ok | QDialogButtonBox::Cancel,
			     Qt::Horizontal,
			     this);
  QGridLayout* bl = new QGridLayout(b);
  int r = 0;
  int lC = 0;
  int wC = 1;

  QLabel* hostL = new QLabel(tr("&Host"), b);
  _hostW = new HostEdit(b);
  hostL->setBuddy(_hostW);
  QLabel* portsL = new QLabel(tr("&Port"), b);
  _portsW = new QSpinBox(b);
  _portsW->setRange(1, 999999);
  portsL->setBuddy(_portsW);
  QLabel* dbL = new QLabel(tr("&Database"), b);
  _dbW = new QLineEdit(b);
  dbL->setBuddy(_dbW);
  QLabel* userL = new QLabel(tr("&User"), b);
  _userW = new LoginEdit(b);
  userL->setBuddy(_userW);
  QLabel* passL = new QLabel(tr("&Password"), b);
  _passW = new PasswordEdit(b);
  passL->setBuddy(_passW);
  _dropSchemaW = new QCheckBox(tr("Drop Schema"), b);
  _createSchemaW = new QCheckBox(tr("Create Schema"), b);
  _insertTemplateDataW = new QCheckBox(tr("Insert Template Data"), b);

  bl->addWidget(hostL, r, lC);
  bl->addWidget(_hostW, r, wC);
  r++;
  bl->addWidget(portsL, r, lC);
  bl->addWidget(_portsW, r, wC);
  r++;
  bl->addWidget(dbL, r, lC);
  bl->addWidget(_dbW, r, wC);
  r++;
  bl->addWidget(userL, r, lC);
  bl->addWidget(_userW, r, wC);
  r++;
  bl->addWidget(passL, r, lC);
  bl->addWidget(_passW, r, wC);
  r++;
  bl->addWidget(_dropSchemaW, r, wC);
  r++;
  bl->addWidget(_createSchemaW, r, wC);
  r++;
  bl->addWidget(_insertTemplateDataW, r, wC);

  layout()->addWidget(b);
  layout()->addWidget(_bb);

  connect(_hostW, SIGNAL(textChanged(const QString&)), this, SLOT(slotHostChanged(const QString&)));
  connect(_portsW, SIGNAL(valueChanged(int)), this, SLOT(slotPortChanged(int)));
  connect(_dbW, SIGNAL(textChanged(const QString&)), this, SLOT(slotDatabaseChanged(const QString&)));
  connect(_userW, SIGNAL(textChanged(const QString&)), this, SLOT(slotUserChanged(const QString&)));
  connect(_passW, SIGNAL(textChanged(const QString&)), this, SLOT(slotPasswordChanged(const QString&)));
  connect(_dropSchemaW, SIGNAL(toggled(bool)), this, SLOT(slotDropSchemaToggled(bool)));
  connect(_createSchemaW, SIGNAL(toggled(bool)), this, SLOT(slotCreateSchemaToggled(bool)));
  connect(_insertTemplateDataW, SIGNAL(toggled(bool)), this, SLOT(slotInsertTemplateDataToggled(bool)));
  connect(_bb, SIGNAL(accepted()), this, SLOT(accept()));
  connect(_bb, SIGNAL(rejected()), this, SLOT(reject()));

  _s = (static_cast<ProfileLogger*>(QApplication::instance()))->getSettings()->getDatabaseConnectionSettings();
  _hostW->setText(_s.getHost());
  _portsW->setValue(_s.getPort());
  _dbW->setText(_s.getDatabase());
  _userW->setText(_s.getUser());
  _passW->clear();
  if (_s.getDropSchema()) {
    _dropSchemaW->setCheckState(Qt::Checked);
  }
  if (_s.getCreateSchema()) {
    _createSchemaW->setCheckState(Qt::Checked);
  }
  if (_s.getInsertTemplateData()) {
    _insertTemplateDataW->setCheckState(Qt::Checked);
  }
}

void DatabaseConnectionDialog::slotHostChanged(const QString& s) {
  _s.setHost(s);
}

void DatabaseConnectionDialog::slotPortChanged(int p) {
  _s.setPort(p);
}

void DatabaseConnectionDialog::slotDatabaseChanged(const QString& s) {
  _s.setDatabase(s);
}

void DatabaseConnectionDialog::slotUserChanged(const QString& s) {
  _s.setUser(s);
}

void DatabaseConnectionDialog::slotPasswordChanged(const QString& s) {
  _s.setPassword(s);
  _pass = s;
}

void DatabaseConnectionDialog::slotDropSchemaToggled(bool b) {
  _s.setDropSchema(b);
}

void DatabaseConnectionDialog::slotCreateSchemaToggled(bool b) {
  _s.setCreateSchema(b);
}

void DatabaseConnectionDialog::slotInsertTemplateDataToggled(bool b) {
  _s.setInsertTemplateData(b);
}

DatabaseConnectionDialog::~DatabaseConnectionDialog() {
}

void DatabaseConnectionDialog::accept() {
  (static_cast<ProfileLogger*>(QApplication::instance()))->getSettings()->setDatabaseConnectionSettings(_s);
  done(QDialog::Accepted);
}
