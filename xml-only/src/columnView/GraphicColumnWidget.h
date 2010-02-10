/* 
 * File:   GraphicColumnWidget.h
 * Author: jolo
 *
 * Created on 16. Dezember 2009, 13:41
 */

#ifndef _GRAPHICCOLUMNWIDGET_H
#define	_GRAPHICCOLUMNWIDGET_H

#include <QGraphicsView>

class QGraphicsScene;

class GraphicColumnHeader;
class GraphicColumnBody;

class Profile;
class Bed;
class GraphicLegendItem;

class GraphicColumnWidget : public QGraphicsView {
    Q_OBJECT
public:
    GraphicColumnWidget(QWidget* p = 0);
    virtual ~GraphicColumnWidget();

signals:
    void currentBedChanged(Bed* b);

public slots:
    void slotCurrentProfileChanged(Profile* p);
    void slotCurrentBedChanged(Bed* b);
    void reload();
    void slotExportToSvg(Profile* p);
    void selectBed(Bed* b);
    void slotExportToSvg();
    void slotExportToTiff();
    void slotExportToPdf();
    void slotExportToJpg();
    void slotExportToPng();
    void slotPrint();
    
protected:
    virtual void keyPressEvent(QKeyEvent* e);
    
private:
    Profile* _profile;
    QGraphicsScene* _scene;
    GraphicColumnHeader* _header;
    GraphicColumnBody* _body;
    GraphicLegendItem* _legend;
    
    qreal _scale;
    qreal _scaleStep;
};

#endif	/* _GRAPHICCOLUMNWIDGET_H */

