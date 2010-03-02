#ifndef STANDARD_DATASET_H
#define STANDARD_DATASET_H

#include "Dataset.h"

class StandardDataset: public Dataset 
{
Q_OBJECT
    Q_PROPERTY(QString _name READ getName WRITE setName)
    Q_PROPERTY(QString _description READ getDescription WRITE setDescription)

    public:
    StandardDataset(Dataset* parent = 0,
		    const int id = 0,
		    const QString& name = QString::null,
		    const QString& description = QString::null);
    virtual ~StandardDataset();
    
    void setName(const QString& n);
    void setDescription(const QString& d);
    QString getName() const;
    QString getDescription() const;
    
private:
    QString _name;
    QString _description;
};

#endif
