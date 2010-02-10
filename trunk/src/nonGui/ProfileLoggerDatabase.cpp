#include "ProfileLoggerDatabase.h"

#include <QCoreApplication>

#include "Schema.h"
#include "Sequence.h"
#include "Table.h"
#include "TableColumn.h"
#include "PrimaryKey.h"
#include "UniqueConstraint.h"
#include "TextNotEmptyCheckConstraint.h"
#include "ForeignKey.h"

ProfileLoggerDatabase::ProfileLoggerDatabase(QCoreApplication* p)
  : Database(p, "profilelogger")
{
  setupSchemas();
  setupSequences();
  setupTables();
  configureTables();
  setupForeignKeys();
}

ProfileLoggerDatabase::~ProfileLoggerDatabase()
{}

void ProfileLoggerDatabase::setupSchemas()
{
  _schemaData = createSchema("data");  
}

void ProfileLoggerDatabase::setupSequences()
{
  _seqProjects = _schemaData->createSequence("seq_projects");
  _seqProfiles = _schemaData->createSequence("seq_profiles");
  _seqLithologies = _schemaData->createSequence("seq_lithologies");
  _seqFossils = _schemaData->createSequence("seq_fossils");
  _seqSedimentStructures = _schemaData->createSequence("seq_sediment_structures");
  _seqCustomSymbols = _schemaData->createSequence("seq_custom_symbols");
  _seqColors = _schemaData->createSequence("seq_colors");
  _seqBeddingTypes = _schemaData->createSequence("seq_bedding_types");
  _seqBoundaryTypes = _schemaData->createSequence("seq_boundary_types");
  _seqOutcropQualities = _schemaData->createSequence("seq_outcrop_qualities");
  _seqFacies = _schemaData->createSequence("seq_facies");
  _seqLithologicalUnitTypes = _schemaData->createSequence("seq_lithological_unit_types");
  _seqLithologicalUnits = _schemaData->createSequence("seq_lithological_units");
  _seqGrainSizeModes = _schemaData->createSequence("seq_grain_size_modes");
  _seqGrainSizes = _schemaData->createSequence("seq_grain_sizes");
  _seqBeds = _schemaData->createSequence("seq_beds");
}

void ProfileLoggerDatabase::setupTables()
{
  _tProjects = _schemaData->createTable("projects");
  _tProfiles = _schemaData->createTable("profiles");
  _tLithologies = _schemaData->createTable("lithologies");
  _tFossils = _schemaData->createTable("fossils");
  _tSedimentStructures = _schemaData->createTable("sediment_structures");
  _tCustomSymbols = _schemaData->createTable("custom_symbols");
  _tColors = _schemaData->createTable("colors");
  _tBeddingTypes = _schemaData->createTable("bedding_types");
  _tBoundaryTypes = _schemaData->createTable("boundary_types");
  _tOutcropQualities = _schemaData->createTable("outcrop_qualities");
  _tFacies = _schemaData->createTable("facies");
  _tLithologicalUnitTypes = _schemaData->createTable("lithological_unit_types");
  _tLithologicalUnits = _schemaData->createTable("lithological_units");
  _tGrainSizeModes = _schemaData->createTable("grain_size_modes");
  _tGrainSizes = _schemaData->createTable("grain_sizes");
  _tBeds = _schemaData->createTable("beds");
}

void ProfileLoggerDatabase::configureTables()
{
  configureTableProjects();
  configureTableProfiles();
  configureTableLithologies();
  configureTableFossils();
  configureTableSedimentStructures();
  configureTableCustomSymbols();
  configureTableColors();
  configureTableBeddingTypes();
  configureTableBoundaryTypes();
  configureTableOutcropQualities();
  configureTableFacies();
  configureTableLithologicalUnitTypes();
  configureTableLithologicalUnits();
  configureTableGrainSizeModes();
  configureTableGrainSizes();
  configureTableBeds();
}

