/* 
 * File:   ProfileCorrelationItem.h
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 20:10
 */

#ifndef _PROFILECORRELATIONITEM_H
#define	_PROFILECORRELATIONITEM_H

#include "StandardItem.h"

class ProfileCorrelation;

class ProfileCorrelationItem: public StandardItem {
 public:
  ProfileCorrelationItem(ProfileCorrelation* p);
  virtual ~ProfileCorrelationItem();
  ProfileCorrelation* getProfileCorrelation() { 
    return (ProfileCorrelation*)getData(); 
  }
};

#endif	/* _PROFILECORRELATIONITEM_H */

