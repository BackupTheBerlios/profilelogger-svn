#ifndef DB_INTERFACE_PART_H
#define DB_INTERFACE_PART_H

#include <QObject>

class DbInterfacePart: public QObject {
  Q_OBJECT
    public:
  DbInterfacePart(QObject* parent, const QString& name = QString::null);
  virtual ~DbInterfacePart();

  QString getQualifiedName() const {
    return _name;
  }

  bool hasName() const {
    return !_name.isEmpty();
  }

  void setName(const QString& n) {
    _name = n;
  }

  QString getName() const {
    return _name;
  }

 private:
  QString _name;
};

#endif
