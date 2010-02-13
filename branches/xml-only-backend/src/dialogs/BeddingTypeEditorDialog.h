/*
 * File:   BeddingTypeEditorDialog.h
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 21:39
 */

#ifndef _BEDDINGTYPEEDITORDIALOG_H
#define	_BEDDINGTYPEEDITORDIALOG_H

#include "DatasetWithFileNameEditorDialog.h"

class BeddingType;

class BeddingTypeEditorDialog: public DatasetWithFileNameEditorDialog {
    Q_OBJECT
public:
    BeddingTypeEditorDialog(QWidget* parent, BeddingType* p);
    virtual ~BeddingTypeEditorDialog();
    BeddingType* getBeddingType();
};

#endif	/* _BEDDINGTYPEEDITORDIALOG_H */
