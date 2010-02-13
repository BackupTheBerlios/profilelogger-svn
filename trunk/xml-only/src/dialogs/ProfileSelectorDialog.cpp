/* 
 * File:   ProfileSelectorDialog.cpp
 * Author: jolo
 * 
 * Created on 23. Januar 2010, 08:51
 */

#include "ProfileSelectorDialog.h"

#include "ProfileLogger.h"
#include "ProfileItemView.h"
#include "Profile.h"

#include <QApplication>

ProfileSelectorDialog::ProfileSelectorDialog(QWidget* p)
: ListSelectorDialog(p, QObject::tr("Select Profile")) {
    ProfileItemView* v = new ProfileItemView(this,
            (static_cast<ProfileLogger*>(QApplication::instance()))->getProfileItemModel());
    setView(v);
    v->setEnabled(true);
    v->setContextMenuPolicy(Qt::NoContextMenu);

    connect(v, SIGNAL(currentProfileChanged(Profile*)), this, SLOT(slotCurrentProfileChanged(Profile*)));
}

ProfileSelectorDialog::~ProfileSelectorDialog() {
}

Profile* ProfileSelectorDialog::getSelectedProfile() {
    if (!getSelectedDataset()) {
        return 0;
    }

    return static_cast<Profile*>(getSelectedDataset());
}

void ProfileSelectorDialog::slotCurrentProfileChanged(Profile* p) {
    _currentDataset = p;
}
