#ifndef DATASET_H
#define DATASET_H

#include <QtCore/QObject>

class Dataset: public QObject 
{
    Q_OBJECT
    Q_PROPERTY(int _id READ getId WRITE setId)
	public:
    Dataset(QObject* parent = 0,
	    const int id = 0);
    
    virtual ~Dataset();

    int getId() const;
    void setId(const int id);
    
private:
    int _id;
};

#endif
