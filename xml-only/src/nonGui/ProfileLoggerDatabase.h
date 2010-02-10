#ifndef PROFILE_LOGGER_DATABASE_H
#define PROFILE_LOGGER_DATABASE_H

#include "Database.h"

class Schema;
class Sequence;
class PrimaryKey;
class Table;
class TableColumn;

class ProfileLoggerDatabase: public Database
{
  Q_OBJECT
    public:
  ProfileLoggerDatabase(QCoreApplication* p);
  virtual ~ProfileLoggerDatabase();

  Sequence* getProjectsSequence() const {
    return _seqProjects;
  }

  Table* getProjectsTable() const {
    return _tProjects;
  }

 private:
  void setupSchemas();
  void setupSequences();
  void setupTables();
  void setupForeignKeys();
  void configureTables();

  void configureTableProjects();
  void configureTableLithologies();
  void configureTableFossils();
  void configureTableProfiles();
  void configureTableSedimentStructures();
  void configureTableCustomSymbols();
  void configureTableColors();
  void configureTableBeddingTypes();
  void configureTableBoundaryTypes();
  void configureTableOutcropQualities();
  void configureTableFacies();
  void configureTableLithologicalUnitTypes();
  void configureTableLithologicalUnits();
  void configureTableGrainSizeModes();
  void configureTableGrainSizes();
  void configureTableBeds();

  Schema* _schemaData;

  Sequence* _seqProjects;
  Sequence* _seqLithologies;
  Sequence* _seqFossils;
  Sequence* _seqProfiles;
  Sequence* _seqSedimentStructures;
  Sequence* _seqCustomSymbols;
  Sequence* _seqColors;
  Sequence* _seqBeddingTypes;
  Sequence* _seqBoundaryTypes;
  Sequence* _seqOutcropQualities;
  Sequence* _seqFacies;
  Sequence* _seqLithologicalUnitTypes;
  Sequence* _seqLithologicalUnits;
  Sequence* _seqGrainSizeModes;
  Sequence* _seqGrainSizes;
  Sequence* _seqBeds;

  Table* _tLithologies;
  TableColumn* _lithologiesLithologyId;

  Table* _tFossils;
  TableColumn* _fossilsFossilId;

  Table* _tSedimentStructures;
  TableColumn* _sedimentStructuresSedimentStructureId;

  Table* _tCustomSymbols;
  TableColumn* _customSymbolsCustomSymbolId;

  Table* _tColors;
  TableColumn* _colorsColorId;

  Table* _tBeddingTypes;
  TableColumn* _beddingTypesBeddingTypeId;

  Table* _tBoundaryTypes;
  TableColumn* _boundaryTypesBoundaryTypeId;

  Table* _tOutcropQualities;
  TableColumn* _outcropQualitiesOutcropQualityId;

  Table* _tFacies;
  TableColumn* _faciesFaciesId;

  Table* _tLithologicalUnitTypes;
  TableColumn* _lithologicalUnitTypesLithologicalUnitTypeId;

  Table* _tLithologicalUnits;
  TableColumn* _lithologicalUnitsLithologicalUnitId;
  TableColumn* _lithologicalUnitsLithologicalUnitTypeId;

  Table* _tGrainSizeModes;
  TableColumn* _grainSizeModesGrainSizeModeId;

  Table* _tGrainSizes;
  TableColumn* _grainSizesGrainSizeId;
  TableColumn* _grainSizesGrainSizeTypeId;

  Table* _tBeds;
  TableColumn* _bedsBedId;
  TableColumn* _bedsProfileId;
  TableColumn* _bedsColorId;
  TableColumn* _bedsOutcropQualityId;
  TableColumn* _bedsLithologyId;
  TableColumn* _bedsBaseGrainSizeId;
  TableColumn* _bedsTopGrainSizeId;
  TableColumn* _bedsTopBoundaryTypeId;
  TableColumn* _bedsFaciesId;
  TableColumn* _bedsLithologicalUnitId;
  
  Table* _tProjects;
  TableColumn* _projectsProjectId;

  Table* _tProfiles;
  TableColumn* _profilesProfileId;
  TableColumn* _profilesProjectId;
};

#endif
