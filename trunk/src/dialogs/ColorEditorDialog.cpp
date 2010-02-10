/*
 * File:   ColorEditorDialog.cpp
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 21:39
 */

#include "ColorEditorDialog.h"

#include <QLayout>
#include <QLabel>
#include <QGroupBox>

#include "QtPatternSelectorWidget.h"

#include "Color.h"

ColorEditorDialog::ColorEditorDialog(QWidget* parent, Color* p)
: DatasetEditorDialog(parent, p) {
    addMainPage(tr("Color"));
    addIdLabel();
    addNameEdit();

    _patternsW = new QtPatternSelectorWidget(getMainPage());
    ((QGridLayout*)(getMainPage()->layout()))->addWidget(new QLabel(tr("Pattern"), getMainPage()), r, lC);
    ((QGridLayout*)(getMainPage()->layout()))->addWidget(_patternsW, r, wC);
    r++;

    addDescriptionEdit();
    addButtons();

    emit showDatasetRequest(getColor());
    slotShowDataset(getColor());

    _patternsW->setPattern(getColor()->getBrushStyle());
    connect(_patternsW, SIGNAL(patternChanged(Qt::BrushStyle)), this, SLOT(slotPatternChanged(Qt::BrushStyle)));
}

ColorEditorDialog::~ColorEditorDialog() {
}

Color* ColorEditorDialog::getColor() {
    return (Color*) getDataset();
}

void ColorEditorDialog::slotPatternChanged(Qt::BrushStyle s) {
    getColor()->setBrushStyle(s);
}
