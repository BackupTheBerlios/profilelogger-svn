/*
 * File:   FaciesLegendItem.cpp
 * Author: jolo
 *
 * Created on 13. Januar 2010, 16:08
 */

#include <qpen.h>

#include "FaciesLegendItem.h"

#include "Facies.h"
#include "ProfileLogger.h"
#include "GraphicBedItem.h"
#include "Settings.h"
#include "ProfileLogger.h"

FaciesLegendItem::FaciesLegendItem(QGraphicsItem* parent, Facies* l, int width, int height)
: PatternLegendItem(parent, width, height),
_lithology(l) {

    ProfileLogger* app = (static_cast<ProfileLogger*> (QApplication::instance()));
    QBrush b = app->getBrushFromFileName(app->getSettings()->getFaciesPath(), l->getFileName());

    addPattern(b);
    addId(l->getId());
    addName(l->getName());
}

FaciesLegendItem::~FaciesLegendItem() {
}
