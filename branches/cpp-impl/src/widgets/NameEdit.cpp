/* 
 * File:   NameEdit.cpp
 * Author: jolo
 * 
 * Created on 10. Dezember 2009, 20:50
 */

#include "NameEdit.h"

#include <QLabel>

NameEdit::NameEdit(QWidget* p)
: QLineEdit(p),
_lbl(0) {
    connect(this, SIGNAL(textChanged(const QString&)), this, SLOT(slotTextChanged(const QString&)));
}

NameEdit::~NameEdit() {
}

QLabel* NameEdit::getLabel() {
    if (!_lbl) {
        _lbl = new QLabel(tr("&Name"), (QWidget*)parent());
        _lbl->setBuddy(this);
        _lbl->setAlignment(Qt::AlignVCenter | Qt::AlignRight);
    }

    return _lbl;
}

void NameEdit::slotTextChanged(const QString& s) {
    emit nameChanged(s);
}
