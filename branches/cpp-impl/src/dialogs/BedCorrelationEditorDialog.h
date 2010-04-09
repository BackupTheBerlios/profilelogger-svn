/*
 * File:   BedCorrelationEditorDialog.h
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 21:39
 */

#ifndef _BEDCORRELATIONEDITORDIALOG_H
#define	_BEDCORRELATIONEDITORDIALOG_H

#include "DatasetEditorDialog.h"

class ProfileItemModel;
class ProfileItemView;
class BedItemModel;
class BedItemView;

class Bed;
class BedCorrelation;

class QtPatternSelectorWidget;

class BedCorrelationEditorDialog : public DatasetEditorDialog {
    Q_OBJECT
public:
    BedCorrelationEditorDialog(QWidget* parent, BedCorrelation* p);
    virtual ~BedCorrelationEditorDialog();
    BedCorrelation* getBedCorrelation();

    public slots:
    virtual void slotLeftBedChanged(Bed* b);
    virtual void slotRightBedChanged(Bed* b);
    virtual void slotShowBedCorrelation(BedCorrelation* c);

 private:
    void setupBedSelectors();

    ProfileItemModel* _leftProfileM;
    ProfileItemView* _leftProfileV;

    ProfileItemModel* _rightProfileM;
    ProfileItemView* _rightProfileV;

    BedItemModel* _leftBedM;
    BedItemView* _leftBedV;

    BedItemModel* _rightBedM;
    BedItemView* _rightBedV;
};

#endif	/* _BEDCORRELATIONEDITORDIALOG_H */
