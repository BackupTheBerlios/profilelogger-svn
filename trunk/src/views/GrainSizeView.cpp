/*
 * File:   GrainSizeView.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:44
 */

#include "GrainSizeView.h"

#include <QApplication>
#include <QMessageBox>
#include <QMenu>
#include <QAction>

#include "GrainSizeItemModel.h"
#include "GrainSizeItem.h"
#include "ProfileLogger.h"
#include "Project.h"
#include "GrainSize.h"

GrainSizeView::GrainSizeView(QWidget* pl)
: TreeView(pl),
_project(0) {
}

GrainSizeView::~GrainSizeView() {
}

void GrainSizeView::slotCurrentProjectChanged(Project* p) {
    (void) p;
}

void GrainSizeView::slotCustomContextMenuRequested(const QPoint& p) {
    (void) p;
}

void GrainSizeView::slotSelectItemRequested(const QModelIndex& idx) {
    (void) idx;
}

void GrainSizeView::slotIndexActivated(const QModelIndex& idx) {
    (void) idx;
}

void GrainSizeView::slotReload() {
}

void GrainSizeView::selectGrainSize(GrainSize* q) {
    (void) q;
    return;
}
