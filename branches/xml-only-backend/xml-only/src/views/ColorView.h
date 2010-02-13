/*
 * File:   ColorView.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:44
 */

#ifndef _COLORVIEW_H
#define	_COLORVIEW_H

#include "TreeView.h"

class Project;

class ColorItemModel;
class Color;

class ColorView : public TreeView {
    Q_OBJECT
public:
    ColorView(QWidget* parent, ColorItemModel* model);
    virtual ~ColorView();

signals:
    void reloadRequest();
    void editRequest(const QModelIndex& idx);
    void deleteRequest(QModelIndexList indexes);
    void currentColorChanged(Color* p);

public slots:
    void selectColor(Color* q);
    void slotIndexActivated(const QModelIndex&);
    void slotCurrentProjectChanged(Project* p);
    void slotCustomContextMenuRequested(const QPoint& p);
    void slotSelectItemRequested(const QModelIndex& idx);
    void slotReload();
    void slotEdit();
    void slotDelete();

private:
    Project* _project;
};

#endif	/* _COLORVIEW_H */

