/* 
 * File:   BeddingTypeLegendItem.cpp
 * Author: jolo
 * 
 * Created on 13. Januar 2010, 16:09
 */

#include "BeddingTypeLegendItem.h"

#include "BeddingType.h"
#include "ProfileLogger.h"
#include "Settings.h"

BeddingTypeLegendItem::BeddingTypeLegendItem(QGraphicsItem* p, BeddingType* t, int w, int h)
: PatternLegendItem(p, w, h),
_beddingType(t) {
    ProfileLogger* app = (static_cast<ProfileLogger*> (QApplication::instance()));
    QBrush b = app->getBrushFromFileName(app->getSettings()->getLithologiesPatternPath(), t->getFileName());

    addPattern(b);
    addId(t->getId());
    addName(t->getName());
}

BeddingTypeLegendItem::~BeddingTypeLegendItem() {
}
