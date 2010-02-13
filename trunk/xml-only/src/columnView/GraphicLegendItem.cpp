/* 
 * File:   GraphicLegendItem.cpp
 * Author: jolo
 * 
 * Created on 13. Januar 2010, 15:32
 */

#include "GraphicLegendItem.h"

#include <QGraphicsSceneContextMenuEvent>
#include <QList>
#include <QApplication>
#include <QMenu>

#include "GraphicColumnHeader.h"
#include "LithologyLegendItem.h"
#include "BeddingTypeLegendItem.h"
#include "ColorLegendItem.h"
#include "FossilLegendItem.h"
#include "SedimentStructureLegendItem.h"
#include "CustomSymbolLegendItem.h"
#include "BoundaryTypeLegendItem.h"
#include "ProfileLogger.h"
#include "Project.h"
#include "LithologyItemModel.h"
#include "GraphicColumnWidget.h"
#include "Profile.h"
#include "Facies.h"
#include "FaciesLegendItem.h"
#include "OutcropQualityLegendItem.h"
#include "ProfileLogger.h"
#include "BedItemModel.h"
#include "MainWindow.h"

GraphicLegendItem::GraphicLegendItem()
: QGraphicsRectItem(),
_profile(0),
_header(0),
_currHeight(0),
_titleSep(10),
_itemWidth(0),
_itemHeight(0),
_colCount(8) {
    _pen.setColor(Qt::black);
    _pen.setStyle(Qt::SolidLine);
    _pen.setWidth(1);

    _font.setPointSize(12);
    _font.setWeight(QFont::Bold);

    setPen(_pen);
}

GraphicLegendItem::~GraphicLegendItem() {
}

void GraphicLegendItem::addTitle(const QString& s) {
    QGraphicsTextItem* titleItm = new QGraphicsTextItem(this);
    titleItm->setHtml(s);
    titleItm->setPos(_titleSep, _currHeight + _titleSep);
    titleItm->setFont(_font);
    _currHeight += _titleSep + (int)(titleItm->boundingRect().height()) + _titleSep;

}

void GraphicLegendItem::drawLithologies() {
    Project* p = (static_cast<ProfileLogger*> (QApplication::instance()))->getProject();

    if (!p) {
        return;
    }

    addTitle(QObject::tr("Lithologies"));

    if (p->getLithologyCount() > 0) {
        int currCol = 0;

        for (QList<Lithology*>::iterator it = p->getFirstLithology();
                it != p->getLastLithology();
                it++) {
            LithologyLegendItem* itm = new LithologyLegendItem(this, *it,
                    _itemWidth, _itemHeight);

            if (itm) {
                itm->setPos(currCol * itm->rect().width(), _currHeight);
                currCol++;

                if (currCol >= _colCount) {
                    currCol = 0;
                    _currHeight += _itemHeight;
                }
            }
        }

        if (currCol <= _colCount) {
            _currHeight += _itemHeight;
        }
    }
}

void GraphicLegendItem::drawOutcropQualities() {
    Project* p = (static_cast<ProfileLogger*> (QApplication::instance()))->getProject();

    if (!p) {
        return;
    }

    addTitle(QObject::tr("Outcrop Qualities"));

    if (p->getOutcropQualityCount() > 0) {
        int currCol = 0;

        for (QList<OutcropQuality*>::iterator it = p->getFirstOutcropQuality();
                it != p->getLastOutcropQuality();
                it++) {
            OutcropQualityLegendItem* itm = new OutcropQualityLegendItem(this, *it,
                    _itemWidth, _itemHeight);

            if (itm) {
                itm->setPos(currCol * itm->rect().width(), _currHeight);
                currCol++;

                if (currCol >= _colCount) {
                    currCol = 0;
                    _currHeight += _itemHeight;
                }
            }
        }

        if (currCol <= _colCount) {
            _currHeight += _itemHeight;
        }
    }
}

