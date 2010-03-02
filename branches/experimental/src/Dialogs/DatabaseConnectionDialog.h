#ifndef DATABASE_CONNECTION_DIALOG_H
#define DATABASE_CONNECTION_DIALOG_H

#include <QDialog>

#include "../Postgres/PostgresConnectionSettings.h"

class QLineEdit;
class QSpinBox;
class QCheckBox;
class QDialogButtonBox;
class QGroupBox;

class FieldLabel;
class HostEdit;
class LoginEdit;
class PasswordEdit;

class DatabaseConnectionDialog: public QDialog {
    Q_OBJECT
	public:
    DatabaseConnectionDialog(QWidget* p,
			     const PostgresConnectionSettings& s);
    virtual ~DatabaseConnectionDialog();

    QString getPassword() const {
	return _pass;
    }

    public slots:
    void accept();
    void slotHostChanged(const QString& s);
    void slotPortChanged(int p);
    void slotDatabaseChanged(const QString& s);
    void slotUserChanged(const QString& s);
    void slotPasswordChanged(const QString& s);
    void slotDropSchemaToggled(bool b);
    void slotCreateSchemaToggled(bool b);
    void slotInsertTemplateDataToggled(bool b);

    PostgresConnectionSettings getPostgresConnectionSettings() const {
	return _s;
    }

private:
    HostEdit* _hostW;
    QSpinBox* _portsW;
    QLineEdit* _dbW;
    LoginEdit* _userW;
    PasswordEdit* _passW;
    QCheckBox* _dropSchemaW;
    QCheckBox* _createSchemaW;
    QCheckBox* _insertTemplateDataW;
    QDialogButtonBox* _bb;

    PostgresConnectionSettings _s;
    QString _pass;
};

#endif
