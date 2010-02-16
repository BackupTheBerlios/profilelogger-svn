/* 
 * File:   DatasetWithFileName.h
 * Author: jolo
 *
 * Created on 17. Dezember 2009, 13:33
 */

#ifndef _DATASETWITHFILENAME_H
#define	_DATASETWITHFILENAME_H

#include "DatasetInProject.h"

class DatasetWithFileName: public DatasetInProject {
 public:
  DatasetWithFileName(Project* p = 0,
		      int id = 0,
		      const QString& name = QString::null,
		      const QString& description = QString::null,
		      const QString& fileName = QString::null);
  DatasetWithFileName(const DatasetWithFileName& orig);
  virtual ~DatasetWithFileName();

  bool hasFileName() const { 
    return !_fileName.isEmpty(); 
  }

  void setFileName(const QString& f) { 
    _fileName = f; 
  }

  QString getFileName() const { 
    return _fileName; 
  }

 private:
  QString _fileName;
};

#endif	/* _DATASETWITHFILENAME_H */