void GraphicLegendItem::drawFacies() {
    Project* p = (static_cast<ProfileLogger*> (QApplication::instance()))->getProject();

    if (!p) {
        return;
    }

    addTitle(QObject::tr("Facies"));

    if (p->getFaciesCount() > 0) {
        int currCol = 0;

        for (QList<Facies*>::iterator it = p->getFirstFacies();
                it != p->getLastFacies();
                it++) {
            FaciesLegendItem* itm = new FaciesLegendItem(this, *it,
                    _itemWidth, _itemHeight);

            if (itm) {
                itm->setPos(currCol * itm->rect().width(), _currHeight);
                currCol++;

                if (currCol >= _colCount) {
                    currCol = 0;
                    _currHeight += _itemHeight;
                }
            }
        }

        if (currCol <= _colCount) {
            _currHeight += _itemHeight;
        }
    }
}

void GraphicLegendItem::drawBeddingTypes() {
    Project* p =(static_cast<ProfileLogger*> (QApplication::instance()))->getProject();

    if (!p) {
        return;
    }

    addTitle(QObject::tr("Bedding Types"));

    if (p->getBeddingTypeCount() > 0) {
        int currCol = 0;

        for (QList<BeddingType*>::iterator it = p->getFirstBeddingType();
                it != p->getLastBeddingType();
                it++) {
            BeddingTypeLegendItem* itm = new BeddingTypeLegendItem(this, *it,
                    _itemWidth, _itemHeight);

            if (itm) {
                itm->setPos(currCol * itm->rect().width(), _currHeight);
                currCol++;

                if (currCol >= _colCount) {
                    currCol = 0;
                    _currHeight += _itemHeight;
                }
            }
        }

        if (currCol <= _colCount) {
            _currHeight += _itemHeight;
        }
    }
}

void GraphicLegendItem::drawColors() {
    Project* p = (static_cast<ProfileLogger*> (QApplication::instance()))->getProject();

    if (!p) {
        return;
    }

    addTitle(QObject::tr("Colors"));

    if (p->getColorCount() > 0) {
        int currCol = 0;

        for (QList<Color*>::iterator it = p->getFirstColor();
                it != p->getLastColor();
                it++) {
            ColorLegendItem* itm = new ColorLegendItem(this, *it,
                    _itemWidth, _itemHeight);

            if (itm) {
                itm->setPos(currCol * itm->rect().width(), _currHeight);
                currCol++;

                if (currCol >= _colCount) {
                    currCol = 0;
                    _currHeight += _itemHeight;
                }
            }
        }

        if (currCol <= _colCount) {
            _currHeight += _itemHeight;
        }
    }
}

void GraphicLegendItem::drawFossils() {
    Project* p = (static_cast<ProfileLogger*> (QApplication::instance()))->getProject();

    if (!p) {
        return;
    }

    addTitle(QObject::tr("Fossils"));

    if (p->getFossilCount() > 0) {
        int currCol = 0;

        for (QList<Fossil*>::iterator it = p->getFirstFossil();
                it != p->getLastFossil();
                it++) {
            FossilLegendItem* itm = new FossilLegendItem(this, *it,
                    _itemWidth, _itemHeight);

            if (itm) {
                itm->setPos(currCol * itm->rect().width(), _currHeight);
                currCol++;

                if (currCol >= _colCount) {
                    currCol = 0;
                    _currHeight += _itemHeight;
                }
            }
        }

        if (currCol <= _colCount) {
            _currHeight += _itemHeight;
        }
    }
}

