/* 
 * File:   GrainSizeModeSelectorWidget.h
 * Author: jolo
 *
 * Created on 12. Dezember 2009, 18:11
 */

#ifndef _GRAINSIZEMODESELECTORWIDGET_H
#define	_GRAINSIZEMODESELECTORWIDGET_H

#include <QGroupBox>

#include "GrainSizeModes.h"

class QRadioButton;

class GrainSizeModeSelectorWidget: public QGroupBox {
    Q_OBJECT
public:
    GrainSizeModeSelectorWidget(QWidget* p = 0);
    virtual ~GrainSizeModeSelectorWidget();

    GrainSizeModes getMode() { return _mode; }
    
signals:
    void modeChanged(GrainSizeModes m);

public slots:
    void setMode(GrainSizeModes m);

protected slots:
    void slotClasticToggled(bool toggled);
    void slotCarbonateToggled(bool toggled);
    
private:
    QRadioButton* _clasticW;
    QRadioButton* _carbonateW;

    GrainSizeModes _mode;
};

#endif	/* _GRAINSIZEMODESELECTORWIDGET_H */

