/* 
 * File:   TreeView.h
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 20:10
 */

#ifndef _TREEVIEW_H
#define	_TREEVIEW_H

#include <QTreeView>

class TreeView: public QTreeView {
    Q_OBJECT
public:
    TreeView(QWidget* p = 0);
    virtual ~TreeView();

public slots:
    virtual void slotReloaded();
    
private:

};

#endif	/* _TREEVIEW_H */

