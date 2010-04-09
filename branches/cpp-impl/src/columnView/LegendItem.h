/* 
 * File:   LegendItem.h
 * Author: jolo
 *
 * Created on 13. Januar 2010, 16:00
 */

#ifndef _LEGENDITEM_H
#define	_LEGENDITEM_H

#include <QGraphicsRectItem>
#include <QFont>

class LegendItem : public QGraphicsRectItem {
public:
    LegendItem(QGraphicsItem* p = 0, int width = 200, int height = 300);
    virtual ~LegendItem();

    QFont getFont() {
        return _font;
    }

    int getSpace() {
        return _space;
    }

protected:
    void addId(int id);
    void addName(const QString& name);

    int getCurrHeight() {
        return _currHeight;
    }

    QFont _font;
    int _space;
    int _currHeight;
};

#endif	/* _LEGENDITEM_H */

