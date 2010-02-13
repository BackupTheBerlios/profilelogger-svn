/* 
 * File:   GraphicColumnBody.h
 * Author: jolo
 *
 * Created on 16. Dezember 2009, 15:15
 */

#ifndef _GRAPHICCOLUMNBODY_H
#define	_GRAPHICCOLUMNBODY_H

#include <QGraphicsRectItem>

#include <QPen>
#include <QFont>
#include <QList>

#include "GraphicBedItem.h"

class GraphicColumnHeader;
class GraphicBedItem;

class Profile;
class Bed;

class GraphicColumnBody: public QGraphicsRectItem {
public:
    GraphicColumnBody(QGraphicsItem* p = 0);
    virtual ~GraphicColumnBody();

    void setProfileAndHeader(Profile* p, GraphicColumnHeader* h);
    Profile* getProfile() { return _profile; }
    void selectBed(Bed* b);
    void clearSelection();
    
private:
    void drawHelpLines();
    void drawHeightMarks();
    void drawBigHeightMark(int height, const QString& value);
    void drawSmallHeightMark(int height);
    
    void drawHelpLine(int widthFromLeft, const QPen& pen);
    void drawLine(const QPoint& start, const QPoint& end, const QPen& pen);

    GraphicBedItem* getItemForBed(Bed* b);
    Bed* getBedFromItem(GraphicBedItem* itm);
    
    GraphicColumnHeader* _header;
    QPen _solidLinePen;
    QPen _dashedLinePen;
    QPen _dottedLinePen;
    QFont _smallMarkFont;
    QFont _bigMarkFont;
    QColor _smallMarkColor;
    QColor _bigMarkColor;
    QPen _smallMarkLinePen;
    QPen _bigMarkLinePen;

    Profile* _profile;
    int _unit;
    QList<GraphicBedItem*> _beds;
    QList<GraphicBedItem*> _selectedItems;

};

#endif	/* _GRAPHICCOLUMNBODY_H */

