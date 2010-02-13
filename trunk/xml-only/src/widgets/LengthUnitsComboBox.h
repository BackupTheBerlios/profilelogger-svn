/* 
 * File:   LengthUnitsComboBox.h
 * Author: jolo
 *
 * Created on 29. Januar 2010, 15:10
 */

#ifndef _LENGTHUNITSCOMBOBOX_H
#define	_LENGTHUNITSCOMBOBOX_H

#include <QComboBox>

class LengthUnit;

class LengthUnitsComboBox : public QComboBox {
    Q_OBJECT
public:
    LengthUnitsComboBox(QWidget* p);
    virtual ~LengthUnitsComboBox();
    void setLengthUnit(LengthUnit* u);
    
signals:
    void lengthUnitChanged(LengthUnit* u);

protected slots:
    void slotSelectionChanged(const QString& s);

private:
    QMap<QString, LengthUnit*> _units;
};

#endif	/* _LENGTHUNITSCOMBOBOX_H */

