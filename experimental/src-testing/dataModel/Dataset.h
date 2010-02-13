#ifndef DATASET_H
#define DATASET_H

#include <QString>

class Dataset {
 public:
  Dataset(int id = 0);
  virtual ~Dataset() {}

  void setId(int id) {
    _id = id;
  }

  int getId() const {
    return _id;
  }

  bool hasId() const {
    return _id > 0;
  }

  virtual QString toString() const {
    return QString::number(_id);
  }

 private:
  int _id;
};

#endif
