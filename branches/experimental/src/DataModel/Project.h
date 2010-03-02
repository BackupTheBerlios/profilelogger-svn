#ifndef PROJECT_H
#define PROJECT_H

#include "StandardDataset.h"

class Project: public StandardDataset
{
Q_OBJECT
    public:
    Project(Dataset* parent = 0,
	    const int id = 0,
	    const QString& name = QString::null,
	    const QString& description = QString::null);
    
    virtual ~Project();
};

#endif
