/* 
 * File:   GraphicColumnHeader.cpp
 * Author: jolo
 * 
 * Created on 16. Dezember 2009, 14:19
 */

#include "GraphicColumnHeader.h"

#include <QGraphicsScene>
#include <QPen>
#include <QObject>
#include <QApplication>
#include <QMenu>
#include <QAction>
#include <QGraphicsSceneContextMenuEvent>

#include "GraphicColumnBody.h"
#include "Profile.h"
#include "ProfileLogger.h"
#include "BedItemModel.h"
#include "MainWindow.h"

GraphicColumnHeader::GraphicColumnHeader(QGraphicsItem* p)
: QGraphicsRectItem(p),
_unit(0) {
    _pen.setColor(Qt::black);
    _pen.setWidth(1);
}

GraphicColumnHeader::~GraphicColumnHeader() {
}

void GraphicColumnHeader::drawContent() {
    drawBoundingBox();

    if (_profile->getShowHeight()) {
        drawHeightBox();
    }

    if (_profile->getShowBedNumbers()) {
        drawBedBox();
    }

    if (_profile->getShowLithology()) {
        drawLithologyBox();
    }

    if (_profile->getShowGrainSize()) {
        drawGrainSizesBox();
    }

    if (_profile->getShowColor()) {
        drawColorBox();
    }

    if (_profile->getShowFacies()) {
        drawFaciesBox();
    }

    if (_profile->getShowLithologicalUnit()) {
        drawLithologicalUnitsBox();
    }

    if (_profile->getShowOutcropQuality()) {
        drawOutcropQualitiesBox();
    }

    if (_profile->getShowFossils()) {
        drawFossilsBox();
    }

    if (_profile->getShowSedimentStructures()) {
        drawSedimentStructuresBox();
    }

    if (_profile->getShowCustomSymbols()) {
        drawCustomSymbolsBox();
    }

    if (_profile->getShowNotes()) {
        drawNotesBox();
    }
}

void GraphicColumnHeader::drawBoundingBox() {
    setRect(0, 0, _w[ColumnEnd], 2 * _unit);
    setPen(_pen);
}

void GraphicColumnHeader::drawHeightBox() {
    drawText(QPoint(_w[HeightStart], (int) (rect().height()) / 2), QObject::tr("Height"));
    drawLine(QPoint(_w[HeightEnd], 0), QPoint(_w[HeightEnd], (int) (rect().height())), _pen);
}

void GraphicColumnHeader::drawBedBox() {
    drawText(QPoint(_w[BedStart], (int) (rect().height()) / 2), QObject::tr("Bed"));
    drawLine(QPoint(_w[BedEnd], 0), QPoint(_w[BedEnd], (int) (rect().height())), _pen);
}

void GraphicColumnHeader::drawLithologyBox() {
    drawText(QPoint(_w[LithologyStart], (int) (rect().height()) / 2), QObject::tr("Lithology"));
    drawLine(QPoint(_w[LithologyEnd], 0), QPoint(_w[LithologyEnd], (int) (rect().height())), _pen);
}

void GraphicColumnHeader::drawFaciesBox() {
    drawLine(QPoint(_w[FaciesStart], 0), QPoint(_w[FaciesStart], (int) (rect().height())), _pen);
    drawText(QPoint(_w[FaciesStart], (int) (rect().height())), QObject::tr("Facies"))->rotate(-90);
    drawLine(QPoint(_w[FaciesEnd], 0), QPoint(_w[FaciesEnd], (int) (rect().height())), _pen);
}

void GraphicColumnHeader::drawOutcropQualitiesBox() {
    drawLine(QPoint(_w[OutcropQualityStart], 0), QPoint(_w[OutcropQualityStart], (int) (rect().height())), _pen);
    drawText(QPoint(_w[OutcropQualityStart], (int) (rect().height())),
            QObject::tr("Quality"))->rotate(-90);
    drawLine(QPoint(_w[OutcropQualityEnd], 0), QPoint(_w[OutcropQualityEnd], (int) (rect().height())), _pen);
}

void GraphicColumnHeader::drawGrainSizesBox() {
    drawLine(QPoint(_w[EvaporiteStart], (int) (rect().height()) / 2),
            QPoint(_w[BlocksEnd], (int) (rect().height()) / 2), _pen);

    drawClasticsBox();
    drawCarbonatesBox();
}