void GraphicLegendItem::drawSedimentStructures() {
    Project* p = (static_cast<ProfileLogger*> (QApplication::instance()))->getProject();

    if (!p) {
        return;
    }

    addTitle(QObject::tr("Sediment Structures"));

    if (p->getSedimentStructureCount() > 0) {
        int currCol = 0;

        for (QList<SedimentStructure*>::iterator it = p->getFirstSedimentStructure();
                it != p->getLastSedimentStructure();
                it++) {
            SedimentStructureLegendItem* itm = new SedimentStructureLegendItem(this, *it,
                    _itemWidth, _itemHeight);

            if (itm) {
                itm->setPos(currCol * itm->rect().width(), _currHeight);
                currCol++;

                if (currCol >= _colCount) {
                    currCol = 0;
                    _currHeight += _itemHeight;
                }
            }
        }

        if (currCol <= _colCount) {
            _currHeight += _itemHeight;
        }
    }
}

void GraphicLegendItem::drawCustomSymbols() {
    Project* p = (static_cast<ProfileLogger*> (QApplication::instance()))->getProject();

    if (!p) {
        return;
    }

    addTitle(QObject::tr("Custom Symbols"));

    if (p->getCustomSymbolCount() > 0) {
        int currCol = 0;

        for (QList<CustomSymbol*>::iterator it = p->getFirstCustomSymbol();
                it != p->getLastCustomSymbol();
                it++) {
            CustomSymbolLegendItem* itm = new CustomSymbolLegendItem(this, *it,
                    _itemWidth, _itemHeight);

            if (itm) {
                itm->setPos(currCol * itm->rect().width(), _currHeight);
                currCol++;

                if (currCol >= _colCount) {
                    currCol = 0;
                    _currHeight += _itemHeight;
                }
            }
        }

        if (currCol <= _colCount) {
            _currHeight += _itemHeight;
        }
    }
}

void GraphicLegendItem::drawBoundaryTypes() {
    Project* p = (static_cast<ProfileLogger*> (QApplication::instance()))->getProject();

    if (!p) {
        return;
    }

    addTitle(QObject::tr("Boundary Types"));

    if (p->getBoundaryTypeCount() > 0) {
        int currCol = 0;

        for (QList<BoundaryType*>::iterator it = p->getFirstBoundaryType();
                it != p->getLastBoundaryType();
                it++) {
            BoundaryTypeLegendItem* itm = new BoundaryTypeLegendItem(this, *it,
                    _itemWidth, _itemHeight);

            if (itm) {
                itm->setPos(currCol * itm->rect().width(), _currHeight);
                currCol++;

                if (currCol >= _colCount) {
                    currCol = 0;
                    _currHeight += _itemHeight;
                }
            }
        }

        if (currCol <= _colCount) {
            _currHeight += _itemHeight;
        }
    }
}

void GraphicLegendItem::setProfileAndHeader(Profile* profile, GraphicColumnHeader* h) {
    _profile = profile;
    _header = h;

    if (!_header) {
        return;
    }

    if (!_profile) {
        return;
    }

    _colCount = _profile->getLegendColumns();
    
    _itemWidth = (_header->getWidthPosition(GraphicColumnHeader::ColumnEnd)
            - _header->getWidthPosition(GraphicColumnHeader::ColumnStart)) / _colCount;

    _itemHeight = (int)(_itemWidth * 1.7);

    drawLithologies();
    drawBeddingTypes();
    drawColors();
    drawFacies();
    drawFossils();
    drawSedimentStructures();
    drawCustomSymbols();
    drawBoundaryTypes();
    drawOutcropQualities();

    int w = _header->getWidthPosition(GraphicColumnHeader::ColumnEnd) - _header->getWidthPosition(GraphicColumnHeader::ColumnStart);

    setRect(QRect(0, 0,
            w, _currHeight));

    setPos(0, 0 - rect().height() - 10);
}

void GraphicLegendItem::contextMenuEvent(QGraphicsSceneContextMenuEvent* e) {
    ProfileLogger* app = (static_cast<ProfileLogger*> (QApplication::instance()));
    BedItemModel* bedsM = app->getBedItemModel();
    bedsM->setCurrentBed(0);

    QMenu* m = new QMenu((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow());

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
