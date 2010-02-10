/* 
 * File:   GraphicColumnBody.cpp
 * Author: jolo
 * 
 * Created on 16. Dezember 2009, 15:15
 */

#include "GraphicColumnBody.h"

#include <QPen>
#include <QGraphicsScene>

#include "GraphicColumnHeader.h"
#include "Profile.h"
#include "GraphicBedItem.h"
#include "Bed.h"
#include "LengthUnit.h"
#include "GraphicColumnWidget.h"
#include "GraphicLegendItem.h"

GraphicColumnBody::GraphicColumnBody(QGraphicsItem* p)
: QGraphicsRectItem(p),
_header(0),
_profile(0),
_unit(2) {
    setPen(QPen(Qt::black));

    _solidLinePen.setColor(Qt::gray);
    _solidLinePen.setStyle(Qt::SolidLine);

    _dashedLinePen.setColor(Qt::lightGray);
    _dashedLinePen.setStyle(Qt::DashLine);

    _dottedLinePen.setColor(Qt::lightGray);
    _dottedLinePen.setStyle(Qt::DotLine);

    _smallMarkFont.setPointSize(10);
    _bigMarkFont.setPointSize(12);
    _smallMarkColor = Qt::darkGray;
    _bigMarkColor = Qt::black;
    _smallMarkLinePen.setColor(_smallMarkColor);
    _smallMarkLinePen.setStyle(Qt::SolidLine);
    _smallMarkLinePen.setWidth(1);

    _bigMarkLinePen.setColor(_bigMarkColor);
    _bigMarkLinePen.setStyle(Qt::SolidLine);
    _bigMarkLinePen.setWidth(1);
}

GraphicColumnBody::~GraphicColumnBody() {
}

void GraphicColumnBody::drawHelpLines() {
    drawHelpLine(_header->getWidthPosition(GraphicColumnHeader::ColumnStart), _solidLinePen);

    if (_profile->getShowHeight()) {
        drawHelpLine(_header->getWidthPosition(GraphicColumnHeader::HeightStart), _solidLinePen);
        drawHelpLine(_header->getWidthPosition(GraphicColumnHeader::HeightEnd), _solidLinePen);
    }

    if (_profile->getShowBedNumbers()) {
        drawHelpLine(_header->getWidthPosition(GraphicColumnHeader::BedEnd), _solidLinePen);
    }

    if (_profile->getShowLithology()) {
        drawHelpLine(_header->getWidthPosition(GraphicColumnHeader::LithologyEnd), _solidLinePen);
    }

    if (_profile->getShowGrainSize()) {
        drawHelpLine(_header->getWidthPosition(GraphicColumnHeader::NoClasticGrainsEnd), _dashedLinePen);
        drawHelpLine(_header->getWidthPosition(GraphicColumnHeader::ClayEnd), _dashedLinePen);

        drawHelpLine(_header->getWidthPosition(GraphicColumnHeader::FineSiltEnd), _dottedLinePen);
        drawHelpLine(_header->getWidthPosition(GraphicColumnHeader::MediumSiltEnd), _dottedLinePen);
        drawHelpLine(_header->getWidthPosition(GraphicColumnHeader::CoarseSiltEnd), _dashedLinePen);

        drawHelpLine(_header->getWidthPosition(GraphicColumnHeader::FineSandEnd), _dottedLinePen);
        drawHelpLine(_header->getWidthPosition(GraphicColumnHeader::MediumSandEnd), _dottedLinePen);
        drawHelpLine(_header->getWidthPosition(GraphicColumnHeader::CoarseSandEnd), _dashedLinePen);

        drawHelpLine(_header->getWidthPosition(GraphicColumnHeader::FineGravelEnd), _dottedLinePen);
        drawHelpLine(_header->getWidthPosition(GraphicColumnHeader::MediumGravelEnd), _dottedLinePen);
        drawHelpLine(_header->getWidthPosition(GraphicColumnHeader::CoarseGravelEnd), _dashedLinePen);

        drawHelpLine(_header->getWidthPosition(GraphicColumnHeader::CobblesEnd), _dashedLinePen);
    }

    if (_profile->getShowColor()) {
        drawHelpLine(_header->getWidthPosition(GraphicColumnHeader::ColorStart), _solidLinePen);
        drawHelpLine(_header->getWidthPosition(GraphicColumnHeader::ColorEnd), _solidLinePen);
    }

    if (_profile->getShowFacies()) {
        drawHelpLine(_header->getWidthPosition(GraphicColumnHeader::FaciesEnd), _solidLinePen);
    }

    if (_profile->getShowLithologicalUnit()) {
        drawHelpLine(_header->getWidthPosition(GraphicColumnHeader::LithologicalUnitEnd), _solidLinePen);
    }

    if (_profile->getShowOutcropQuality()) {
        drawHelpLine(_header->getWidthPosition(GraphicColumnHeader::OutcropQualityEnd), _solidLinePen);
    }

    if (_profile->getShowFossils()) {
        drawHelpLine(_header->getWidthPosition(GraphicColumnHeader::FossilsEnd), _solidLinePen);
    }

    if (_profile->getShowSedimentStructures()) {
        drawHelpLine(_header->getWidthPosition(GraphicColumnHeader::SedimentStructuresEnd), _solidLinePen);
    }

    if (_profile->getShowCustomSymbols()) {
        drawHelpLine(_header->getWidthPosition(GraphicColumnHeader::CustomSymbolsEnd), _solidLinePen);
    }

    if (_profile->getShowNotes()) {
        drawHelpLine(_header->getWidthPosition(GraphicColumnHeader::NotesEnd), _solidLinePen);
    }

    drawHelpLine(_header->getWidthPosition(GraphicColumnHeader::ColumnEnd), _solidLinePen);
}