void GraphicColumnHeader::drawClasticsBox() {
    int x = 0;
    int yStart = (int) (rect().height()) / 2;
    int yEnd = (int) (rect().height());

    drawText(QPoint(_w[NoClasticGrainsStart], yStart), QObject::tr("None"));
    x = _w[NoClasticGrainsEnd];
    drawLine(QPoint(x, yStart), QPoint(x, yEnd), _pen);

    drawText(QPoint(_w[ClayStart], yStart), QObject::tr("Clay"));
    x = _w[ClayEnd];
    drawLine(QPoint(x, yStart), QPoint(x, yEnd), _pen);

    drawText(QPoint(_w[FineSiltStart], yStart), QObject::tr("fs"));
    x = _w[FineSiltEnd];
    drawLine(QPoint(x, yStart), QPoint(x, yEnd), _pen);

    drawText(QPoint(_w[MediumSiltStart], yStart), QObject::tr("ms"));
    x = _w[MediumSiltEnd];
    drawLine(QPoint(x, yStart), QPoint(x, yEnd), _pen);

    drawText(QPoint(_w[CoarseSiltStart], yStart), QObject::tr("cs"));
    x = _w[CoarseSiltEnd];
    drawLine(QPoint(x, yStart), QPoint(x, yEnd), _pen);


    drawText(QPoint(_w[FineSandStart], yStart), QObject::tr("fS"));
    x = _w[FineSandEnd];
    drawLine(QPoint(x, yStart), QPoint(x, yEnd), _pen);

    drawText(QPoint(_w[MediumSandStart], yStart), QObject::tr("mS"));
    x = _w[MediumSandEnd];
    drawLine(QPoint(x, yStart), QPoint(x, yEnd), _pen);

    drawText(QPoint(_w[CoarseSandStart], yStart), QObject::tr("cS"));
    x = _w[CoarseSandEnd];
    drawLine(QPoint(x, yStart), QPoint(x, yEnd), _pen);

    drawText(QPoint(_w[FineGravelStart], yStart), QObject::tr("fG"));
    x = _w[FineGravelEnd];
    drawLine(QPoint(x, yStart), QPoint(x, yEnd), _pen);

    drawText(QPoint(_w[MediumGravelStart], yStart), QObject::tr("mG"));
    x = _w[MediumGravelEnd];
    drawLine(QPoint(x, yStart), QPoint(x, yEnd), _pen);

    drawText(QPoint(_w[CoarseGravelStart], yStart), QObject::tr("cG"));
    x = _w[CoarseGravelEnd];
    drawLine(QPoint(x, yStart), QPoint(x, yEnd), _pen);

    drawText(QPoint(_w[CobblesStart], yStart), QObject::tr("C"));
    x = _w[CobblesEnd];
    drawLine(QPoint(x, yStart), QPoint(x, yEnd), _pen);

    drawText(QPoint(_w[BlocksStart], yStart), QObject::tr("B"));
    x = _w[BlocksEnd];
    drawLine(QPoint(x, yStart), QPoint(x, yEnd), _pen);
}

void GraphicColumnHeader::drawCarbonatesBox() {
    int x = 0;
    int yStart = 0;
    int yEnd = (int) (rect().height()) / 2;

    drawText(QPoint(_w[EvaporiteStart], yStart), QObject::tr("Evaporite"));
    x = _w[EvaporiteEnd];
    drawLine(QPoint(x, yStart), QPoint(x, yEnd), _pen);

    drawText(QPoint(_w[MudstoneStart], yStart), QObject::tr("M"));
    x = _w[MudstoneEnd];
    drawLine(QPoint(x, yStart), QPoint(x, yEnd), _pen);

    drawText(QPoint(_w[WackestoneStart], yStart), QObject::tr("W"));
    x = _w[WackestoneEnd];
    drawLine(QPoint(x, yStart), QPoint(x, yEnd), _pen);

    drawText(QPoint(_w[PackstoneStart], yStart), QObject::tr("P"));
    x = _w[PackstoneEnd];
    drawLine(QPoint(x, yStart), QPoint(x, yEnd), _pen);

    drawText(QPoint(_w[GrainstoneStart], yStart), QObject::tr("G"));
    x = _w[GrainstoneEnd];
    drawLine(QPoint(x, yStart), QPoint(x, yEnd), _pen);

    drawText(QPoint(_w[RudstoneStart], yStart), QObject::tr("R"));
    x = _w[RudstoneEnd];
    drawLine(QPoint(x, yStart), QPoint(x, yEnd), _pen);
}

void GraphicColumnHeader::drawColorBox() {
    drawLine(QPoint(_w[ColorStart], 0), QPoint(_w[ColorStart], (int) (rect().height())), _pen);
    drawText(QPoint(_w[ColorStart], (int) (rect().height())), QObject::tr("Color"))->rotate(-90);
    drawLine(QPoint(_w[ColorEnd], 0), QPoint(_w[ColorEnd], (int) (rect().height())), _pen);
}

void GraphicColumnHeader::drawFossilsBox() {
    drawText(QPoint(_w[FossilsStart], (int) (rect().height()) / 2), QObject::tr("Fossils"));
    drawLine(QPoint(_w[FossilsEnd], 0), QPoint(_w[FossilsEnd], (int) (rect().height())), _pen);
}

