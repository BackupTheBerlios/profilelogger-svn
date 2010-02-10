/*
 * File:   ProfileCorrelationEditorDialog.h
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 21:39
 */

#ifndef _PROFILECORRELATIONEDITORDIALOG_H
#define	_PROFILECORRELATIONEDITORDIALOG_H

#include "DatasetEditorDialog.h"

class ProfileCorrelation;

class ProfileCorrelationEditorDialog : public DatasetEditorDialog {
    Q_OBJECT
public:
    ProfileCorrelationEditorDialog(QWidget* parent, ProfileCorrelation* p);
    virtual ~ProfileCorrelationEditorDialog();
    ProfileCorrelation* getProfileCorrelation();
};

#endif	/* _PROFILECORRELATIONEDITORDIALOG_H */
