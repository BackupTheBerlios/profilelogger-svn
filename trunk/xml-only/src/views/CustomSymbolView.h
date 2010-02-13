/*
 * File:   CustomSymbolView.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:44
 */

#ifndef _CUSTOMSYMBOLVIEW_H
#define	_CUSTOMSYMBOLVIEW_H

#include "TreeView.h"

#include <QList>

class Project;

class CustomSymbolItemModel;
class CustomSymbol;

class CustomSymbolView : public TreeView {
    Q_OBJECT
public:
    CustomSymbolView(QWidget* parent, CustomSymbolItemModel* model);
    virtual ~CustomSymbolView();
    QList<CustomSymbol*> getSelectedCustomSymbols();

signals:
    void reloadRequest();
    void editRequest(const QModelIndex& idx);
    void deleteRequest(QModelIndexList indexes);
    void currentCustomSymbolChanged(CustomSymbol* p);

public slots:
    void selectCustomSymbol(CustomSymbol* q);
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

#endif	/* _CUSTOMSYMBOLVIEW_H */

