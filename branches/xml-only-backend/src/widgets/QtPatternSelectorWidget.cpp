/* 
 * File:   QtPatternSelectorWidget.cpp
 * Author: jolo
 * 
 * Created on 19. Dezember 2009, 11:36
 */

#include "QtPatternSelectorWidget.h"

QtPatternSelectorWidget::QtPatternSelectorWidget(QWidget * p)
: QComboBox(p) {
    setupPatterns();
    connect(this, SIGNAL(currentIndexChanged(int)), this, SLOT(slotCurrentIndexChanged(int)));
}

QtPatternSelectorWidget::~QtPatternSelectorWidget() {
}

void QtPatternSelectorWidget::slotCurrentIndexChanged(int idx) {
    emit patternChanged(_brushes[idx]);
}

void QtPatternSelectorWidget::setupPatterns() {
    int idx = 0;
    _brushes[idx++] = Qt::HorPattern;
    insertItem(idx, tr("Horizontal Pattern"));
    _brushes[idx++] = Qt::VerPattern;
    insertItem(idx, tr("Vertical Pattern"));
    _brushes[idx++] = Qt::CrossPattern;
    insertItem(idx, tr("Cross Pattern"));
    _brushes[idx++] = Qt::BDiagPattern;
    insertItem(idx, tr("Right Diagonal Pattern"));
    _brushes[idx++] = Qt::FDiagPattern;
    insertItem(idx, tr("Left Diagonal Pattern"));
    _brushes[idx++] = Qt::DiagCrossPattern;
    insertItem(idx, tr("Diagonal Cross Pattern"));
    _brushes[idx++] = Qt::SolidPattern;
    insertItem(idx, tr("Solid"));
    _brushes[idx++] = Qt::Dense1Pattern;
    insertItem(idx, tr("Dense 1"));
    _brushes[idx++] = Qt::Dense2Pattern;
    insertItem(idx, tr("Dense 2"));
    _brushes[idx++] = Qt::Dense3Pattern;
    insertItem(idx, tr("Dense 3"));
    _brushes[idx++] = Qt::Dense4Pattern;
    insertItem(idx, tr("Dense 4"));
    _brushes[idx++] = Qt::Dense5Pattern;
    insertItem(idx, tr("Dense 5"));
    _brushes[idx++] = Qt::Dense6Pattern;
    insertItem(idx, tr("Dense 6"));
    _brushes[idx++] = Qt::NoBrush;
    insertItem(idx, tr("No Brush"));
}

void QtPatternSelectorWidget::setPattern(Qt::BrushStyle s) {
    for (QMap<int, Qt::BrushStyle>::iterator it = _brushes.begin(); it != _brushes.end(); it++) {
        if (it.value() == s) {
            setCurrentIndex(it.key());
            return;
        }
    }
}
