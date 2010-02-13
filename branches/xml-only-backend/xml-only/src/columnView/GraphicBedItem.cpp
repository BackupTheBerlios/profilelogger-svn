/* 
 * File:   GraphicBedItem.cpp
 * Author: jolo
 * 
 * Created on 16. Dezember 2009, 18:56
 */

#include <QGraphicsScene>
#include <QGraphicsItem>
#include <QApplication>
#include <QGraphicsSceneContextMenuEvent>
#include <QMenu>
#include <QAction>

#include "GraphicBedItem.h"
#include "GraphicColumnHeader.h"
#include "GraphicSvgItem.h"
#include "SymbolFactory.h"
#include "ProfileLogger.h"
#include "Bed.h"
#include "Lithology.h"
#include "BoundaryType.h"
#include "BeddingType.h"
#include "LengthUnit.h"
#include "DatasetWithFileName.h"
#include "ProfileLogger.h"
#include "GrainSize.h"
#include "ClasticGrainSize.h"
#include "CarbonateGrainSize.h"
#include "GraphicColumnWidget.h"
#include "Profile.h"
#include "SedimentStructure.h"
#include "CustomSymbol.h"
#include "GraphicColumnBody.h"
#include "Color.h"
#include "Settings.h"
#include "Facies.h"
#include "OutcropQuality.h"
#include "LithologicalUnit.h"
#include "BedItemModel.h"
#include "MainWindow.h"

GraphicBedItem::GraphicBedItem(QGraphicsItem* p, GraphicColumnHeader* header, Bed* bed)
: QGraphicsRectItem(p),
_header(header),
_bed(bed),
_isSelected(false),
_leftLineStartX(0),
_leftLineEndX(0),
_rightLineStartX(0),
_rightLineEndX(0) {
    QPen pen;
    pen.setColor(Qt::white);
    pen.setWidth(0);
    setPen(pen);

    _sf = new SymbolFactory(this);
    _font.setPointSize(10);

    if (bed->hasValidHeight()) {
        setRect(0, 0,
                header->rect().width(),
                bed->getHeight()->getValue()
                * bed->getHeight()->getUnit()->getMilliMetre()
                * bed->getProfile()->getScaleFactor());
    } else {
        setRect(0, 0, header->rect().width(), 0);
    }

    if (_bed->getProfile()->getShowBedNumbers()) {
        drawBedNumber();
    }

    if (_bed->getProfile()->getShowLithology()) {
        drawLithology();
    }

    if (_bed->getProfile()->getShowGrainSize()) {
        drawGrainSize();
    }

    if (_bed->getProfile()->getShowFossils()) {
        drawFossils();
    }

    if (_bed->getProfile()->getShowSedimentStructures()) {
        drawSedimentStructures();
    }

    if (_bed->getProfile()->getShowCustomSymbols()) {
        drawCustomSymbols();
    }

    if (_bed->getProfile()->getShowNotes()) {
        drawNotes();
    }

    if (_bed->getProfile()->getShowColor()) {
        drawColor();
    }

    if (_bed->getProfile()->getShowFacies()) {
        drawFacies();
    }

    if (_bed->getProfile()->getShowLithologicalUnit()) {
        drawLithologicalUnit();
    }

    if (_bed->getProfile()->getShowOutcropQuality()) {
        drawOutcropQuality();
    }

    // always draw a line - which on is decided in drawTopBoundary()
    drawTopBoundary();
}

GraphicBedItem::~GraphicBedItem() {
    delete _sf;
}

void GraphicBedItem::select() {
    _isSelected = true;
}

void GraphicBedItem::deselect() {
    _isSelected = false;
}

void GraphicBedItem::drawBedNumber() {
    QGraphicsTextItem* itm = new QGraphicsTextItem(this);

    itm->setFont(_font);
    itm->setHtml(QObject::tr("Bed %1: %2").arg(_bed->getPosition()).arg(_bed->getFormattedHeight()));
    itm->setPos(_header->getWidthPosition(GraphicColumnHeader::BedEnd) - itm->boundingRect().width(),
            rect().height() / 2 - itm->boundingRect().height() / 2);
}

