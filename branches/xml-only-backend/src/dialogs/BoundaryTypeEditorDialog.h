/*
 * File:   BoundaryTypeEditorDialog.h
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 21:39
 */

#ifndef _BOUNDARYTYPEEDITORDIALOG_H
#define	_BOUNDARYTYPEEDITORDIALOG_H

#include "DatasetWithFileNameEditorDialog.h"

class BoundaryType;

class BoundaryTypeEditorDialog: public DatasetWithFileNameEditorDialog {
    Q_OBJECT
public:
    BoundaryTypeEditorDialog(QWidget* parent, BoundaryType* p);
    virtual ~BoundaryTypeEditorDialog();
    BoundaryType* getBoundaryType();
};

#endif	/* _BOUNDARYTYPEEDITORDIALOG_H */
