/* 
 * File:   IdLabel.cpp
 * Author: jolo
 * 
 * Created on 10. Dezember 2009, 21:24
 */

#include "IdLabel.h"

IdLabel::IdLabel(QWidget* p)
: QLabel(p),
_lbl(0) {
    setId(0);
}

IdLabel::~IdLabel() {
}

void IdLabel::setId(int id) {
    if (id < 1) {
        setText(tr("<Not Set>"));
    } else {
        setText(QString::number(id));
    }
}

QLabel* IdLabel::getLabel() {
    if (!_lbl) {
        _lbl = new QLabel(tr("ID"), this);
        _lbl->setAlignment(Qt::AlignHCenter | Qt::AlignRight);
    }

    return _lbl;
}
