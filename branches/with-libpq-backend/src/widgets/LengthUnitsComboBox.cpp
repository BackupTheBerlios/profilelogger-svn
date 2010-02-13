/* 
 * File:   LengthUnitsComboBox.cpp
 * Author: jolo
 * 
 * Created on 29. Januar 2010, 15:10
 */

#include "LengthUnitsComboBox.h"

#include "ProfileLogger.h"
#include "Project.h"
#include "LengthUnit.h"

#include <QApplication>

LengthUnitsComboBox::LengthUnitsComboBox(QWidget* p)
: QComboBox(p) {
    for (QList<LengthUnit*>::iterator it = (static_cast<ProfileLogger*> (QApplication::instance()))->getProject()->getFirstLengthUnit();
            it != (static_cast<ProfileLogger*> (QApplication::instance()))->getProject()->getLastLengthUnit();
            it++) {
        _units[(*it)->getName()] = *it;
        addItem((*it)->getName());
    }

    connect(this, SIGNAL(activated(const QString&)), this, SLOT(slotSelectionChanged(const QString&)));
}

LengthUnitsComboBox::~LengthUnitsComboBox() {
}

void LengthUnitsComboBox::slotSelectionChanged(const QString& s) {
    emit lengthUnitChanged(_units[s]);
}

void LengthUnitsComboBox::setLengthUnit(LengthUnit* u) {
    if (!u) {
        return;
    }

    int idx = findData(u->getName(), Qt::DisplayRole);
    setCurrentIndex(idx);
}