void ProfileLoggerDatabase::configureTableProjects()
{
  _projectsProjectId = _tProjects->createTableColumn("id", Database::DataTypeInt);
  _projectsProjectId->setSequence(_seqProjects);
  TableColumn* n = _tProjects->createTableColumn("name", Database::DataTypeText);
  (void) _tProjects->createTableColumn("description", Database::DataTypeText);

  PrimaryKey* pk = _tProjects->createPrimaryKey("pk_projects");
  pk->add(_projectsProjectId);

  UniqueConstraint* u = _tProjects->createUniqueConstraint("u_projects_name");
  u->add(n);

  TextNotEmptyCheckConstraint* c = _tProjects->createTextNotEmptyCheckConstraint("u_projects_name_not_empty");
  c->add(n);
}

void ProfileLoggerDatabase::configureTableLithologies()
{
  _lithologiesLithologyId = _tLithologies->createTableColumn("id", Database::DataTypeInt);
  _lithologiesLithologyId->setSequence(_seqLithologies);

  TableColumn* n = _tLithologies->createTableColumn("name", Database::DataTypeText);
  (void) _tLithologies->createTableColumn("description", Database::DataTypeText);
  (void) _tLithologies->createTableColumn("svg", Database::DataTypeText);

  _tLithologies->createPrimaryKey("pk_lithologies")->add(_lithologiesLithologyId);
  _tLithologies->createUniqueConstraint("u_lithologies_name")->add(n);
  _tLithologies->createTextNotEmptyCheckConstraint("chk_lithologies_name_not_empty")->add(n);
}

void ProfileLoggerDatabase::configureTableFossils()
{
  _fossilsFossilId = _tFossils->createTableColumn("id", Database::DataTypeInt);
  _fossilsFossilId->setSequence(_seqFossils);

  TableColumn* n = _tFossils->createTableColumn("name", Database::DataTypeText);
  (void) _tFossils->createTableColumn("description", Database::DataTypeText);
  (void) _tFossils->createTableColumn("svg", Database::DataTypeText);

  _tFossils->createPrimaryKey("pk_fossils")->add(_fossilsFossilId);
  _tFossils->createUniqueConstraint("u_fossils_name")->add(n);
  _tFossils->createTextNotEmptyCheckConstraint("chk_fossils_name_not_empty")->add(n);
}

void ProfileLoggerDatabase::configureTableGrainSizeModes()
{
  _grainSizeModesGrainSizeModeId = _tGrainSizeModes->createTableColumn("id", Database::DataTypeInt);
  _grainSizeModesGrainSizeModeId->setSequence(_seqGrainSizeModes);

  TableColumn* n = _tGrainSizeModes->createTableColumn("name", Database::DataTypeText);
  (void) _tGrainSizeModes->createTableColumn("description", Database::DataTypeText);
  (void) _tGrainSizeModes->createTableColumn("c_enum_value", Database::DataTypeInt);

  _tGrainSizeModes->createPrimaryKey("pk_grainSizeModes")->add(_grainSizeModesGrainSizeModeId);
  _tGrainSizeModes->createUniqueConstraint("u_grainSizeModes_name")->add(n);
  _tGrainSizeModes->createTextNotEmptyCheckConstraint("chk_grainSizeModes_name_not_empty")->add(n);
}

void ProfileLoggerDatabase::configureTableGrainSizes()
{
  _grainSizesGrainSizeId = _tGrainSizes->createTableColumn("id", Database::DataTypeInt);
  _grainSizesGrainSizeId->setSequence(_seqGrainSizes);
  _grainSizesGrainSizeTypeId = _tGrainSizes->createTableColumn("grain_size_type_id", 
							       Database::DataTypeInt);

  TableColumn* n = _tGrainSizes->createTableColumn("name", Database::DataTypeText);
  (void) _tGrainSizes->createTableColumn("description", Database::DataTypeText); 
 
  _tGrainSizes->createPrimaryKey("pk_grain_size")->add(_grainSizesGrainSizeId);
  _tGrainSizes->createUniqueConstraint("u_grain_size_unit_name")->add(n);
  _tGrainSizes->createTextNotEmptyCheckConstraint("chk_grain_size_name_not_empty")->add(n);
}

