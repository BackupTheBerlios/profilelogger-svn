#include "DatasetInProjectWithFileNameEditorDialog.h"

#include <QLayout>
#include <QLabel>
#include <QGroupBox>

#include "FileNameBrowserWidget.h"
#include "DatasetInProjectWithFileName.h"
#include "IdLabel.h"
#include "NameEdit.h"
#include "DescriptionEdit.h"
#include "FileNameBrowserWidget.h"
#include "ImageFileNameBrowserWidget.h"

DatasetInProjectWithFileNameEditorDialog::DatasetInProjectWithFileNameEditorDialog(QWidget* p, DatasetInProjectWithFileName* d)
  : DatasetInProjectEditorDialog(p, d),
    _fileNameW(0),
    _imageFileNameW(0) {
}

DatasetInProjectWithFileName* DatasetInProjectWithFileNameEditorDialog::getDatasetInProjectWithFileName() {
  return (DatasetInProjectWithFileName*)getDatasetInProject();
}

FileNameBrowserWidget* DatasetInProjectWithFileNameEditorDialog::addFileNameBrowser(const QString& label,
										    const QString& defaultPath,
										    const QString& filter) {
  _fileNameW = new FileNameBrowserWidget(getMainPage(), filter);
  _fileNameW->setDefaultPath(defaultPath);

  QGridLayout* l = ((QGridLayout*) (getMainPage()->layout()));

  l->addWidget(new QLabel(label, getMainPage()), r, lC);
  l->addWidget(_fileNameW, r, wC);

  connect(_fileNameW, SIGNAL(fileNameChanged(const QString&)), this, SLOT(slotFileNameChanged(const QString&)));
  r++;
  return _fileNameW;
}

ImageFileNameBrowserWidget* DatasetInProjectWithFileNameEditorDialog::addImageFileNameBrowser(
											      const QString& label,
											      const QString& defaultPath,
											      const QString& filter) {
  _imageFileNameW = new ImageFileNameBrowserWidget(getMainPage(), filter);
  _imageFileNameW->setDefaultPath(defaultPath);

  QGridLayout* l = ((QGridLayout*) (getMainPage()->layout()));

  l->addWidget(new QLabel(label, getMainPage()), r, lC);
  l->addWidget(_imageFileNameW, r, wC);
  r++;

  connect(_imageFileNameW, SIGNAL(fileNameChanged(const QString&)), this, SLOT(slotFileNameChanged(const QString&)));

  return _imageFileNameW;
}

void DatasetInProjectWithFileNameEditorDialog::slotFileNameChanged(const QString& s) {
  getDatasetInProjectWithFileName()->setFileName(s);
}

void DatasetInProjectWithFileNameEditorDialog::slotShowDataset(Dataset* d) {
  if (!d) {
    return;
  }

  DatasetInProjectWithFileName* dd = (DatasetInProjectWithFileName*) d;

  if (hasIdWidget()) {
    getIdLabel()->setId(dd->getId());
  }

  if (hasNameWidget()) {
    getNameEdit()->setText(dd->getName());
  }

  if (hasDescriptionWidget()) {
    getDescriptionEdit()->setText(dd->getDescription());
  }

  if (hasFileNameWidget()) {
    getFileNameBrowser()->setFileName(dd->getFileName());
  }

  if (hasImageFileNameWidget()) {
    getImageFileNameBrowser()->setImageFileName(dd->getFileName());
  }
}