void GraphicBedItem::drawLithology() {
    QBrush b;
    QPen p;
    QString dir = (static_cast<ProfileLogger*> (QApplication::instance()))->getSettings()->getLithologiesPatternPath();
    QGraphicsRectItem* r = new QGraphicsRectItem(this);

    p.setColor(Qt::black);
    b.setStyle(Qt::SolidPattern);
    //r->setPen(p);

    if (_bed->hasLithology()) {
        r->setBrush((static_cast<ProfileLogger*> (QApplication::instance()))->getBrushFromFileName(dir, _bed->getLithology()->getFileName()));
    }

    r->setRect(0, 0,
            _header->getWidthPosition(GraphicColumnHeader::LithologyEnd) -
            _header->getWidthPosition(GraphicColumnHeader::LithologyStart),
            rect().height());
    r->setPos(_header->getWidthPosition(GraphicColumnHeader::LithologyStart), 0);
}

void GraphicBedItem::drawFacies() {
    QBrush b;
    QPen p;
    QString dir = (static_cast<ProfileLogger*> (QApplication::instance()))->getSettings()->getFaciesPath();
    QGraphicsRectItem* r = new QGraphicsRectItem(this);

    p.setColor(Qt::black);
    b.setStyle(Qt::SolidPattern);
    r->setPen(p);

    if (_bed->hasFacies()) {
        r->setBrush((static_cast<ProfileLogger*> (QApplication::instance()))->getBrushFromFileName(dir, _bed->getFacies()->getFileName()));
    }

    r->setRect(0, 0,
            _header->getWidthPosition(GraphicColumnHeader::FaciesEnd) -
            _header->getWidthPosition(GraphicColumnHeader::FaciesStart),
            rect().height());
    r->setPos(_header->getWidthPosition(GraphicColumnHeader::FaciesStart), 0);
}

void GraphicBedItem::drawOutcropQuality() {
    QBrush b;
    QPen p;
    QString dir = (static_cast<ProfileLogger*> (QApplication::instance()))->getSettings()->getOutcropQualitiesPath();
    QGraphicsRectItem* r = new QGraphicsRectItem(this);

    p.setColor(Qt::black);
    b.setStyle(Qt::SolidPattern);
    r->setPen(p);

    if (_bed->hasOutcropQuality()) {
        r->setBrush((static_cast<ProfileLogger*> (QApplication::instance()))->getBrushFromFileName(dir, _bed->getOutcropQuality()->getFileName()));
    }

    r->setRect(0, 0,
            _header->getWidthPosition(GraphicColumnHeader::OutcropQualityEnd) -
            _header->getWidthPosition(GraphicColumnHeader::OutcropQualityStart),
            rect().height());
    r->setPos(_header->getWidthPosition(GraphicColumnHeader::OutcropQualityStart), 0);
}

void GraphicBedItem::drawGrainSize() {
    QPolygon poly;
    QBrush b;

    QString dir = (static_cast<ProfileLogger*> (QApplication::instance()))->getSettings()->getBeddingTypesPatternPath();

    QGraphicsPolygonItem* r = new QGraphicsPolygonItem(this);
    b.setStyle(Qt::SolidPattern);

    int bottomX = 0;
    int topX = 0;

    if (_bed->hasClasticGrainSizeMode()) {
        int startX = _header->getWidthPosition(GraphicColumnHeader::NoClasticGrainsStart);

        if (_bed->hasBaseClasticGrainSize()) {
            bottomX = _header->getWidthPosition(_bed->getBaseClasticGrainSize()->getPosition()) - startX;
            topX = bottomX;
        }
        if (_bed->hasTopClasticGrainSize()) {
            topX = _header->getWidthPosition(_bed->getTopClasticGrainSize()->getPosition()) - startX;
        }
    }

    if (_bed->hasCarbonateGrainSizeMode()) {
        int startX = _header->getWidthPosition(GraphicColumnHeader::EvaporiteStart);
        if (_bed->hasBaseCarbonateGrainSize()) {
            bottomX = _header->getWidthPosition(_bed->getBaseCarbonateGrainSize()->getPosition()) - startX;
            topX = bottomX;
        }
        if (_bed->hasTopCarbonateGrainSize()) {
            topX = _header->getWidthPosition(_bed->getTopCarbonateGrainSize()->getPosition()) - startX;
        }
    }

    poly.append(QPoint(0, 0)); // top left
    poly.append(QPoint(0, (int) rect().height())); // bottom left
    poly.append(QPoint(bottomX, (int) rect().height())); // bottom right
    poly.append(QPoint(topX, 0)); // to be calculated: top right

    r->setPolygon(poly);

    r->setPos(_header->getWidthPosition(GraphicColumnHeader::EvaporiteStart), 0);

    if (_bed->hasBeddingType() && _bed->getProfile()->getShowBeddingType()) {
        r->setBrush((static_cast<ProfileLogger*> (QApplication::instance()))->getBrushFromFileName(dir, _bed->getBeddingType()->getFileName()));
    }

    QPen pen;
    pen.setColor(Qt::darkGray);
    pen.setStyle(Qt::SolidLine);
    r->setPen(pen);
}

