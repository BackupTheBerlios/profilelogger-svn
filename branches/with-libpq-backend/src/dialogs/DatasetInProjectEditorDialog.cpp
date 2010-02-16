#include "DatasetInProjectEditorDialog.h"

#include "DatasetInProject.h"

DatasetInProjectEditorDialog::DatasetInProjectEditorDialog(QWidget* p,
							   DatasetInProject* d)
  : DatasetEditorDialog(p, d) {
}

DatasetInProject* DatasetInProjectEditorDialog::getDatasetInProject() {
  return (DatasetInProject*)getDataset();
}