void GraphicColumnHeader::drawSedimentStructuresBox() {
    drawText(QPoint(_w[SedimentStructuresStart], 0), QObject::tr("Sediment<br/>Structures"));
    drawLine(QPoint(_w[SedimentStructuresEnd], 0),
            QPoint(_w[SedimentStructuresEnd],
            (int) (rect().height())), _pen);
}

void GraphicColumnHeader::drawCustomSymbolsBox() {
    drawText(QPoint(_w[CustomSymbolsStart], 0), QObject::tr("Custom<br/>Symbols"));
    drawLine(QPoint(_w[CustomSymbolsEnd], 0), QPoint(_w[CustomSymbolsEnd],
            (int) (rect().height())), _pen);
}

void GraphicColumnHeader::drawNotesBox() {
    drawText(QPoint(_w[NotesStart], (int) (rect().height()) / 2), QObject::tr("Notes"));
    drawLine(QPoint(_w[NotesEnd], 0), QPoint(_w[NotesEnd],
            (int) (rect().height())), _pen);
}

void GraphicColumnHeader::drawLithologicalUnitsBox() {
    drawText(QPoint(_w[LithologicalUnitStart], 0), QObject::tr("Lithological<br/>Unit"));
    drawLine(QPoint(_w[LithologicalUnitEnd], 0), QPoint(_w[LithologicalUnitEnd],
            (int) (rect().height())), _pen);
}

QGraphicsLineItem* GraphicColumnHeader::drawLine(const QPoint& begin, const QPoint& end, const QPen& pen) {
    QGraphicsLineItem* l = new QGraphicsLineItem(this);
    l->setPen(pen);
    l->setLine(QLineF(begin, end));
    return l;
}

QGraphicsTextItem* GraphicColumnHeader::drawText(const QPoint& pos, const QString& txt) {
    QFont f;
    f.setPointSize(12);
    f.setWeight(QFont::Bold);

    QGraphicsTextItem* l = new QGraphicsTextItem(this);
    l->setFont(f);
    l->setHtml(txt);
    l->setPos(pos);
    //    l->rotate(-90);
    return l;
}