void GraphicBedItem::drawFossils() {
    if (_bed->getFossilCount() < 1) {
        return;
    }

    int i = 0;

    int maxSize = ((_header->getWidthPosition(GraphicColumnHeader::FossilsEnd)
            - _header->getWidthPosition(GraphicColumnHeader::FossilsStart))) / _bed->getFossilCount();

    if (maxSize > rect().height()) {
        maxSize = (int) (rect().height());
    }

    if (maxSize > _bed->getProfile()->getMaxSymbolSize()) {
        maxSize = (int) (_bed->getProfile()->getMaxSymbolSize());
    }

    int yPos = (int) ((rect().height() - maxSize) / 2);

    for (QList<Fossil*>::iterator it = _bed->getFirstFossil(); it != _bed->getLastFossil(); it++) {
        Fossil* f = *it;
        GraphicSvgItem* itm = _sf->make(f, maxSize);
        if (itm) {
            itm->setPos(_header->getWidthPosition(GraphicColumnHeader::FossilsStart) + i * maxSize, yPos);
            i++;
        }
    }
}

void GraphicBedItem::drawSedimentStructures() {
    if (_bed->getSedimentStructureCount() < 1) {
        return;
    }

    int i = 0;

    int maxSize = ((_header->getWidthPosition(GraphicColumnHeader::SedimentStructuresEnd)
            - _header->getWidthPosition(GraphicColumnHeader::SedimentStructuresStart))) / _bed->getSedimentStructureCount();

    if (maxSize > rect().height()) {
        maxSize = (int) (rect().height());
    }

    if (maxSize > _bed->getProfile()->getMaxSymbolSize()) {
        maxSize = (int) (_bed->getProfile()->getMaxSymbolSize());
    }

    int yPos = (int) ((rect().height() - maxSize) / 2);

    for (QList<SedimentStructure*>::iterator it = _bed->getFirstSedimentStructure(); it != _bed->getLastSedimentStructure(); it++) {
        SedimentStructure* f = *it;
        GraphicSvgItem* itm = _sf->make(f, maxSize);
        if (itm) {
            itm->setPos(_header->getWidthPosition(GraphicColumnHeader::SedimentStructuresStart) + i * maxSize, yPos);
            i++;
        }
    }
}

void GraphicBedItem::drawCustomSymbols() {
    if (_bed->getCustomSymbolCount() < 1) {
        return;
    }

    int i = 0;

    int maxSize = ((_header->getWidthPosition(GraphicColumnHeader::CustomSymbolsEnd)
            - _header->getWidthPosition(GraphicColumnHeader::CustomSymbolsStart))) / _bed->getCustomSymbolCount();

    int yPos = (int) ((rect().height() - maxSize) / 2);

    if (maxSize > rect().height()) {
        maxSize = (int) (rect().height());
    }

    if (maxSize > _bed->getProfile()->getMaxSymbolSize()) {
        maxSize = (int) (_bed->getProfile()->getMaxSymbolSize());
    }

    for (QList<CustomSymbol*>::iterator it = _bed->getFirstCustomSymbol(); it != _bed->getLastCustomSymbol(); it++) {
        CustomSymbol* f = *it;
        GraphicSvgItem* itm = _sf->make(f, maxSize);
        if (itm) {
            itm->setPos(_header->getWidthPosition(GraphicColumnHeader::CustomSymbolsStart) + i * maxSize, yPos);
            i++;
        }
    }
}

