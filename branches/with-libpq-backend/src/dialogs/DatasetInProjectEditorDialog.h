#ifndef DATASETINPROJECTEDITORDIALOG_H
#define DATASETINPROJECTEDITORDIALOG_H

#include "DatasetEditorDialog.h"

class DatasetInProject;

class DatasetInProjectEditorDialog: public DatasetEditorDialog {
  Q_OBJECT
    public:
  DatasetInProjectEditorDialog(QWidget* p, DatasetInProject* d);
  virtual ~DatasetInProjectEditorDialog() {};

  DatasetInProject* getDatasetInProject();
};

#endif
