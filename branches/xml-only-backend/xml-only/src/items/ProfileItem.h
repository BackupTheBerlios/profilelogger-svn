/* 
 * File:   ProfileItem.h
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 20:10
 */

#ifndef _PROFILEITEM_H
#define	_PROFILEITEM_H

#include "StandardItem.h"

class Profile;

class ProfileItem: public StandardItem {
public:
    ProfileItem(Profile* p);
    virtual ~ProfileItem();
    Profile* getProfile() { return (Profile*)getData(); }
};

#endif	/* _PROFILEITEM_H */

