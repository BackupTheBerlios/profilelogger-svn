#include "DatabaseErrorDialog.h"

#include <QLayout>
#include <QLabel>
#include <QDialogButtonBox>

DatabaseErrorDialog::DatabaseErrorDialog(QWidget* p, const DatabaseError& e)
  : QMessageBox(QMessageBox::Critical,
		tr("Query Failed"),
		"",
		QMessageBox::Ok,
		p)

{
  setText(e.getMessage());
  setDetailedText(tr("Query: %1\n\n%2")
		  .arg(e.getSql())
		  .arg(e.getDatabaseMessage()));
}
