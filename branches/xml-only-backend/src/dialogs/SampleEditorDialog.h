/*
 * File:   SampleEditorDialog.h
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 21:39
 */

#ifndef _SAMPLEEDITORDIALOG_H
#define	_SAMPLEEDITORDIALOG_H

#include "DatasetEditorDialog.h"

class Sample;

class QtPatternSelectorWidget;

class SampleEditorDialog : public DatasetEditorDialog {
    Q_OBJECT
public:
    SampleEditorDialog(QWidget* parent, Sample* p);
    virtual ~SampleEditorDialog();
    Sample* getSample();
};

#endif	/* _SAMPLEEDITORDIALOG_H */
