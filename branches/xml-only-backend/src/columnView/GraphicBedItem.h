/* 
 * File:   GraphicBedItem.h
 * Author: jolo
 *
 * Created on 16. Dezember 2009, 18:56
 */

#ifndef _GRAPHICBEDITEM_H
#define	_GRAPHICBEDITEM_H

#include "QGraphicsRectItem"

#include <QColor>
#include <QFont>

class GraphicColumnHeader;
class QGraphicsScene;
class QGraphicsTextItem;
class SymbolFactory;

class Bed;

class GraphicBedItem: public QGraphicsRectItem {
public:
    GraphicBedItem(QGraphicsItem* p, GraphicColumnHeader* header, Bed* bed);
    virtual ~GraphicBedItem();

    void select();
    void deselect();
    bool isSelected() { return _isSelected; }

    Bed* getBed() const { return _bed; }

protected:
    void contextMenuEvent(QGraphicsSceneContextMenuEvent* event);

private:
    void drawLithology();
    void drawGrainSize();
    void drawBedNumber();
    void drawFossils();
    void drawSedimentStructures();
    void drawCustomSymbols();
    void drawTopBoundary();
    void drawNotes();
    void drawColor();
    void drawFacies();
    void drawLithologicalUnit();
    void drawOutcropQuality();
    
    GraphicColumnHeader* _header;
    Bed* _bed;

    bool _isSelected;

    QFont _font;

    SymbolFactory* _sf;

    int _leftLineStartX;
    int _leftLineEndX;
    int _rightLineStartX;
    int _rightLineEndX;
};

#endif	/* _GRAPHICBEDITEM_H */

