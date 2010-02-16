/* 
 * File:   Dataset.h
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 19:41
 */

#ifndef _DATASET_H
#define	_DATASET_H

#include "PrimitiveDataset.h"

class Dataset: public PrimitiveDataset {
 public:
  Dataset(int id = 0,
	  const QString& name = QString::null,
	  const QString& description = QString::null,
	  const bool isInDatabase = false);
  virtual ~Dataset();
  void setName(const QString& n) { 
    _name = n; 
  }

  void setDescription(const QString& d) { 
    _description = d; 
  }

  QString getName() const { 
    return _name; 
  }

  QString getDescription() const { 
    return _description; 
  }

  bool hasName() { 
    return !_name.isEmpty(); 
  }

  bool hasDescription() { 
    return !_description.isEmpty(); 
  }

  virtual QString makeToolTipText(const bool withDatasetName = false) const;
    
  virtual void copyData(Dataset* other);

  virtual bool isInDatabase() const {
    return _isInDatabase;
  }

 private:
  QString _name;
  QString _description;
  bool _isInDatabase;
};

#endif	/* _DATASET_H */