void ProfileLoggerDatabase::configureTableLithologicalUnitTypes()
{
  _lithologicalUnitTypesLithologicalUnitTypeId = _tLithologicalUnitTypes->createTableColumn("id", Database::DataTypeInt);
  _lithologicalUnitTypesLithologicalUnitTypeId->setSequence(_seqLithologicalUnitTypes);

  TableColumn* n = _tLithologicalUnitTypes->createTableColumn("name", Database::DataTypeText);
  (void) _tLithologicalUnitTypes->createTableColumn("description", Database::DataTypeText);

  _tLithologicalUnitTypes->createPrimaryKey("pk_lithological_unit_types")->add(_lithologicalUnitTypesLithologicalUnitTypeId);
  _tLithologicalUnitTypes->createUniqueConstraint("u_lithological_unit_types_name")->add(n);
  _tLithologicalUnitTypes->createTextNotEmptyCheckConstraint("chk_lithological_unit_types_name_not_empty")->add(n);
}

void ProfileLoggerDatabase::configureTableLithologicalUnits()
{
  _lithologicalUnitsLithologicalUnitId = _tLithologicalUnits->createTableColumn("id", Database::DataTypeInt);
  _lithologicalUnitsLithologicalUnitId->setSequence(_seqLithologicalUnits);
  _lithologicalUnitsLithologicalUnitTypeId = _tLithologicalUnits->createTableColumn("lithological_unit_type_id", 
										    Database::DataTypeInt);

  TableColumn* n = _tLithologicalUnits->createTableColumn("name", Database::DataTypeText);
  (void) _tLithologicalUnits->createTableColumn("description", Database::DataTypeText);
  
  (void) _tLithologicalUnits->createTableColumn("svg", Database::DataTypeText);

  _tLithologicalUnits->createPrimaryKey("pk_lithologicalUnit")->add(_lithologicalUnitsLithologicalUnitId);
  _tLithologicalUnits->createUniqueConstraint("u_lithological_unit_name")->add(n);
  _tLithologicalUnits->createTextNotEmptyCheckConstraint("chk_lithological_unit_name_not_empty")->add(n);
}

void ProfileLoggerDatabase::configureTableFacies()
{
  _faciesFaciesId = _tFacies->createTableColumn("id", Database::DataTypeInt);
  _faciesFaciesId->setSequence(_seqFacies);

  TableColumn* n = _tFacies->createTableColumn("name", Database::DataTypeText);
  (void) _tFacies->createTableColumn("description", Database::DataTypeText);
  (void) _tFacies->createTableColumn("svg", Database::DataTypeText);

  _tFacies->createPrimaryKey("pk_facies")->add(_faciesFaciesId);
  _tFacies->createUniqueConstraint("u_facies_name")->add(n);
  _tFacies->createTextNotEmptyCheckConstraint("chk_facies_name_not_empty")->add(n);
}

void ProfileLoggerDatabase::configureTableOutcropQualities()
{
  _outcropQualitiesOutcropQualityId = _tOutcropQualities->createTableColumn("id", Database::DataTypeInt);
  _outcropQualitiesOutcropQualityId->setSequence(_seqOutcropQualities);

  TableColumn* n = _tOutcropQualities->createTableColumn("name", Database::DataTypeText);
  (void) _tOutcropQualities->createTableColumn("description", Database::DataTypeText);
  (void) _tOutcropQualities->createTableColumn("svg", Database::DataTypeText);

  _tOutcropQualities->createPrimaryKey("pk_outcropQualities")->add(_outcropQualitiesOutcropQualityId);
  _tOutcropQualities->createUniqueConstraint("u_outcrop_qualities_name")->add(n);
  _tOutcropQualities->createTextNotEmptyCheckConstraint("chk_outcrop_qualities_name_not_empty")->add(n);
}

void ProfileLoggerDatabase::configureTableBeddingTypes()
{
  _beddingTypesBeddingTypeId = _tBeddingTypes->createTableColumn("id", Database::DataTypeInt);
  _beddingTypesBeddingTypeId->setSequence(_seqBeddingTypes);

  TableColumn* n = _tBeddingTypes->createTableColumn("name", Database::DataTypeText);
  (void) _tBeddingTypes->createTableColumn("description", Database::DataTypeText);
  (void) _tBeddingTypes->createTableColumn("svg", Database::DataTypeText);

  _tBeddingTypes->createPrimaryKey("pk_bedding_types")->add(_beddingTypesBeddingTypeId);
  _tBeddingTypes->createUniqueConstraint("u_bedding_types_name")->add(n);
  _tBeddingTypes->createTextNotEmptyCheckConstraint("chk_bedding_types_name_not_empty")->add(n);
}

