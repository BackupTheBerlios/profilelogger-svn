/*
 * File:   ImageItemModel.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 11:39
 */

#ifndef _IMAGEITEMMODEL_H
#define	_IMAGEITEMMODEL_H

#include "StandardItemModel.h"

class Profile;
class Image;
class ImageItem;

class ImageItemModel : public StandardItemModel {
    Q_OBJECT
public:
    ImageItemModel(QObject* p = 0);
    virtual ~ImageItemModel();

signals:
    void selectRequest(const QModelIndex& idx);

public slots:
    void slotCurrentProfileChanged(Profile* p);
    void reload();

    void slotCreate();
    void slotEdit(const QModelIndex& idx);
    void slotDelete(QModelIndexList lst);

private:
    ImageItem* appendItem(Image* b);
    ImageItem* findItemForImage(Image* b);

    Profile* _profile;
};

#endif	/* _IMAGEITEMMODEL_H */

