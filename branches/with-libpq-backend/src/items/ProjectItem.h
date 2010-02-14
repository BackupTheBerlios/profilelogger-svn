#ifndef _PROJECTITEM_H
#define	_PROJECTITEM_H

#include "StandardItem.h"

class Project;

class ProjectItem: public StandardItem {
public:
    ProjectItem(Project* p);
    virtual ~ProjectItem();
    Project* getProject() { return (Project*)getData(); }
};

#endif	/* _PROJECTITEM_H */

