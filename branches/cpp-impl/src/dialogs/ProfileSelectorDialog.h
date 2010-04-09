/* 
 * File:   ProfileSelectorDialog.h
 * Author: jolo
 *
 * Created on 23. Januar 2010, 08:51
 */

#ifndef _PROFILESELECTORDIALOG_H
#define	_PROFILESELECTORDIALOG_H

#include "ListSelectorDialog.h"

class Profile;

class ProfileSelectorDialog: public ListSelectorDialog {
    Q_OBJECT
public:
    ProfileSelectorDialog(QWidget* p);
    virtual ~ProfileSelectorDialog();

    Profile* getSelectedProfile();

protected slots:
    virtual void slotCurrentProfileChanged(Profile* p);
};

#endif	/* _PROFILESELECTORDIALOG_H */

