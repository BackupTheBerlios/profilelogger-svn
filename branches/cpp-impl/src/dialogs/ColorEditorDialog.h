/*
 * File:   ColorEditorDialog.h
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 21:39
 */

#ifndef _COLOREDITORDIALOG_H
#define	_COLOREDITORDIALOG_H

#include "DatasetEditorDialog.h"

class Color;

class QtPatternSelectorWidget;

class ColorEditorDialog: public DatasetEditorDialog {
    Q_OBJECT
public:
    ColorEditorDialog(QWidget* parent, Color* p);
    virtual ~ColorEditorDialog();
    Color* getColor();

public slots:
    virtual void slotPatternChanged(Qt::BrushStyle s);

private:
    QtPatternSelectorWidget* _patternsW;
};

#endif	/* _COLOREDITORDIALOG_H */