void ProfileLoggerDatabase::configureTableBoundaryTypes()
{
  _boundaryTypesBoundaryTypeId = _tBoundaryTypes->createTableColumn("id", Database::DataTypeInt);
  _boundaryTypesBoundaryTypeId->setSequence(_seqBoundaryTypes);

  TableColumn* n = _tBoundaryTypes->createTableColumn("name", Database::DataTypeText);
  (void) _tBoundaryTypes->createTableColumn("description", Database::DataTypeText);
  (void) _tBoundaryTypes->createTableColumn("svg", Database::DataTypeText);

  _tBoundaryTypes->createPrimaryKey("pk_boundary_types")->add(_boundaryTypesBoundaryTypeId);
  _tBoundaryTypes->createUniqueConstraint("u_boundary_types_name")->add(n);
  _tBoundaryTypes->createTextNotEmptyCheckConstraint("chk_boundary_types_name_not_empty")->add(n);
}

void ProfileLoggerDatabase::configureTableColors()
{
  _colorsColorId = _tColors->createTableColumn("id", Database::DataTypeInt);
  _colorsColorId->setSequence(_seqColors);

  TableColumn* n = _tColors->createTableColumn("name", Database::DataTypeText);
  (void) _tColors->createTableColumn("description", Database::DataTypeText);
  (void) _tColors->createTableColumn("qt_brush_pattern_id", Database::DataTypeInt);

  _tColors->createPrimaryKey("pk_colors")->add(_colorsColorId);
  _tColors->createUniqueConstraint("u_colors_name")->add(n);
  _tColors->createTextNotEmptyCheckConstraint("chk_colors_name_not_empty")->add(n);
}

void ProfileLoggerDatabase::configureTableCustomSymbols()
{
  _customSymbolsCustomSymbolId = _tCustomSymbols->createTableColumn("id", Database::DataTypeInt);
  _customSymbolsCustomSymbolId->setSequence(_seqCustomSymbols);

  TableColumn* n = _tCustomSymbols->createTableColumn("name", Database::DataTypeText);
  (void) _tCustomSymbols->createTableColumn("description", Database::DataTypeText);
  (void) _tCustomSymbols->createTableColumn("svg", Database::DataTypeText);

  _tCustomSymbols->createPrimaryKey("pk_custom_symbols")->add(_customSymbolsCustomSymbolId);
  _tCustomSymbols->createUniqueConstraint("u_custom_symbols_name")->add(n);
  _tCustomSymbols->createTextNotEmptyCheckConstraint("chk_custom_symbols_name_not_empty")->add(n);
}

void ProfileLoggerDatabase::configureTableSedimentStructures()
{
  _sedimentStructuresSedimentStructureId = _tSedimentStructures->createTableColumn("id", Database::DataTypeInt);
  _sedimentStructuresSedimentStructureId->setSequence(_seqSedimentStructures);

  TableColumn* n = _tSedimentStructures->createTableColumn("name", Database::DataTypeText);
  (void) _tSedimentStructures->createTableColumn("description", Database::DataTypeText);
  (void) _tSedimentStructures->createTableColumn("svg", Database::DataTypeText);

  _tSedimentStructures->createPrimaryKey("pk_sediment_tructures")->add(_sedimentStructuresSedimentStructureId);
  _tSedimentStructures->createUniqueConstraint("u_sediment_tructures_name")->add(n);
  _tSedimentStructures->createTextNotEmptyCheckConstraint("chk_sediment_structures_name_not_empty")->add(n);
}

void ProfileLoggerDatabase::configureTableProfiles()
{
  _profilesProfileId = _tProfiles->createTableColumn("id", Database::DataTypeInt);
  _profilesProfileId->setSequence(_seqProfiles);

  TableColumn* n = _tProfiles->createTableColumn("name", Database::DataTypeText);
  (void) _tProfiles->createTableColumn("description", Database::DataTypeText);
  _profilesProjectId = _tProfiles->createTableColumn("project_id", Database::DataTypeInt);

  _tProfiles->createPrimaryKey("pk_profiles")->add(_profilesProfileId);
  _tProfiles->createTextNotEmptyCheckConstraint("chk_profiles_name_not_empty")->add(n);
  UniqueConstraint* u = _tProfiles->createUniqueConstraint("u_profile_name_in_project");
  u->add(n);
  u->add(_profilesProjectId);
}

