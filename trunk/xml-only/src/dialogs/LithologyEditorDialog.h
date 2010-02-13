/*
 * File:   LithologyEditorDialog.h
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 21:39
 */

#ifndef _LITHOLOGYEDITORDIALOG_H
#define	_LITHOLOGYEDITORDIALOG_H

#include "DatasetWithFileNameEditorDialog.h"
#include "GrainSizeModes.h"

class Lithology;
class GrainSizeSelectorWidget;
class CarbonateGrainSize;
class ClasticGrainSize;

class LithologyEditorDialog : public DatasetWithFileNameEditorDialog {
    Q_OBJECT
public:
    LithologyEditorDialog(QWidget* parent, Lithology* p);
    virtual ~LithologyEditorDialog();
    Lithology* getLithology();

public slots:
    void slotDefaultGrainSizeModeChanged(GrainSizeModes m);
    void slotDefaultCarbonateGrainSizeChanged(CarbonateGrainSize* s);
    void slotDefaultClasticGrainSizeChanged(ClasticGrainSize* s);

private:
    GrainSizeSelectorWidget* _grainSizeW;
};

#endif	/* _LITHOLOGYEDITORDIALOG_H */
