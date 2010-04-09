/* 
 * File:   GraphicColumnHeader.h
 * Author: jolo
 *
 * Created on 16. Dezember 2009, 14:19
 */

#ifndef _GRAPHICCOLUMNHEADER_H
#define	_GRAPHICCOLUMNHEADER_H

#include <QGraphicsRectItem>

#include <QMap>
#include <QPen>

class QGraphicsLineItem;
class QGraphicsTextItem;
class Profile;

class GraphicColumnHeader : public QGraphicsRectItem {
public:
    GraphicColumnHeader(QGraphicsItem* p = 0);
    virtual ~GraphicColumnHeader();

    enum WidthPositions {
        ColumnStart,

        HeightStart,
        HeightEnd,
        BedStart,
        BedEnd,
        LithologyStart,
        LithologyEnd,
        NoClasticGrainsStart,
        NoClasticGrainsEnd,
        ClayStart,
        ClayEnd,

        SiltStart,
        FineSiltStart,
        FineSiltEnd,
        MediumSiltStart,
        MediumSiltEnd,
        CoarseSiltStart,
        CoarseSiltEnd,
        SiltEnd,

        SandStart,
        FineSandStart,
        FineSandEnd,
        MediumSandStart,
        MediumSandEnd,
        CoarseSandStart,
        CoarseSandEnd,
        SandEnd,

        GravelStart,
        FineGravelStart,
        FineGravelEnd,
        MediumGravelStart,
        MediumGravelEnd,
        CoarseGravelStart,
        CoarseGravelEnd,
        GravelEnd,

        CobblesStart,
        CobblesEnd,

        BlocksStart,
        BlocksEnd,

        EvaporiteStart,
        EvaporiteEnd,
        MudstoneStart,
        MudstoneEnd,
        WackestoneStart,
        WackestoneEnd,
        PackstoneStart,
        PackstoneEnd,
        GrainstoneStart,
        GrainstoneEnd,
        RudstoneStart,
        RudstoneEnd,

        ColorStart,
        ColorEnd,

        FaciesStart,
        FaciesEnd,

        OutcropQualityStart,
        OutcropQualityEnd,

        LithologicalUnitStart,
        LithologicalUnitEnd,

        FossilsStart,
        FossilsEnd,

        SedimentStructuresStart,
        SedimentStructuresEnd,

        CustomSymbolsStart,
        CustomSymbolsEnd,

        NotesStart,
        NotesEnd,

        ColumnEnd
    };

    int getWidthPosition(GraphicColumnHeader::WidthPositions pos) {
        if (!_w.contains(pos)) {
            return 0;
        }

        return _w[pos];
    }

    int getCellWidth() {
        return _unit;
    }
    void setProfile(Profile* p);

protected:
    void contextMenuEvent(QGraphicsSceneContextMenuEvent* e);
    
private:
    void setupWidths();

    void drawContent();
    void drawBoundingBox();
    void drawHeightBox();
    void drawBedBox();
    void drawLithologyBox();
    void drawGrainSizesBox();
    void drawClasticsBox();
    void drawCarbonatesBox();
    void drawColorBox();
    void drawFossilsBox();
    void drawSedimentStructuresBox();
    void drawCustomSymbolsBox();
    void drawNotesBox();
    void drawFaciesBox();
    void drawOutcropQualitiesBox();
    void drawLithologicalUnitsBox();

    QGraphicsLineItem* drawLine(const QPoint& begin, const QPoint& end, const QPen& pen);
    QGraphicsTextItem* drawText(const QPoint& pos, const QString& txt);

    int _unit;
    QPen _pen;
    QMap<GraphicColumnHeader::WidthPositions, int> _w;
    Profile* _profile;
};

#endif	/* _GRAPHICCOLUMNHEADER_H */

