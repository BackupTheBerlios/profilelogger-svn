/*
 * File:   CustomSymbol.h
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 16:37
 */

#ifndef _CustomSymbol_H
#define	_CustomSymbol_H

#include "DatasetWithFileName.h"

#include <QObject>
#include <QStringList>

class CustomSymbol: public DatasetWithFileName {
 public:
  CustomSymbol(Project* p = 0,
	       int id = 0,
	       const QString& name = QObject::tr("New Custom Symbol"),
	       const QString& description = QString::null,
	       const QString& fileName = QString::null);
  virtual ~CustomSymbol();
  QString makeToolTipText(const bool withDatasetName=false) const;
};

#endif	/* _CustomSymbol_H */

