/* 
 * File:   ManagementToolBox.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:30
 */

#ifndef _MANAGEMENTTOOLBOX_H
#define	_MANAGEMENTTOOLBOX_H

#include <QToolBox>

#include "SedimentStructureView.h"

class Project;

class OutcropQualityView;
class ColorView;
class LithologyView;
class BeddingTypeView;
class BoundaryTypeView;
class FossilView;
class SedimentaryStructureView;
class CustomSymbolView;
class FaciesView;
class LithologicalUnitTypeView;
class LithologicalUnitView;

class ManagementToolBox: public QToolBox {
    Q_OBJECT
public:
    ManagementToolBox(QWidget* parent = 0);
    virtual ~ManagementToolBox();

public slots:
    virtual void slotCurrentProjectChanged(Project* p);
    
 signals:
    void currentProjectChanged(Project* p);

private:
    Project* _project;

    OutcropQualityView* _outcropQualityV;
    ColorView* _colorV;
    LithologyView* _lithologyV;
    BeddingTypeView* _beddingTypeV;
    BoundaryTypeView* _boundaryTypeV;
    FossilView* _fossilV;
    SedimentStructureView* _sedimentStructureV;
    CustomSymbolView* _customSymbolV;
    FaciesView* _faciesV;
    LithologicalUnitTypeView* _lithologicalUnitTypeV;
    LithologicalUnitView* _lithologicalUnitV;
};

#endif	/* _MANAGEMENTTOOLBOX_H */

