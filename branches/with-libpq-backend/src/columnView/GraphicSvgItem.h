/* 
 * File:   GraphicsSvgItem.h
 * Author: jolo
 *
 * Created on 24. Dezember 2009, 10:18
 */

#ifndef _GRAPHICSVGITEM_H
#define	_GRAPHICSVGITEM_H

#include <QGraphicsSvgItem>

class GraphicSvgItem: public QGraphicsSvgItem {
public:
    GraphicSvgItem(const QString& filename,
            QGraphicsItem* parent);

    virtual ~GraphicSvgItem();
};

#endif	/* _GRAPHICSVGITEM_H */

