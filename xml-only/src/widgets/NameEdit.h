/* 
 * File:   NameEdit.h
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 20:50
 */

#ifndef _NAMEEDIT_H
#define	_NAMEEDIT_H

#include "QLineEdit"

class QLabel;

class NameEdit : public QLineEdit {
    Q_OBJECT
public:
    NameEdit(QWidget* p = 0);
    NameEdit(const NameEdit& orig);
    virtual ~NameEdit();
    QLabel* getLabel();

signals:
    void nameChanged(const QString& s);

public slots:
    void slotTextChanged(const QString& s);

private:
    QLabel* _lbl;
};

#endif	/* _NAMEEDIT_H */

