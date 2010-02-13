/*
 * File:   ImageItemView.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 11:40
 */

#ifndef _IMAGEITEMVIEW_H
#define	_IMAGEITEMVIEW_H

#include "TreeView.h"

class Profile;
class Image;
class ImageItemModel;

class ImageItemView : public TreeView {
    Q_OBJECT
public:
    ImageItemView(QWidget* p, ImageItemModel* model);
    virtual ~ImageItemView();

signals:
    void currentImageChanged(Image* bed);
    void reloadRequest();
    void createImageRequest();
    void editRequest(const QModelIndex& idx);
    void deleteRequest(QModelIndexList indexes);

public slots:
    void slotCurrentProfileChanged(Profile* p);
    void slotCustomContextMenuRequested(const QPoint& p);
    void slotIndexActivated(const QModelIndex&);

    void slotReload();
    void slotCreate();
    void slotEdit();
    void slotDelete();
    void slotReloaded();

private:
    Profile* _profile;
};

#endif	/* _IMAGEITEMVIEW_H */
