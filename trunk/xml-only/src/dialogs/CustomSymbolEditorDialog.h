/*
 * File:   CustomSymbolEditorDialog.h
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 21:39
 */

#ifndef _CUSTOMSYMBOLEDITORDIALOG_H
#define	_CUSTOMSYMBOLEDITORDIALOG_H

#include "DatasetWithFileNameEditorDialog.h"

class CustomSymbol;

class CustomSymbolEditorDialog : public DatasetWithFileNameEditorDialog {
    Q_OBJECT
public:
    CustomSymbolEditorDialog(QWidget* parent, CustomSymbol* p);
    virtual ~CustomSymbolEditorDialog();
    CustomSymbol* getCustomSymbol();
};

#endif	/* _CUSTOMSYMBOLEDITORDIALOG_H */
