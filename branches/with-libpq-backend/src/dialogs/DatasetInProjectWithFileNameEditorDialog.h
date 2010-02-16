#ifndef DATASETINPROJECTWITHFILENAMEEDITORDIALOG_H
#define DATASETINPROJECTWITHFILENAMEEDITORDIALOG_H

#include "DatasetInProjectEditorDialog.h"

class FileNameBrowserWidget;
class ImageFileNameBrowserWidget;
class DatasetInProjectWithFileName;

class DatasetInProjectWithFileNameEditorDialog: public DatasetInProjectEditorDialog {
  Q_OBJECT
    public:
  DatasetInProjectWithFileNameEditorDialog(QWidget* p,
					   DatasetInProjectWithFileName* d);
  virtual ~DatasetInProjectWithFileNameEditorDialog() {}

  DatasetInProjectWithFileName* getDatasetInProjectWithFileName();

  public slots:
  virtual void slotFileNameChanged(const QString& s);
  virtual void slotShowDataset(Dataset* d);

 protected:
  bool hasFileNameWidget() const {
    return 0 != _fileNameW;
  }

  bool hasImageFileNameWidget() const {
    return 0 != _imageFileNameW;
  }

  FileNameBrowserWidget* addFileNameBrowser(const QString& label,
					    const QString& defaultPath,
					    const QString& filter = QObject::tr("SVG Files *.svg *.SVG"));
  ImageFileNameBrowserWidget* addImageFileNameBrowser(const QString& label,
						      const QString& defaultPath,
						      const QString& filter = QObject::tr("JPEG Files *.jpg *.jpeg *.JPG *.JPEG"));

  FileNameBrowserWidget* getFileNameBrowser() {
    return _fileNameW;
  }

  ImageFileNameBrowserWidget* getImageFileNameBrowser() {
    return _imageFileNameW;
  }

 private:

  FileNameBrowserWidget* _fileNameW;
  ImageFileNameBrowserWidget* _imageFileNameW;
};

#endif
