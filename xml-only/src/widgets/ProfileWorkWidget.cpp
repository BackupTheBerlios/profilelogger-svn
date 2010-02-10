/* 
 * File:   ProfileWorkWidget.cpp
 * Author: jolo
 * 
 * Created on 10. Dezember 2009, 20:05
 */

#include "ProfileWorkWidget.h"

#include "Profile.h"

ProfileWorkWidget::ProfileWorkWidget(QWidget* p)
: QWidget(p),
_profile(0) {
}

ProfileWorkWidget::~ProfileWorkWidget() {
}

void ProfileWorkWidget::slotCurrentProfileChanged(Profile* p) {
    _profile = p;
}