void GraphicColumnHeader::setupWidths() {
    _w[ColumnStart] = 0;
    _w[ColumnEnd] = _w[ColumnStart];

    if (_profile->getShowHeight()) {
        _w[HeightStart] = _w[ColumnEnd];
        _w[HeightEnd] = _w[HeightStart] + 3 * _unit;
        _w[ColumnEnd] = _w[HeightEnd];
    }

    if (_profile->getShowBedNumbers()) {
        _w[BedStart] = _w[ColumnEnd];
        _w[BedEnd] = _w[BedStart] + 3 * _unit;
        _w[ColumnEnd] = _w[BedEnd];
    }

    if (_profile->getShowLithology()) {
        _w[LithologyStart] = _w[ColumnEnd];
        _w[LithologyEnd] = _w[LithologyStart] + 4 * _unit;
        _w[ColumnEnd] = _w[LithologyEnd];
    }

    if (_profile->getShowGrainSize()) {
        _w[NoClasticGrainsStart] = _w[ColumnEnd];
        _w[NoClasticGrainsEnd] = _w[NoClasticGrainsStart] + 3 * _unit;
        _w[ClayStart] = _w[NoClasticGrainsEnd];
        _w[ClayEnd] = _w[ClayStart] + 3 * _unit;

        _w[SiltStart] = _w[ClayEnd];
        _w[FineSiltStart] = _w[SiltStart];
        _w[FineSiltEnd] = _w[FineSiltStart] + _unit;
        _w[MediumSiltStart] = _w[FineSiltEnd];
        _w[MediumSiltEnd] = _w[MediumSiltStart] + _unit;
        _w[CoarseSiltStart] = _w[MediumSiltEnd];
        _w[CoarseSiltEnd] = _w[CoarseSiltStart] + _unit;
        _w[SiltEnd] = _w[CoarseSiltEnd];

        _w[SandStart] = _w[SiltEnd];
        _w[FineSandStart] = _w[SandStart];
        _w[FineSandEnd] = _w[FineSandStart] + _unit;
        _w[MediumSandStart] = _w[FineSandEnd];
        _w[MediumSandEnd] = _w[MediumSandStart] + _unit;
        _w[CoarseSandStart] = _w[MediumSandEnd];
        _w[CoarseSandEnd] = _w[CoarseSandStart] + _unit;
        _w[SandEnd] = _w[CoarseSandEnd];

        _w[GravelStart] = _w[SandEnd];
        _w[FineGravelStart] = _w[GravelStart];
        _w[FineGravelEnd] = _w[FineGravelStart] + _unit;
        _w[MediumGravelStart] = _w[FineGravelEnd];
        _w[MediumGravelEnd] = _w[MediumGravelStart] + _unit;
        _w[CoarseGravelStart] = _w[MediumGravelEnd];
        _w[CoarseGravelEnd] = _w[CoarseGravelStart] + _unit;
        _w[GravelEnd] = _w[CoarseGravelEnd];

        _w[CobblesStart] = _w[GravelEnd];
        _w[CobblesEnd] = _w[CobblesStart] + _unit;

        _w[BlocksStart] = _w[CobblesEnd];
        _w[BlocksEnd] = _w[BlocksStart] + _unit;

        _w[EvaporiteStart] = _w[NoClasticGrainsStart];
        _w[EvaporiteEnd] = _w[NoClasticGrainsEnd];
        _w[MudstoneStart] = _w[EvaporiteEnd];
        _w[MudstoneEnd] = _w[SiltEnd];
        _w[WackestoneStart] = _w[MudstoneEnd];
        _w[WackestoneEnd] = _w[FineSandEnd];
        _w[PackstoneStart] = _w[WackestoneEnd];
        _w[PackstoneEnd] = _w[MediumSandEnd];
        _w[GrainstoneStart] = _w[PackstoneEnd];
        _w[GrainstoneEnd] = _w[CoarseSandEnd];
        _w[RudstoneStart] = _w[GrainstoneEnd];
        _w[RudstoneEnd] = _w[BlocksEnd];

        _w[ColumnEnd] = _w[BlocksEnd];
    }

    if (_profile->getShowColor()) {
        _w[ColorStart] = _w[ColumnEnd];
        _w[ColorEnd] = _w[ColorStart] + _unit;
        _w[ColumnEnd] = _w[ColorEnd];
    }

    if (_profile->getShowFacies()) {
        _w[FaciesStart] = _w[ColumnEnd];
        _w[FaciesEnd] = _w[FaciesStart] + _unit;
        _w[ColumnEnd] = _w[FaciesEnd];
    }

    if (_profile->getShowLithologicalUnit()) {
        _w[LithologicalUnitStart] = _w[ColumnEnd];
        _w[LithologicalUnitEnd] = _w[LithologicalUnitStart] + 4 * _unit;
        _w[ColumnEnd] = _w[LithologicalUnitEnd];
    }

    if (_profile->getShowOutcropQuality()) {
        _w[OutcropQualityStart] = _w[ColumnEnd];
        _w[OutcropQualityEnd] = _w[OutcropQualityStart] + _unit;
        _w[ColumnEnd] = _w[OutcropQualityEnd];
    }

    if (_profile->getShowFossils()) {
        _w[FossilsStart] = _w[ColumnEnd];
        _w[FossilsEnd] = _w[FossilsStart] + 4 * _unit;
        _w[ColumnEnd] = _w[FossilsEnd];
    }

    if (_profile->getShowSedimentStructures()) {
        _w[SedimentStructuresStart] = _w[ColumnEnd];
        _w[SedimentStructuresEnd] = _w[SedimentStructuresStart] + 4 * _unit;
        _w[ColumnEnd] = _w[SedimentStructuresEnd];
    }

    if (_profile->getShowCustomSymbols()) {
        _w[CustomSymbolsStart] = _w[ColumnEnd];
        _w[CustomSymbolsEnd] = _w[CustomSymbolsStart] + 4 * _unit;
        _w[ColumnEnd] = _w[CustomSymbolsEnd];
    }

    if (_profile->getShowNotes()) {
        _w[NotesStart] = _w[ColumnEnd];
        _w[NotesEnd] = _w[NotesStart] + 12 * _unit;
        _w[ColumnEnd] = _w[NotesEnd];
    }
}

void GraphicColumnHeader::setProfile(Profile* p) {
    _profile = p;

    if (!_profile) {
        return;
    }

    _unit = 30; // _profile->getCellSize();
    setupWidths();
    drawContent();
}

void GraphicColumnHeader::contextMenuEvent(QGraphicsSceneContextMenuEvent* e) {
    ProfileLogger* app = (static_cast<ProfileLogger*> (QApplication::instance()));
    BedItemModel* bedsM = app->getBedItemModel();
    bedsM->setCurrentBed(0);

    QMenu* m = new QMenu((static_cast<ProfileLogger*> (QApplication::instance()))->getMainWindow());

    m->addAction(app->getReloadBedsAction());
    m->insertSeparator(app->getCreateBedOnTopAction());
    m->addAction(app->getCreateBedOnTopAction());

    m->insertSeparator(app->getExportProfileToSvgAction());
    m->addAction(app->getExportProfileToSvgAction());
    m->addAction(app->getExportProfileToPdfAction());
    m->addAction(app->getExportProfileToJpgAction());
    m->addAction(app->getExportProfileToPngAction());
    m->addAction(app->getExportProfileToTiffAction());

    m->exec(e->screenPos());
}
