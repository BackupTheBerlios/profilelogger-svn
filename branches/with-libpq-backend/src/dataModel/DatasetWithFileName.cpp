/* 
 * File:   DatasetWithFileName.cpp
 * Author: jolo
 * 
 * Created on 17. Dezember 2009, 13:33
 */

#include "DatasetWithFileName.h"

DatasetWithFileName::DatasetWithFileName(Project* p,
					 int id,
					 const QString& name,
					 const QString& description,
					 const QString& fileName)
  : DatasetInProject(p, 
		     id, 
		     name, 
		     description),
    _fileName(fileName) {
    }

DatasetWithFileName::~DatasetWithFileName() {
}
