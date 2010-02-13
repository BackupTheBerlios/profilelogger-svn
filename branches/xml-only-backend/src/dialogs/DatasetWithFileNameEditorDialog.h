/* 
 * File:   DatasetWithFileNameEditorDialog.h
 * Author: jolo
 *
 * Created on 17. Dezember 2009, 13:53
 */

#ifndef _DATASETWITHFILENAMEEDITORDIALOG_H
#define	_DATASETWITHFILENAMEEDITORDIALOG_H

#include "DatasetEditorDialog.h"

class FileNameBrowserWidget;
class DatasetWithFileName;
class ImageFileNameBrowserWidget;

class DatasetWithFileNameEditorDialog : public DatasetEditorDialog {
    Q_OBJECT
public:
    DatasetWithFileNameEditorDialog(QWidget* p, DatasetWithFileName* d);
    virtual ~DatasetWithFileNameEditorDialog();

    DatasetWithFileName* getDatasetWithFileName() {
        return (DatasetWithFileName*) getDataset();
    }

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

#endif	/* _DATASETWITHFILENAMEEDITORDIALOG_H */

