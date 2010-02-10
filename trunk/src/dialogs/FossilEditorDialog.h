/*
 * File:   FossilEditorDialog.h
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 21:39
 */

#ifndef _FOSSILEDITORDIALOG_H
#define	_FOSSILEDITORDIALOG_H

#include "DatasetWithFileNameEditorDialog.h"

class Fossil;

class FossilEditorDialog: public DatasetWithFileNameEditorDialog {
    Q_OBJECT
public:
    FossilEditorDialog(QWidget* parent, Fossil* p);
    virtual ~FossilEditorDialog();
    Fossil* getFossil();
};

#endif	/* _FOSSILEDITORDIALOG_H */
