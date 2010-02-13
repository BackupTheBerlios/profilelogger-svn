/* 
 * File:   IdLabel.h
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 21:24
 */

#ifndef _IDLABEL_H
#define	_IDLABEL_H

#include <QLabel>

class IdLabel: public QLabel {
    Q_OBJECT
public:
    IdLabel(QWidget* p);
    virtual ~IdLabel();
    QLabel* getLabel();
    
    void setId(int id);
private:
    QLabel* _lbl;
};

#endif	/* _IDLABEL_H */