void GraphicColumnBody::drawHelpLine(int widthFromLeft, const QPen& pen) {
    drawLine(QPoint(widthFromLeft, 0),
            QPoint(widthFromLeft, (int) (rect().height())),
            pen);
}

void GraphicColumnBody::drawLine(const QPoint& start, const QPoint& end, const QPen& pen) {
    QGraphicsLineItem* l = new QGraphicsLineItem(this);
    l->setLine(QLineF(start, end));
    l->setPen(pen);
}

void GraphicColumnBody::setProfileAndHeader(Profile* p, GraphicColumnHeader* h) {
    _profile = p;
    _header = h;
    if (!_profile) {
        return;
    }

    if (!_header) {
        return;
    }

    setRect(0, 0, _header->rect().width(), _profile->getScaledHeight());
    setPos(0, _header->rect().height());

    _beds.clear();

    if (_profile->getShowHeightMarks()) {
        drawHeightMarks();
    }

    drawHelpLines();

    int lastBedBaseHeight = (int) (_profile->getScaledHeight());

    for (QList<Bed*>::iterator it = _profile->getFirstBed(); it != _profile->getLastBed(); it++) {
        Bed* b = (*it);
        int bedHeight = 10;

        if (b->getHeight()->hasUnit()) {
            bedHeight = (int) (b->getScaledHeight());
        }

        _beds.append(new GraphicBedItem(this, _header, *it));
        _beds.last()->setPos(0, lastBedBaseHeight - bedHeight);
        lastBedBaseHeight = (int) (_beds.last()->pos().y());
    }
}

GraphicBedItem* GraphicColumnBody::getItemForBed(Bed* b) {
    if (!b) {
        return 0;
    }

    for (int i = 0; i < _beds.size(); i++) {
        GraphicBedItem* itm = _beds.at(i);

        if (itm->getBed() == b) {
            return itm;
        }
    }

    return 0;
}

Bed* GraphicColumnBody::getBedFromItem(GraphicBedItem* itm) {
    if (!itm) {
        return 0;
    }

    for (QList<GraphicBedItem*>::iterator it = _beds.begin(); it != _beds.end(); it++) {
        if ((*it) == itm) {
            return (*it)->getBed();
        }
    }

    return 0;
}

void GraphicColumnBody::selectBed(Bed* b) {
    clearSelection();

    if (!b) {
        return;
    }

    GraphicBedItem* itm = getItemForBed(b);

    if (!itm) {
        return;
    }

    itm->select();
    _selectedItems.append(itm);
}

void GraphicColumnBody::clearSelection() {
    for (QList<GraphicBedItem*>::iterator it = _selectedItems.begin(); it != _selectedItems.end(); it++) {
        GraphicBedItem* itm = *it;
        if (itm) {
            itm->deselect();
        }
    }

    _selectedItems.clear();
}

void GraphicColumnBody::drawHeightMarks() {
    int realHeight = _profile->getHeightInMillimetres(); // in mm

    int currHeight = 0;

    do {
        drawBigHeightMark(currHeight, QString("%1 mm").arg(currHeight));
        currHeight += _profile->getBigMarksDistance()->getMillimetres();
    } while (currHeight <= realHeight - 1);

    currHeight = _profile->getSmallMarksDistance()->getMillimetres(); // skip 0 height - there is a big mark.

    do {
        drawSmallHeightMark(currHeight);
        currHeight += _profile->getSmallMarksDistance()->getMillimetres();
    } while (currHeight <= realHeight - 1);
}

void GraphicColumnBody::drawBigHeightMark(int height, const QString& value) {
    QGraphicsLineItem* mark = new QGraphicsLineItem(this);
    mark->setPen(_bigMarkLinePen);

    QGraphicsTextItem* txt = new QGraphicsTextItem(this);
    txt->setFont(_bigMarkFont);
    txt->setHtml(value);

    int y = (int) (rect().height() - height * _profile->getScaleFactor());

    mark->setLine(-5, 0, 0, 0);
    mark->setPos(_header->getWidthPosition(GraphicColumnHeader::ColumnStart), y);

    txt->setPos(mark->pos().x() - txt->boundingRect().width() - 5,
            y - (txt->boundingRect().height() / 2));

}

void GraphicColumnBody::drawSmallHeightMark(int height) {
    QGraphicsLineItem* mark = new QGraphicsLineItem(this);
    mark->setPen(_smallMarkLinePen);

    QGraphicsTextItem* txt = new QGraphicsTextItem(this);
    txt->setFont(_smallMarkFont);
    txt->setHtml(QString::number(height));

    int y = (int) (rect().height() - height * _profile->getScaleFactor());

    mark->setLine(0, 0, 5, 0);
    mark->setPos(_header->getWidthPosition(GraphicColumnHeader::ColumnStart), y);

    txt->setPos(mark->pos().x() - txt->boundingRect().width() - 5,
            y - (txt->boundingRect().height() / 2));
}
