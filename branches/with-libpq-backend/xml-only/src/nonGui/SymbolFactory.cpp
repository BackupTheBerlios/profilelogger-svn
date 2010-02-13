/* 
 * File:   SymbolFactory.cpp
 * Author: jolo
 * 
 * Created on 24. Dezember 2009, 11:40
 */

#include "SymbolFactory.h"

#include <QString>
#include <QFileInfo>
#include <QApplication>

#include "ProfileLogger.h"
#include "GraphicBedItem.h"
#include "GraphicSvgItem.h"
#include "Fossil.h"
#include "CustomSymbol.h"
#include "SedimentStructure.h"
#include "Settings.h"
#include "BoundaryType.h"

SymbolFactory::SymbolFactory(QGraphicsItem* b)
: _parent(b) {
}

SymbolFactory::~SymbolFactory() {
}

GraphicSvgItem* SymbolFactory::make(Fossil* ds, int maxSize) {
    QString path = (static_cast<ProfileLogger*> (QApplication::instance()))->getSettings()->getFossilsPath();
    QFileInfo fi(path, ds->getFileName());

    if (!fi.isReadable()) {
        return 0;
    }

    GraphicSvgItem* itm = new GraphicSvgItem(fi.canonicalFilePath(), _parent);

    Q_ASSERT(0 != itm);

    if (itm->boundingRect().width() <= 0) {
        return 0;
    }

    itm->scale(calculateScaleFactor(itm, maxSize), calculateScaleFactor(itm, maxSize));

    return itm;
}

qreal SymbolFactory::calculateScaleFactor(GraphicSvgItem* itm, int maxSize) {
    // scale to fit into max size
    qreal f = 1.0;

    if (itm->boundingRect().width() > itm->boundingRect().height()) {
        f = (qreal) maxSize / itm->boundingRect().width();
    } else {
        f = (qreal) maxSize / itm->boundingRect().height();
    }

    return f;
}

GraphicSvgItem* SymbolFactory::make(SedimentStructure* ds, int maxSize) {
    QString path = (static_cast<ProfileLogger*> (QApplication::instance()))->getSettings()->getSedimentStructuresPath();
    QFileInfo fi(path, ds->getFileName());

    if (!fi.isReadable()) {
        return 0;
    }

    GraphicSvgItem* itm = new GraphicSvgItem(fi.canonicalFilePath(), _parent);
    Q_ASSERT(0 != itm);

    if (itm->boundingRect().width() <= 0) {
        return 0;
    }

    itm->scale(calculateScaleFactor(itm, maxSize), calculateScaleFactor(itm, maxSize));

    return itm;
}

GraphicSvgItem* SymbolFactory::make(CustomSymbol* ds, int maxSize) {
    QString path = (static_cast<ProfileLogger*> (QApplication::instance()))->getSettings()->getCustomSymbolsPath();
    QFileInfo fi(path, ds->getFileName());

    if (!fi.isReadable()) {
        return 0;
    }

    GraphicSvgItem* itm = new GraphicSvgItem(fi.canonicalFilePath(), _parent);
    Q_ASSERT(0 != itm);

    if (itm->boundingRect().width() <= 0) {
        return 0;
    }

    itm->scale(calculateScaleFactor(itm, maxSize), calculateScaleFactor(itm, maxSize));

    return itm;
}

GraphicSvgItem* SymbolFactory::make(BoundaryType* t, int maxSize) {
    QString path = (static_cast<ProfileLogger*> (QApplication::instance()))->getSettings()->getBoundaryTypesPath();
    QFileInfo fi(path, t->getFileName());

    if (!fi.isReadable()) {
        return 0;
    }

    GraphicSvgItem* itm = new GraphicSvgItem(fi.canonicalFilePath(), _parent);
    Q_ASSERT(0 != itm);

    if (itm->boundingRect().width() <= 0) {
        return 0;
    }

    itm->scale(calculateScaleFactor(itm, maxSize), 1.0);

    return itm;
}

