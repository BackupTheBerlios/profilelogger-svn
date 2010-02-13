/* 
 * File:   ManagementToolBox.cpp
 * Author: jolo
 * 
 * Created on 11. Dezember 2009, 16:30
 */

#include "ManagementToolBox.h"

#include <QApplication>

#include "WorkWidget.h"
#include "ProfileLogger.h"
#include "OutcropQualityItemModel.h"
#include "OutcropQualityView.h"
#include "ColorItemModel.h"
#include "ColorView.h"
#include "LithologyView.h"
#include "BeddingTypeView.h"
#include "BoundaryTypeView.h"
#include "FossilView.h"
#include "SedimentStructureView.h"
#include "CustomSymbolView.h"
#include "Project.h"
#include "FaciesView.h"
#include "LithologicalUnitTypeView.h"
#include "LithologicalUnitView.h"

ManagementToolBox::ManagementToolBox(QWidget* p)
: QToolBox(p),
_project(0) {
    setEnabled(false);

    _colorV = new ColorView(this,
            (static_cast<ProfileLogger*> (QApplication::instance()))->getColorItemModel());
    _outcropQualityV = new OutcropQualityView(this,
            (static_cast<ProfileLogger*> (QApplication::instance()))->getOutcropQualityItemModel());
    _lithologyV = new LithologyView(this,
            (static_cast<ProfileLogger*> (QApplication::instance()))->getLithologyItemModel());
    _beddingTypeV = new BeddingTypeView(this,
            (static_cast<ProfileLogger*> (QApplication::instance()))->getBeddingTypeItemModel());
    _boundaryTypeV = new BoundaryTypeView(this,
            (static_cast<ProfileLogger*> (QApplication::instance()))->getBoundaryTypeItemModel());
    _fossilV = new FossilView(this,
            (static_cast<ProfileLogger*> (QApplication::instance()))->getFossilItemModel());
    _sedimentStructureV = new SedimentStructureView(this,
            (static_cast<ProfileLogger*> (QApplication::instance()))->getSedimentStructureItemModel());
    _customSymbolV = new CustomSymbolView(this,
            (static_cast<ProfileLogger*> (QApplication::instance()))->getCustomSymbolItemModel());
    _faciesV = new FaciesView(this,
            (static_cast<ProfileLogger*> (QApplication::instance()))->getFaciesItemModel());

    _lithologicalUnitTypeV = new LithologicalUnitTypeView(this,
            (static_cast<ProfileLogger*> (QApplication::instance()))->getLithologicalUnitTypeItemModel());

    _lithologicalUnitV = new LithologicalUnitView(this,
            (static_cast<ProfileLogger*> (QApplication::instance()))->getLithologicalUnitItemModel());

    addItem(_lithologyV, tr("Lithologies"));
    addItem(_fossilV, tr("Fossils"));
    addItem(_sedimentStructureV, tr("Sediment Structures"));
    addItem(_customSymbolV, tr("Custom Symbols"));
    addItem(_colorV, tr("Colors"));
    addItem(_beddingTypeV, tr("Bedding Types"));
    addItem(_boundaryTypeV, tr("Boundary Types"));
    addItem(_outcropQualityV, tr("Outcrop Qualities"));
    addItem(_faciesV, tr("Facies"));
    addItem(_lithologicalUnitTypeV, tr("Lithological Unit Types"));
    addItem(_lithologicalUnitV, tr("Lithological Units"));

    connect(static_cast<ProfileLogger*> (QApplication::instance()), SIGNAL(currentProjectChanged(Project*)),
            this, SLOT(slotCurrentProjectChanged(Project*)));
}

ManagementToolBox::~ManagementToolBox() {
}

void ManagementToolBox::slotCurrentProjectChanged(Project* p) {
    _project = p;
    setEnabled(_project);
}
