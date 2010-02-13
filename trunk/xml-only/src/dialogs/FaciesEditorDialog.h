/*
 * File:   FaciesEditorDialog.h
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 21:39
 */

#ifndef _FACIESEDITORDIALOG_H
#define	_FACIESEDITORDIALOG_H

#include "DatasetWithFileNameEditorDialog.h"

class Facies;

class FaciesEditorDialog: public DatasetWithFileNameEditorDialog {
    Q_OBJECT
public:
    FaciesEditorDialog(QWidget* parent, Facies* p);
    virtual ~FaciesEditorDialog();
    Facies* getFacies();
};

#endif	/* _FACIESEDITORDIALOG_H */
