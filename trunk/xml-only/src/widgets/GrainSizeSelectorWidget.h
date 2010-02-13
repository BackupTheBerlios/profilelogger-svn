/* 
 * File:   GrainSizeSelectorWidget.h
 * Author: jolo
 *
 * Created on 23. Januar 2010, 13:33
 */

#ifndef _GRAINSIZESELECTORWIDGET_H
#define	_GRAINSIZESELECTORWIDGET_H

#include <QWidget>

#include "GrainSizeModes.h"

class GrainSizeModeSelectorWidget;
class CarbonateGrainSizeView;
class ClasticGrainSizeView;

class ClasticGrainSize;
class CarbonateGrainSize;

class GrainSizeSelectorWidget : public QWidget {
    Q_OBJECT
public:
    GrainSizeSelectorWidget(QWidget* p);
    virtual ~GrainSizeSelectorWidget();

    void setGrainSizeMode(GrainSizeModes m);
    void setClasticGrainSize(ClasticGrainSize* s);
    void setCarbonateGrainSize(CarbonateGrainSize* s);
    
signals:
    void grainSizeModeChanged(GrainSizeModes m);
    void clasticGrainSizeChanged(ClasticGrainSize* s);
    void carbonateGrainSizeChanged(CarbonateGrainSize* s);

public slots:
    void slotGrainSizeModeChanged(GrainSizeModes m);
    void slotClasticGrainSizeChanged(ClasticGrainSize* s);
    void slotCarbonateGrainSizeChanged(CarbonateGrainSize* s);
    
private:
    GrainSizeModeSelectorWidget* _modesW;
    CarbonateGrainSizeView* _carbW;
    ClasticGrainSizeView* _clastW;
};

#endif	/* _GRAINSIZESELECTORWIDGET_H */

