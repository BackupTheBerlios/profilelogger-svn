#include "DatabaseErrorDialog.h"

#include <QLayout>
#include <QLabel>
#include <QDialogButtonBox>

DatabaseErrorDialog::DatabaseErrorDialog(QWidget* p, const QueryError& e)
  : QMessageBox(QMessageBox::Critical,
		tr("Query Failed"),
		"",
		QMessageBox::Ok,
		p)

{
  setText(tr("Query Failed"));
  setDetailedText(e.text());
}

DatabaseErrorDialog::DatabaseErrorDialog(QWidget* p, const TransactionError& e)
  : QMessageBox(QMessageBox::Critical,
		tr("Transaction Failed"),
		"",
		QMessageBox::Ok,
		p)

{
  setText(tr("Transaction Failed"));
  setDetailedText(e.text());
}

DatabaseErrorDialog::DatabaseErrorDialog(QWidget* p, const ConnectionError& e)
  : QMessageBox(QMessageBox::Critical,
		tr("Connection Failed"),
		"",
		QMessageBox::Ok,
		p)

{
  setText(tr("Connection Failed"));
  setDetailedText(e.text());
}