void ProfileLoggerDatabase::configureTableBeds()
{
  _bedsBedId = _tBeds->createTableColumn("id", Database::DataTypeInt);
  _bedsBedId->setSequence(_seqBeds);

  _bedsProfileId = _tBeds->createTableColumn("profile_id", Database::DataTypeInt);
  _bedsColorId = _tBeds->createTableColumn("color_id", Database::DataTypeInt);
  _bedsOutcropQualityId = _tBeds->createTableColumn("outcrop_quality_id", Database::DataTypeInt);
  _bedsLithologyId = _tBeds->createTableColumn("lithology_id", Database::DataTypeInt);
  _bedsBaseGrainSizeId = _tBeds->createTableColumn("base_grain_size_id", Database::DataTypeInt);
  _bedsTopGrainSizeId = _tBeds->createTableColumn("top_grain_size_id", Database::DataTypeInt);  
  _bedsTopBoundaryTypeId = _tBeds->createTableColumn("top_boundary_type_id", Database::DataTypeInt);
  _bedsFaciesId = _tBeds->createTableColumn("facies_id", Database::DataTypeInt);
  _bedsLithologicalUnitId = _tBeds->createTableColumn("lithological_unit_id", Database::DataTypeInt);

  TableColumn* n = _tBeds->createTableColumn("name", Database::DataTypeText);
  (void) _tBeds->createTableColumn("description", Database::DataTypeText);
  (void) _tBeds->createTableColumn("svg", Database::DataTypeText);

  _tBeds->createPrimaryKey("pk_beds")->add(_bedsBedId);
  _tBeds->createUniqueConstraint("u_beds_name")->add(n);
  _tBeds->createTextNotEmptyCheckConstraint("chk_beds_name_not_empty")->add(n);
}
void ProfileLoggerDatabase::setupForeignKeys()
{
  _tProfiles->createForeignKey("fk_profiles_project_exists")->setColumns(_profilesProjectId, _projectsProjectId);
  _tLithologicalUnits->createForeignKey("fk_lithological_units_type_exists")->setColumns(_lithologicalUnitsLithologicalUnitTypeId,
											 _lithologicalUnitTypesLithologicalUnitTypeId);
  _tGrainSizes->createForeignKey("fk_grain_sizes_mode_exists")->setColumns(_grainSizesGrainSizeTypeId,
									   _grainSizeModesGrainSizeModeId);
  _tBeds->createForeignKey("fk_beds_profile_exists")->setColumns(_bedsProfileId,
								 _profilesProfileId);
  _tBeds->createForeignKey("fk_beds_color_exists")->setColumns(_bedsColorId,
							       _colorsColorId);
  _tBeds->createForeignKey("fk_beds_outcrop_quality_exists")->setColumns(_bedsOutcropQualityId,
									 _outcropQualitiesOutcropQualityId);
  _tBeds->createForeignKey("fk_beds_lithology_exists")->setColumns(_bedsLithologyId,
								   _lithologiesLithologyId);
  _tBeds->createForeignKey("fk_beds_base_grain_size_exists")->setColumns(_bedsBaseGrainSizeId,
									 _grainSizesGrainSizeId);
  _tBeds->createForeignKey("fk_beds_top_grain_size_exists")->setColumns(_bedsTopGrainSizeId,
									_grainSizesGrainSizeId);
  _tBeds->createForeignKey("fk_beds_top_boundary_type_exists")->setColumns(_bedsTopBoundaryTypeId,
									   _boundaryTypesBoundaryTypeId);
  _tBeds->createForeignKey("fk_beds_facies_exists")->setColumns(_bedsFaciesId,
								_faciesFaciesId);
  _tBeds->createForeignKey("fk_beds_lithological_unit_exists")->setColumns(_bedsLithologicalUnitId,
									   _lithologicalUnitsLithologicalUnitId);

}
