#ifndef BED_CORRELATION_H
#define BED_CORRELATION_H

#include "Dataset.h"

class Bed;

class BedCorrelation: public Dataset {
public:
  BedCorrelation(int id = 0,
		 Bed* left = 0, 
		 Bed* right = 0);
  virtual ~BedCorrelation();
  
  Bed* getLeftBed() const {
    return _left;
  }
  
  void setLeftBed(Bed* left);

  Bed* getRightBed() const { 
    return _right;
  }

  void setRightBed(Bed* r);

  bool hasLeftBed() const {
    return 0 != _left;
  }

  bool hasRightBed() const {
    return 0 != _right;
  }

private:
  void updateName();

  Bed* _left;
  Bed* _right;
};

#endif
