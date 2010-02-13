/*
 * File:   LithologicalUnitEditorDialog.h
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 21:39
 */

#ifndef _LITHOLOGICALUNITEDITORDIALOG_H
#define	_LITHOLOGICALUNITEDITORDIALOG_H

#include "DatasetEditorDialog.h"

class LithologicalUnit;
class LithologicalUnitType;

class LithologicalUnitTypeView;

class QtPatternSelectorWidget;

class LithologicalUnitEditorDialog: public DatasetEditorDialog {
    Q_OBJECT
public:
    LithologicalUnitEditorDialog(QWidget* parent, LithologicalUnit* p);
    virtual ~LithologicalUnitEditorDialog();
    LithologicalUnit* getLithologicalUnit();

public slots:
    void slotLithologicalUnitTypeChanged(LithologicalUnitType* t);
    
private:
    LithologicalUnitTypeView* _typeV;
};

#endif	/* _LITHOLOGICALUNITEDITORDIALOG_H */
