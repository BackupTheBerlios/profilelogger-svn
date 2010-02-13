/* 
 * File:   GraphicLegendItem.h
 * Author: jolo
 *
 * Created on 13. Januar 2010, 15:32
 */

#ifndef _GRAPHICLEGENDITEM_H
#define	_GRAPHICLEGENDITEM_H

#include "QGraphicsRectItem"

#include <QFont>
#include <QPen>

class Profile;
class GraphicColumnHeader;

class GraphicLegendItem : public QGraphicsRectItem {
public:
    GraphicLegendItem();
    virtual ~GraphicLegendItem();

    void setProfileAndHeader(Profile* p, GraphicColumnHeader* h);

    int getLegendItemWidth() {
        return _itemWidth;
    }

    int getLegendItemHeight() {
        return _itemHeight;
    }

    int getLegendColCount() {
        return _colCount;
    }

protected:
    void contextMenuEvent(QGraphicsSceneContextMenuEvent* e);

private:
    void addTitle(const QString& s);

    void drawLithologies();
    void drawBeddingTypes();
    void drawColors();
    void drawFossils();
    void drawSedimentStructures();
    void drawCustomSymbols();
    void drawBoundaryTypes();
    void drawFacies();
    void drawOutcropQualities();
    
    Profile* _profile;
    GraphicColumnHeader* _header;

    QPen _pen;
    QFont _font;

    int _currHeight;
    int _titleSep;
    int _itemWidth;
    int _itemHeight;
    int _colCount;
};

#endif	/* _GRAPHICLEGENDITEM_H */

