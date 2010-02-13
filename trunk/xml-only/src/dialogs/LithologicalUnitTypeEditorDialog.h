/*
 * File:   LithologicalUnitTypeEditorDialog.h
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 21:39
 */

#ifndef _LITHOLOGICALUNITTYPEEDITORDIALOG_H
#define	_LITHOLOGICALUNITTYPEEDITORDIALOG_H

#include "DatasetEditorDialog.h"

class LithologicalUnitType;

class QtPatternSelectorWidget;

class LithologicalUnitTypeEditorDialog: public DatasetEditorDialog {
    Q_OBJECT
public:
    LithologicalUnitTypeEditorDialog(QWidget* parent, LithologicalUnitType* p);
    virtual ~LithologicalUnitTypeEditorDialog();
    LithologicalUnitType* getLithologicalUnitType();
};

#endif	/* _LITHOLOGICALUNITTYPEEDITORDIALOG_H */
