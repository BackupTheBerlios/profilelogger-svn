/* 
 * File:   DescriptionEdit.cpp
 * Author: jolo
 * 
 * Created on 10. Dezember 2009, 20:54
 */

#include "DescriptionEdit.h"

#include <QLabel>

DescriptionEdit::DescriptionEdit(QWidget* p)
: QTextEdit(p),
_lbl(0) {
    connect(this, SIGNAL(textChanged()), this, SLOT(slotTextChanged()));
}

DescriptionEdit::~DescriptionEdit() {
}

QLabel* DescriptionEdit::getLabel() {
    if (!_lbl) {
        _lbl = new QLabel(tr("&Description"), (QWidget*)parent());
        _lbl->setBuddy(this);
        _lbl->setAlignment(Qt::AlignTop | Qt::AlignRight);
    }

    return _lbl;
}

void DescriptionEdit::slotTextChanged() {
    emit descriptionChanged(document()->toPlainText());
}
