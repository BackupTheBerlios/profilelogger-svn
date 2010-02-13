/*
 * File:   SedimentStructureEditorDialog.h
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 21:39
 */

#ifndef _SEDIMENTSTRUCTUREEDITORDIALOG_H
#define	_SEDIMENTSTRUCTUREEDITORDIALOG_H

#include "DatasetWithFileNameEditorDialog.h"

class SedimentStructure;

class SedimentStructureEditorDialog: public DatasetWithFileNameEditorDialog {
    Q_OBJECT
public:
    SedimentStructureEditorDialog(QWidget* parent, SedimentStructure* p);
    virtual ~SedimentStructureEditorDialog();
    SedimentStructure* getSedimentStructure();
};

#endif	/* _SEDIMENTSTRUCTUREEDITORDIALOG_H */
