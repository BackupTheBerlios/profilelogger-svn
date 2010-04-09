/*
 * File:   ImageEditorDialog.cpp
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 21:39
 */

#include "ImageEditorDialog.h"

#include <QLayout>
#include <QLabel>
#include <QGroupBox>

#include "QtPatternSelectorWidget.h"

#include "Image.h"
#include "ProfileLogger.h"
#include "Settings.h"

ImageEditorDialog::ImageEditorDialog(QWidget* parent, Image* p)
: DatasetWithFileNameEditorDialog(parent, p) {
    addMainPage(tr("Image"));
    addIdLabel();
    addNameEdit();
    addImageFileNameBrowser(tr("Image File"),
            (static_cast<ProfileLogger*>(QApplication::instance()))->getSettings()->getImagePath(),
            tr("JPEG Files *.jpg *.JPG *.jpeg *.JPEG"));
    addDescriptionEdit();
    addButtons();

    emit showDatasetRequest(getImage());
    slotShowDataset(getImage());
}

ImageEditorDialog::~ImageEditorDialog() {
}

Image* ImageEditorDialog::getImage() {
    return (Image*) getDataset();
}
