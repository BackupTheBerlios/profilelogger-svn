/*
 * File:   OutcropQualityEditorDialog.h
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 21:39
 */

#ifndef _OUTCROPQUALITYEDITORDIALOG_H
#define	_OUTCROPQUALITYEDITORDIALOG_H

#include "DatasetWithFileNameEditorDialog.h"

class OutcropQuality;

class OutcropQualityEditorDialog: public DatasetWithFileNameEditorDialog {
    Q_OBJECT
public:
    OutcropQualityEditorDialog(QWidget* parent, OutcropQuality* p);
    virtual ~OutcropQualityEditorDialog();
    OutcropQuality* getOutcropQuality();
};

#endif	/* _OUTCROPQUALITYEDITORDIALOG_H */
