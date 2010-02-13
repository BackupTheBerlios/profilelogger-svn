/* 
 * File:   LithologyLegendItem.cpp
 * Author: jolo
 * 
 * Created on 13. Januar 2010, 16:08
 */

#include <qpen.h>

#include "LithologyLegendItem.h"

#include "Lithology.h"
#include "ProfileLogger.h"
#include "GraphicBedItem.h"
#include "Settings.h"
#include "ProfileLogger.h"

LithologyLegendItem::LithologyLegendItem(QGraphicsItem* parent, Lithology* l, int width, int height)
: PatternLegendItem(parent, width, height),
_lithology(l) {

    ProfileLogger* app = (static_cast<ProfileLogger*> (QApplication::instance()));
    QBrush b = app->getBrushFromFileName(app->getSettings()->getLithologiesPatternPath(), l->getFileName());

    addPattern(b);
    addId(l->getId());
    addName(l->getName());
}

LithologyLegendItem::~LithologyLegendItem() {
}
