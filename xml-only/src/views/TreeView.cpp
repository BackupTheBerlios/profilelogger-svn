/* 
 * File:   TreeView.cpp
 * Author: jolo
 * 
 * Created on 10. Dezember 2009, 20:10
 */

#include "TreeView.h"

TreeView::TreeView(QWidget* p)
: QTreeView(p) {
    setEditTriggers(QAbstractItemView::NoEditTriggers);
    setSortingEnabled(true);
}

TreeView::~TreeView() {
}

void TreeView::slotReloaded() {
    sortByColumn(0, Qt::AscendingOrder);
}