void GraphicBedItem::drawTopBoundary() {
    if (!_bed->hasTopBoundaryType() || (!_bed->getProfile()->getShowTopBoundaryType())) {
        QGraphicsLineItem* line = new QGraphicsLineItem(0, 0,
                _header->getWidthPosition(GraphicColumnHeader::ColumnEnd), 0);
        QPen p;
        p.setWidth(1);
        p.setColor(Qt::black);
        p.setStyle(Qt::SolidLine);
        line->setPen(p);
        
        return;
    }

    GraphicSvgItem* itm = _sf->make(_bed->getTopBoundaryType(),
            _header->getWidthPosition(GraphicColumnHeader::ColumnEnd)
            - _header->getWidthPosition(GraphicColumnHeader::ColumnStart));

    if (!itm) {
        return;
    }

    itm->setPos(0, 0);
}

void GraphicBedItem::drawNotes() {
    QGraphicsTextItem* itm = new QGraphicsTextItem(this);
    itm->setFont(_font);

    itm->setHtml(_bed->getDescription().replace("\n", "<br/>\n"));

    itm->setPos(_header->getWidthPosition(GraphicColumnHeader::NotesStart), rect().height() / 2);
}

void GraphicBedItem::drawLithologicalUnit() {
    if (!_bed->hasLithologicalUnit()) {
        return;
    }
    QGraphicsTextItem* itm = new QGraphicsTextItem(this);
    itm->setFont(_font);

    itm->setHtml(_bed->getLithologicalUnit()->getName());

    itm->setPos(_header->getWidthPosition(GraphicColumnHeader::LithologicalUnitStart),
            rect().height() / 2);
}

void GraphicBedItem::drawColor() {
    QBrush b;
    if (_bed->hasColor()) {
        b.setStyle(_bed->getColor()->getBrushStyle());
    }

    QGraphicsRectItem* r = new QGraphicsRectItem(this);
    r->setRect(0, 0, _header->getWidthPosition(GraphicColumnHeader::ColorEnd) - _header->getWidthPosition(GraphicColumnHeader::ColorStart), rect().height());
    r->setBrush(b);
    r->setPos(_header->getWidthPosition(GraphicColumnHeader::ColorStart), 0);
}

void GraphicBedItem::contextMenuEvent(QGraphicsSceneContextMenuEvent* e) {
    ProfileLogger* app = (static_cast<ProfileLogger*> (QApplication::instance()));
    BedItemModel* bedsM = app->getBedItemModel();
    bedsM->setCurrentBed(_bed);

    QMenu* m = new QMenu((static_cast<ProfileLogger*> (QApplication::instance()))->getMainWindow());

    m->addAction(app->getReloadBedsAction());
    m->insertSeparator(app->getCreateBedOnTopAction());
    m->addAction(app->getCreateBedOnTopAction());
    m->addAction(app->getCreateBedAboveCurrentBedAction());
    m->addAction(app->getCreateBedBelowCurrentBedAction());
    m->insertSeparator(app->getEditBedAction());
    m->addAction(app->getEditBedAction());
    m->addAction(app->getMoveBedUpAction());
    m->addAction(app->getMoveBedDownAction());
    m->addAction(app->getDuplicateBedAndInsertAtTopAction());
    m->insertSeparator(app->getSplitProfileAtBedAction());
    m->addAction(app->getSplitProfileAtBedAction());
    m->addAction(app->getInsertProfileAboveBedAction());
    //m->addAction(app->getInsertProfileBelowBedAction());
    m->insertSeparator(app->getDeleteBedAction());
    m->addAction(app->getDeleteBedAction());
    m->addAction(app->getDeleteBedsAboveBedAction());
    m->addAction(app->getDeleteBedsBelowBelowAction());

    m->insertSeparator(app->getExportProfileToSvgAction());
    m->addAction(app->getExportProfileToSvgAction());
    m->addAction(app->getExportProfileToPdfAction());
    m->addAction(app->getExportProfileToJpgAction());
    m->addAction(app->getExportProfileToPngAction());
    m->addAction(app->getExportProfileToTiffAction());

    m->exec(e->screenPos());
}
