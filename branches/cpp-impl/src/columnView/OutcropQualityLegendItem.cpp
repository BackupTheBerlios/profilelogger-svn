/*
 * File:   OutcropQualityLegendItem.cpp
 * Author: jolo
 *
 * Created on 13. Januar 2010, 16:08
 */

#include <qpen.h>

#include "OutcropQualityLegendItem.h"

#include "OutcropQuality.h"
#include "ProfileLogger.h"
#include "GraphicBedItem.h"
#include "Settings.h"
#include "ProfileLogger.h"

OutcropQualityLegendItem::OutcropQualityLegendItem(QGraphicsItem* parent, OutcropQuality* l, int width, int height)
: PatternLegendItem(parent, width, height),
_outcropQuality(l) {

    ProfileLogger* app = (static_cast<ProfileLogger*> (QApplication::instance()));
    QBrush b = app->getBrushFromFileName(app->getSettings()->getOutcropQualitiesPath(), l->getFileName());

    addPattern(b);
    addId(l->getId());
    addName(l->getName());
}

OutcropQualityLegendItem::~OutcropQualityLegendItem() {
}
