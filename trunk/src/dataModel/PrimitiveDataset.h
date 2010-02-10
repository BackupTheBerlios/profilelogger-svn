#ifndef PRIMITIVE_DATASET_H
#define PRIMITIVE_DATASET_H

#include <QString>
#include <QStringList>
#include <QCoreApplication>

class PrimitiveDataset {
  Q_DECLARE_TR_FUNCTIONS(PrimitiveDataset)
 public:
  PrimitiveDataset(int id = 0);
  virtual ~PrimitiveDataset();

  void setId(int id) { _id = id; }
  bool hasId() { return _id > 0; }
  int getId() const { return _id; }
  void copyData(PrimitiveDataset* other) { (void) other; }

  virtual QString toString(const bool withDatasetName = false) const;
  virtual QString makeToolTipText(const bool withDatasetName = false) const;

 private:
  int _id;
};

#endif
