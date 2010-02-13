/*
 * File:   GrainSizeItemModel.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:42
 */

#include "GrainSizeItemModel.h"

#include <QApplication>

#include "ProfileLogger.h"
#include "GrainSizeItem.h"
#include "Project.h"
#include "GrainSize.h"

class Project;

GrainSizeItemModel::GrainSizeItemModel(QObject* p)
: StandardItemModel(p),
_project(0) {
}

GrainSizeItemModel::~GrainSizeItemModel() {
}

void GrainSizeItemModel::slotCurrentProjectChanged(Project* p) {
    (void) p;
}

void GrainSizeItemModel::reload() {
}

GrainSizeItem* GrainSizeItemModel::appendItem(GrainSize* p) {
    (void) p;
    return 0;
}

GrainSizeItem* GrainSizeItemModel::findItemForGrainSize(int id) {
    (void) id;
    return 0;
}

QModelIndex GrainSizeItemModel::findIndexForGrainSize(GrainSize* q) {
    (void) q;
    return QModelIndex();
}
