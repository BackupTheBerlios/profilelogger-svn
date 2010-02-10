#ifndef DBSTANDARDDATASET_H
#define DBSTANDARDDATASET_H

#include "DbDataset.h"

class DbStandardDataset: public DbDataset {
    Q_DECLARE_TR_FUNCTIONS(DbStandardDataset);
 public:
    DbStandardDataset(const int id = 0,
		      const QString& name = QString::null,
		      const QString& description = QString::null);

    virtual ~DbStandardDataset() {}

    virtual void setName(const QString& n) {
      setIsDirty(true);
      _name = n;
    }

    virtual void setDescription(const QString& n) {
      setIsDirty(true);
      _description = n;
    }

    QString getName() const {
      return _name;
    }

    QString getDescription() const {
      return _description;
    }

    bool hasName() const {
      return !_name.isEmpty();
    }

    bool hasDescription() const {
      return !_description.isEmpty();
    }

    virtual QString toString() const;

 private:
    QString _name;
    QString _description;
};

#endif
