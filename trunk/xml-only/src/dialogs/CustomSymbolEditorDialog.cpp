/*
 * File:   CustomSymbolEditorDialog.cpp
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 21:39
 */

#include "CustomSymbolEditorDialog.h"

#include "CustomSymbol.h"
#include "Settings.h"
#include "ProfileLogger.h"

CustomSymbolEditorDialog::CustomSymbolEditorDialog(QWidget* parent, CustomSymbol* p)
: DatasetWithFileNameEditorDialog(parent, p) {
    addMainPage(tr("Custom Symbol"));
    addIdLabel();
    addNameEdit();
    addFileNameBrowser(tr("Symbol File"), 
		       (static_cast<ProfileLogger*> (QApplication::instance()))->getSettings()->getCustomSymbolsPath());
    addDescriptionEdit();
    addButtons();

    emit showDatasetRequest(getCustomSymbol());
    slotShowDataset(getCustomSymbol());
}

CustomSymbolEditorDialog::~CustomSymbolEditorDialog() {
}

CustomSymbol* CustomSymbolEditorDialog::getCustomSymbol() {
    return (CustomSymbol*) getDataset();
}
