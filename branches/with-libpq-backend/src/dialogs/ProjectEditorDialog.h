/*
 * File:   ProjectEditorDialog.h
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 21:39
 */

#ifndef _PROJECTEDITORDIALOG_H
#define	_PROJECTEDITORDIALOG_H

#include "DatasetEditorDialog.h"
#include "GrainSizeModes.h"

class Project;

class ProjectEditorDialog : public DatasetEditorDialog {
    Q_OBJECT
public:
    ProjectEditorDialog(QWidget* parent, Project* p);
    virtual ~ProjectEditorDialog();
    Project* getProject();
};

#endif	/* _PROJECTEDITORDIALOG_H */