/*
 * File:   LithologyEditorDialog.h
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 21:39
 */

#ifndef _LITHOLOGYEDITORDIALOG_H
#define	_LITHOLOGYEDITORDIALOG_H

#include "DatasetInProjectWithFileNameEditorDialog.h"
#include "GrainSizeModes.h"

class Lithology;
class GrainSizeSelectorWidget;
class CarbonateGrainSize;
class ClasticGrainSize;
class LithologyManager;

class LithologyEditorDialog : public DatasetInProjectWithFileNameEditorDialog {
    Q_OBJECT
public:
    LithologyEditorDialog(QWidget* parent, Lithology* p);
    virtual ~LithologyEditorDialog();
    Lithology* getLithology();
    LithologyManager* getLithologyManager();

public slots:
    virtual void accept();
    void slotDefaultGrainSizeModeChanged(GrainSizeModes m);
    void slotDefaultCarbonateGrainSizeChanged(CarbonateGrainSize* s);
    void slotDefaultClasticGrainSizeChanged(ClasticGrainSize* s);

private:
    GrainSizeSelectorWidget* _grainSizeW;
};

#endif	/* _LITHOLOGYEDITORDIALOG_H */
