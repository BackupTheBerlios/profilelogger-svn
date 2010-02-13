/* 
 * File:   ProfileWorkWidget.h
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 20:05
 */

#ifndef _PROFILEWORKWIDGET_H
#define	_PROFILEWORKWIDGET_H

#include <QWidget>

class Profile;

class ProfileWorkWidget: public QWidget {
    Q_OBJECT
public:
    ProfileWorkWidget(QWidget* p = 0);

    virtual ~ProfileWorkWidget();

public slots:
    virtual void slotCurrentProfileChanged(Profile* p);

private:
    Profile* _profile;
};

#endif	/* _PROFILEWORKWIDGET_H */

