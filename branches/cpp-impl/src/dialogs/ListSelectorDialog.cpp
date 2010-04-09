/* 
 * File:   ListSelectorDialog.cpp
 * Author: jolo
 * 
 * Created on 23. Januar 2010, 08:41
 */

#include "ListSelectorDialog.h"
#include "BedEditorDialog.h"

#include <QWidget>
#include <QLabel>

ListSelectorDialog::ListSelectorDialog(QWidget* p, const QString& title)
: QDialog(p),
_currentDataset(0),
_title(title) {
    setLayout(new QVBoxLayout(this));
}

void ListSelectorDialog::setView(TreeView* v) {
    QWidget* w = new QWidget(this);
    w->setLayout(new QVBoxLayout(w));
    w->layout()->addWidget(new QLabel(_title, w));
    w->layout()->addWidget(v);

    layout()->addWidget(w);

    _bb = new QDialogButtonBox(QDialogButtonBox::Ok | QDialogButtonBox::Cancel, Qt::Horizontal, this);
    connect(_bb, SIGNAL(accepted()), this, SLOT(accept()));
    connect(_bb, SIGNAL(rejected()), this, SLOT(reject()));
    layout()->addWidget(_bb);
}

ListSelectorDialog::~ListSelectorDialog() {
}

void ListSelectorDialog::slotSelectionChanged(Dataset* d) {
    _currentDataset = d;
}
