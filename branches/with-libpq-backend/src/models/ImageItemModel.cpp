/*
 * File:   ImageItemModel.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 11:39
 */

#include "ImageItemModel.h"

#include <QList>
#include <QFileDialog>
#include <QMessageBox>
#include <QFile>
#include <QTextStream>
#include <QDir>
#include <QFileInfo>

#include "MainWindow.h"
#include "StandardItemModel.h"
#include "ProfileLogger.h"
#include "Profile.h"
#include "Project.h"
#include "ImageItem.h"
#include "ImageEditorDialog.h"
#include "Image.h"
#include "WorkWidget.h"

ImageItemModel::ImageItemModel(QObject* p)
: StandardItemModel(p),
_profile(0) {
    setSortRole(Qt::UserRole);
}

ImageItemModel::~ImageItemModel() {
}

void ImageItemModel::slotCurrentProfileChanged(Profile* p) {
    _profile = p;

    reload();
}

void ImageItemModel::reload() {
    clear();

    QStringList hh;
    hh << tr("Images");
    setHorizontalHeaderLabels(hh);

    if (!_profile) {
        return;
    }

    for (QList<Image*>::iterator it = _profile->getFirstImage();
            it != _profile->getLastImage();
            it++) {
        appendItem(*it);
    }

    emit reloaded();
}

ImageItem* ImageItemModel::appendItem(Image* b) {
    ImageItem* itm = new ImageItem(b);
    appendRow(itm);
    return itm;
}

void ImageItemModel::slotCreate() {
    Image* image = _profile->createImage();

    ImageEditorDialog* dlg = new ImageEditorDialog((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(), image);
    dlg->exec();

    reload();

    emit selectRequest(indexFromItem(findItemForImage(image)));
}

void ImageItemModel::slotEdit(const QModelIndex& idx) {
    if (!idx.isValid()) {
        return;
    }

    ImageItem* itm = (ImageItem*) itemFromIndex(idx);
    Image* image = itm->getImage();

    ImageEditorDialog* dlg = new ImageEditorDialog((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(), image);
    dlg->exec();

    reload();

    emit selectRequest(indexFromItem(findItemForImage(image)));
}

ImageItem* ImageItemModel::findItemForImage(Image* b) {
    if (!b) {
        return 0;
    }

    int max = rowCount();
    for (int r = 0; r < max; r++) {
        ImageItem* itm = (ImageItem*) item(r);
        if (itm->getImage()->getId() == b->getId()) {
            return itm;
        }
    }
    return 0;
}

void ImageItemModel::slotDelete(QModelIndexList lst) {
    for (QModelIndexList::iterator it = lst.begin(); it != lst.end(); it++) {
        ImageItem* itm = (ImageItem*) itemFromIndex(*it);
        _profile->deleteImage(itm->getImage());
    }
    reload();
}
