from Model import *
from DataType import *
from TemplateFile import *

class MyModel(Model):
    def __init__(self):
        Model.__init__(self, 'Model')
        self.setupDataTypes()
        self.setupDatabases()
        self.setupPythonModules()
    def setupDataTypes(self):
        self.createDataType('Integer')
        self.createDataType('Unicode')
        self.createDataType('Float')
        self.createDataType('Date')
        self.createDataType('Time')
        self.createDataType('Timestamp')
    def setupDatabases(self):
        self.createDatabase('profilelogger')
        self.setupTablesInProfileLogger()
    def setupTablesInProfileLogger(self):
        db = self.createDatabase('profilelogger')
        s = db.createSchema('data')
        self.setupTableGraphicPrimitives(s)
        self.setupTableLengthUnits(s)
        self.setupTableProjects(s)
        self.setupTableProfiles(s)
        self.setupTableProfileColumns(s)
        self.setupTableProfileColumnsInProfile(s)
        self.setupTableBeds(s)
        self.setupTableColors(s)
        self.setupTableColorsInBed(s)
        self.setupTableOutcropTypes(s)
        self.setupTableOutcropTypesInBed(s)
        self.setupTableFacies(s)
        self.setupTableFaciesInBed(s)
        self.setupTableLithologies(s)
        self.setupTableLithologiesInBed(s)
        self.setupTableTectonicUnitTypes(s)
        self.setupTableTectonicUnits(s)
        self.setupTableTectonicUnitsInBed(s)
        self.setupTableGrainSizeTypes(s)
        self.setupTableGrainSizes(s)
        self.setupTableGrainSizesInBed(s)
        self.setupTableLithologicUnitTypes(s)
        self.setupTableLithologicUnits(s)
        self.setupTableLithologicUnitsInBed(s)
        self.setupTableSedimentologicUnitTypes(s)
        self.setupTableSedimentologicUnits(s)
        self.setupTableSedimentologicUnitsInBed(s)
        self.setupTableStratigraphicUnitTypes(s)
        self.setupTableStratigraphicUnits(s)
        self.setupTableStratigraphicUnitsInBed(s)
        self.setupTableFossils(s)
        self.setupTableFossilsInBed(s)
        self.setupTableBeddingTypes(s)
        self.setupTableBeddingTypesInBed(s)
        self.setupTableBoundaryTypes(s)
        self.setupTableBoundaryTypesInBed(s)
        self.setupTableSedimentStructures(s)
        self.setupTableSedimentStructuresInBed(s)
        self.setupTableCustomSymbols(s)
        self.setupTableCustomSymbolsInBed(s)
        self.setupTableFieldBooks(s)
        self.setupTableFieldBookEntries(s)
    def setupTableProfileColumns(self, s):
        t = s.createTable('profile_columns', hasNameColumn=True, nameColumnIsUnique=True, hasDescriptionColumn=True)
    def setupTableProfileColumnsInProfile(self, s):
        t = s.createTable('profile_columns_in_profiles')
        t.createColumn('profile_id', nullable=False, referencedColumn=s.table('profiles').column('id'))
        t.createColumn('profile_column_id', nullable=False, referencedColumn=s.table('profile_columns').column('id'))
        t.createColumn('position', self.dataType('Integer'), nullable=False, defaultValue=0)
    def setupTableGraphicPrimitives(self, s):
        t = s.createTable('graphic_primitives', hasNameColumn=True, nameColumnIsUnique=True, hasDescriptionColumn=True)
        t.createColumn('svg_data', self.dataType('Unicode'), nullable=False, defaultText='')
        t.createColumn('original_path', self.dataType('Unicode'), nullable=False, defaultText='')
    def setupTableTectonicUnitTypes(self, s):
        t = s.createTable('tectonic_unit_types', hasNameColumn=True, nameColumnIsUnique=True, hasDescriptionColumn=True)
        t.createColumn('project_id', nullable=False, referencedColumn=s.table('projects').column('id'))
        t.createUniqueConstraint('u_tectonic_unit_types_name', [t.column('name')])
    def setupTableTectonicUnits(self, s):
        t = s.createTable('tectonic_units', hasNameColumn=True, hasDescriptionColumn=True)
        t.createColumn('project_id', nullable=False, referencedColumn=s.table('projects').column('id'))
        t.createColumn('tectonic_unit_type_id', nullable=False, referencedColumn=s.table('tectonic_unit_types').column('id'))
        t.createColumn('graphic_primitive_id', nullable=False, referencedColumn=s.table('graphic_primitives').column('id'))
        t.createUniqueConstraint('u_tectonic_unit_in_project', [t.column('name'), t.column('project_id')])
    def setupTableTectonicUnitsInBed(self, s):
        t = s.createTable('tectonic_units_in_beds', hasDescriptionColumn=True)
        t.createColumn('base', self.dataType('Integer'), nullable=False, defaultValue=0)
        t.createColumn('top', self.dataType('Integer'), nullable=False, defaultValue=100)
        t.createColumn('bed_id', nullable=False, referencedColumn=s.table('beds').column('id'))
        t.createColumn('tectonic_unit_id', nullable=False, referencedColumn=s.table('tectonic_units').column('id'))
        t.createRangeCheckConstraint('chk_tectonic_units_in_beds_base_in_range', t.column('base'), 0, 100)
        t.createRangeCheckConstraint('chk_tectonic_units_in_beds_top_in_range', t.column('top'), 0, 100)
    def setupTableGrainSizeTypes(self, s):
        t = s.createTable('grain_size_types', hasNameColumn=True, nameColumnIsUnique=True, hasDescriptionColumn=True)
        t.createColumn('project_id', nullable=False, referencedColumn=s.table('projects').column('id'))
        t.createUniqueConstraint('u_grain_size_types_name', [t.column('name')])
    def setupTableGrainSizes(self, s):
        t = s.createTable('grain_sizes', hasNameColumn=True, hasDescriptionColumn=True)
        t.createColumn('project_id', nullable=False, referencedColumn=s.table('projects').column('id'))
        t.createColumn('grain_size_type_id', nullable=False, referencedColumn=s.table('grain_size_types').column('id'))
        t.createColumn('graphic_primitive_id', nullable=False, referencedColumn=s.table('graphic_primitives').column('id'))
        t.createColumn('percent_from_max', self.dataType('Integer'), nullable=False, defaultValue=0)
        t.createUniqueConstraint('u_grain_size_in_project', [t.column('name'), t.column('project_id')])
        t.createRangeCheckConstraint('chk_grain_sizes_percent_from_max_range', t.column('percent_from_max'), 0, 100)
    def setupTableGrainSizesInBed(self, s):
        t = s.createTable('grain_sizes_in_beds', hasDescriptionColumn=True)
        t.createColumn('base', self.dataType('Integer'), nullable=False, defaultValue=0)
        t.createColumn('top', self.dataType('Integer'), nullable=False, defaultValue=100)
        t.createColumn('bed_id', nullable=False, referencedColumn=s.table('beds').column('id'))
        t.createColumn('grain_size_id', nullable=False, referencedColumn=s.table('grain_sizes').column('id'))
        t.createRangeCheckConstraint('chk_grain_sizes_in_beds_base_in_range', t.column('base'), 0, 100)
        t.createRangeCheckConstraint('chk_grain_sizes_in_beds_top_in_range', t.column('top'), 0, 100)
    def setupTableLithologicUnitTypes(self, s):
        t = s.createTable('lithologic_unit_types', hasNameColumn=True, nameColumnIsUnique=True, hasDescriptionColumn=True)
        t.createColumn('project_id', nullable=False, referencedColumn=s.table('projects').column('id'))
        t.createUniqueConstraint('u_lithologic_unit_types_name', [t.column('name')])
    def setupTableLithologicUnits(self, s):
        t = s.createTable('lithologic_units', hasNameColumn=True, hasDescriptionColumn=True)
        t.createColumn('project_id', nullable=False, referencedColumn=s.table('projects').column('id'))
        t.createColumn('lithologic_unit_type_id', nullable=False, referencedColumn=s.table('lithologic_unit_types').column('id'))
        t.createColumn('graphic_primitive_id', nullable=False, referencedColumn=s.table('graphic_primitives').column('id'))
        t.createUniqueConstraint('u_lithologic_unit_in_project', [t.column('name'), t.column('project_id')])
    def setupTableLithologicUnitsInBed(self, s):
        t = s.createTable('lithologic_units_in_beds', hasDescriptionColumn=True)
        t.createColumn('base', self.dataType('Integer'), nullable=False, defaultValue=0)
        t.createColumn('top', self.dataType('Integer'), nullable=False, defaultValue=100)
        t.createColumn('bed_id', nullable=False, referencedColumn=s.table('beds').column('id'))
        t.createColumn('lithologic_unit_id', nullable=False, referencedColumn=s.table('lithologic_units').column('id'))
        t.createRangeCheckConstraint('chk_lithologic_units_in_beds_base_in_range', t.column('base'), 0, 100)
        t.createRangeCheckConstraint('chk_lithologic_units_in_beds_top_in_range', t.column('top'), 0, 100)
    def setupTableSedimentologicUnitTypes(self, s):
        t = s.createTable('sedimentologic_unit_types', hasNameColumn=True, nameColumnIsUnique=True, hasDescriptionColumn=True)
        t.createColumn('project_id', nullable=False, referencedColumn=s.table('projects').column('id'))
        t.createUniqueConstraint('u_sedimentologic_unit_types_name', [t.column('name')])
    def setupTableSedimentologicUnits(self, s):
        t = s.createTable('sedimentologic_units', hasNameColumn=True, hasDescriptionColumn=True)
        t.createColumn('project_id', nullable=False, referencedColumn=s.table('projects').column('id'))
        t.createColumn('sedimentologic_unit_type_id', nullable=False, referencedColumn=s.table('sedimentologic_unit_types').column('id'))
        t.createColumn('graphic_primitive_id', nullable=False, referencedColumn=s.table('graphic_primitives').column('id'))
        t.createUniqueConstraint('u_sedimentologic_unit_in_project', [t.column('name'), t.column('project_id')])
    def setupTableSedimentologicUnitsInBed(self, s):
        t = s.createTable('sedimentologic_units_in_beds', hasDescriptionColumn=True)
        t.createColumn('base', self.dataType('Integer'), nullable=False, defaultValue=0)
        t.createColumn('top', self.dataType('Integer'), nullable=False, defaultValue=100)
        t.createColumn('bed_id', nullable=False, referencedColumn=s.table('beds').column('id'))
        t.createColumn('sedimentologic_unit_id', nullable=False, referencedColumn=s.table('sedimentologic_units').column('id'))
        t.createRangeCheckConstraint('chk_sedimentologic_units_in_beds_base_in_range', t.column('base'), 0, 100)
        t.createRangeCheckConstraint('chk_sedimentologic_units_in_beds_top_in_range', t.column('top'), 0, 100)
    def setupTableStratigraphicUnitTypes(self, s):
        t = s.createTable('stratigraphic_unit_types', hasNameColumn=True, nameColumnIsUnique=True, hasDescriptionColumn=True)
        t.createColumn('project_id', nullable=False, referencedColumn=s.table('projects').column('id'))
        t.createUniqueConstraint('u_stratigraphic_unit_types_name', [t.column('name')])
    def setupTableStratigraphicUnits(self, s):
        t = s.createTable('stratigraphic_units', hasNameColumn=True, hasDescriptionColumn=True)
        t.createColumn('project_id', nullable=False, referencedColumn=s.table('projects').column('id'))
        t.createColumn('stratigraphic_unit_type_id', nullable=False, referencedColumn=s.table('stratigraphic_unit_types').column('id'))
        t.createColumn('graphic_primitive_id', nullable=False, referencedColumn=s.table('graphic_primitives').column('id'))
        t.createUniqueConstraint('u_stratigraphic_unit_in_project', [t.column('name'), t.column('project_id')])
    def setupTableStratigraphicUnitsInBed(self, s):
        t = s.createTable('stratigraphic_units_in_beds', hasDescriptionColumn=True)
        t.createColumn('base', self.dataType('Integer'), nullable=False, defaultValue=0)
        t.createColumn('top', self.dataType('Integer'), nullable=False, defaultValue=100)
        t.createColumn('bed_id', nullable=False, referencedColumn=s.table('beds').column('id'))
        t.createColumn('stratigraphic_unit_id', nullable=False, referencedColumn=s.table('stratigraphic_units').column('id'))
        t.createRangeCheckConstraint('chk_stratigraphic_units_in_beds_base_in_range', t.column('base'), 0, 100)
        t.createRangeCheckConstraint('chk_stratigraphic_units_in_beds_top_in_range', t.column('top'), 0, 100)
    def setupTableColors(self, s):
        t = s.createTable('colors', hasNameColumn=True, hasDescriptionColumn=True)
        t.createColumn('project_id', nullable=False, referencedColumn=s.table('projects').column('id'))
        t.createColumn('graphic_primitive_id', nullable=False, referencedColumn=s.table('graphic_primitives').column('id'))
        t.createUniqueConstraint('u_colors_name', [t.column('name'), t.column('project_id'), ])
    def setupTableColorsInBed(self, s):
        t = s.createTable('colors_in_beds', hasDescriptionColumn=True)
        t.createColumn('base', self.dataType('Integer'), nullable=False, defaultValue=0)
        t.createColumn('top', self.dataType('Integer'), nullable=False, defaultValue=100)
        t.createColumn('bed_id', nullable=False, referencedColumn=s.table('beds').column('id'))
        t.createColumn('color_id', nullable=False, referencedColumn=s.table('colors').column('id'))
        t.createRangeCheckConstraint('chk_colors_in_beds_base_in_range', t.column('base'), 0, 100)
        t.createRangeCheckConstraint('chk_colors_in_beds_top_in_range', t.column('top'), 0, 100)
    def setupTableOutcropTypes(self, s):
        t = s.createTable('outcrop_types', hasNameColumn=True, hasDescriptionColumn=True)
        t.createColumn('project_id', nullable=False, referencedColumn=s.table('projects').column('id'))
        t.createColumn('graphic_primitive_id', nullable=False, referencedColumn=s.table('graphic_primitives').column('id'))
        t.createUniqueConstraint('u_outcrop_types_name', [t.column('name'), t.column('project_id'), ])
    def setupTableOutcropTypesInBed(self, s):
        t = s.createTable('outcrop_types_in_beds', hasDescriptionColumn=True)
        t.createColumn('base', self.dataType('Integer'), nullable=False, defaultValue=0)
        t.createColumn('top', self.dataType('Integer'), nullable=False, defaultValue=100)
        t.createColumn('bed_id', nullable=False, referencedColumn=s.table('beds').column('id'))
        t.createColumn('outcrop_type_id', nullable=False, referencedColumn=s.table('outcrop_types').column('id'))
        t.createRangeCheckConstraint('chk_outcrop_types_in_beds_base_in_range', t.column('base'), 0, 100)
        t.createRangeCheckConstraint('chk_outcrop_types_in_beds_top_in_range', t.column('top'), 0, 100)
    def setupTableFacies(self, s):
        t = s.createTable('facies', hasNameColumn=True, hasDescriptionColumn=True)
        t.createColumn('project_id', nullable=False, referencedColumn=s.table('projects').column('id'))
        t.createColumn('graphic_primitive_id', nullable=False, referencedColumn=s.table('graphic_primitives').column('id'))
        t.createUniqueConstraint('u_facies_name', [t.column('name'), t.column('project_id'), ])
    def setupTableFaciesInBed(self, s):
        t = s.createTable('facies_in_beds', hasDescriptionColumn=True)
        t.createColumn('base', self.dataType('Integer'), nullable=False, defaultValue=0)
        t.createColumn('top', self.dataType('Integer'), nullable=False, defaultValue=100)
        t.createColumn('bed_id', nullable=False, referencedColumn=s.table('beds').column('id'))
        t.createColumn('facies_id', nullable=False, referencedColumn=s.table('facies').column('id'))
        t.createRangeCheckConstraint('chk_facies_in_beds_base_in_range', t.column('base'), 0, 100)
        t.createRangeCheckConstraint('chk_facies_in_beds_top_in_range', t.column('top'), 0, 100)
    def setupTableLithologies(self, s):
        t = s.createTable('lithologies', hasNameColumn=True, hasDescriptionColumn=True)
        t.createColumn('project_id', nullable=False, referencedColumn=s.table('projects').column('id'))
        t.createColumn('graphic_primitive_id', nullable=False, referencedColumn=s.table('graphic_primitives').column('id'))
        t.createUniqueConstraint('u_lithologies_name', [t.column('name'), t.column('project_id'), ])
    def setupTableLithologiesInBed(self, s):
        t = s.createTable('lithologies_in_beds', hasDescriptionColumn=True)
        t.createColumn('base', self.dataType('Integer'), nullable=False, defaultValue=0)
        t.createColumn('top', self.dataType('Integer'), nullable=False, defaultValue=100)
        t.createColumn('bed_id', nullable=False, referencedColumn=s.table('beds').column('id'))
        t.createColumn('lithology_id', nullable=False, referencedColumn=s.table('lithologies').column('id'))
        t.createRangeCheckConstraint('chk_lithologies_in_beds_base_in_range', t.column('base'), 0, 100)
        t.createRangeCheckConstraint('chk_lithologies_in_beds_top_in_range', t.column('top'), 0, 100)
    def setupTableFossils(self, s):
        t = s.createTable('fossils', hasNameColumn=True, hasDescriptionColumn=True)
        t.createColumn('project_id', nullable=False, referencedColumn=s.table('projects').column('id'))
        t.createColumn('graphic_primitive_id', nullable=False, referencedColumn=s.table('graphic_primitives').column('id'))
        t.createUniqueConstraint('u_fossils_name', [t.column('name'), t.column('project_id'), ])
    def setupTableFossilsInBed(self, s):
        t = s.createTable('fossils_in_beds', hasDescriptionColumn=True)
        t.createColumn('base', self.dataType('Integer'), nullable=False, defaultValue=0)
        t.createColumn('top', self.dataType('Integer'), nullable=False, defaultValue=100)
        t.createColumn('bed_id', nullable=False, referencedColumn=s.table('beds').column('id'))
        t.createColumn('fossil_id', nullable=False, referencedColumn=s.table('fossils').column('id'))
        t.createRangeCheckConstraint('chk_fossils_in_beds_base_in_range', t.column('base'), 0, 100)
        t.createRangeCheckConstraint('chk_fossils_in_beds_top_in_range', t.column('top'), 0, 100)
    def setupTableBeddingTypes(self, s):
        t = s.createTable('bedding_types', hasNameColumn=True, hasDescriptionColumn=True)
        t.createColumn('project_id', nullable=False, referencedColumn=s.table('projects').column('id'))
        t.createColumn('graphic_primitive_id', nullable=False, referencedColumn=s.table('graphic_primitives').column('id'))
        t.createUniqueConstraint('u_bedding_types_name', [t.column('name'), t.column('project_id'), ])
    def setupTableBeddingTypesInBed(self, s):
        t = s.createTable('bedding_types_in_beds', hasDescriptionColumn=True)
        t.createColumn('base', self.dataType('Integer'), nullable=False, defaultValue=0)
        t.createColumn('top', self.dataType('Integer'), nullable=False, defaultValue=100)
        t.createColumn('bed_id', nullable=False, referencedColumn=s.table('beds').column('id'))
        t.createColumn('bedding_type_id', nullable=False, referencedColumn=s.table('bedding_types').column('id'))
        t.createRangeCheckConstraint('chk_bedding_types_in_beds_base_in_range', t.column('base'), 0, 100)
        t.createRangeCheckConstraint('chk_bedding_types_in_beds_top_in_range', t.column('top'), 0, 100)
    def setupTableBoundaryTypes(self, s):
        t = s.createTable('boundary_types', hasNameColumn=True, hasDescriptionColumn=True)
        t.createColumn('project_id', nullable=False, referencedColumn=s.table('projects').column('id'))
        t.createColumn('graphic_primitive_id', nullable=False, referencedColumn=s.table('graphic_primitives').column('id'))
        t.createUniqueConstraint('u_boundary_types_name', [t.column('name'), t.column('project_id'), ])
    def setupTableBoundaryTypesInBed(self, s):
        t = s.createTable('boundary_types_in_beds', hasDescriptionColumn=True)
        t.createColumn('base', self.dataType('Integer'), nullable=False, defaultValue=0)
        t.createColumn('top', self.dataType('Integer'), nullable=False, defaultValue=100)
        t.createColumn('bed_id', nullable=False, referencedColumn=s.table('beds').column('id'))
        t.createColumn('boundary_type_id', nullable=False, referencedColumn=s.table('boundary_types').column('id'))
        t.createRangeCheckConstraint('chk_boundary_types_in_beds_base_in_range', t.column('base'), 0, 100)
        t.createRangeCheckConstraint('chk_boundary_types_in_beds_top_in_range', t.column('top'), 0, 100)
    def setupTableSedimentStructures(self, s):
        t = s.createTable('sediment_structures', hasNameColumn=True, hasDescriptionColumn=True)
        t.createColumn('project_id', nullable=False, referencedColumn=s.table('projects').column('id'))
        t.createColumn('graphic_primitive_id', nullable=False, referencedColumn=s.table('graphic_primitives').column('id'))
        t.createUniqueConstraint('u_sediment_structures_name', [t.column('name'), t.column('project_id'), ])
    def setupTableSedimentStructuresInBed(self, s):
        t = s.createTable('sediment_structures_in_beds', hasDescriptionColumn=True)
        t.createColumn('base', self.dataType('Integer'), nullable=False, defaultValue=0)
        t.createColumn('top', self.dataType('Integer'), nullable=False, defaultValue=100)
        t.createColumn('bed_id', nullable=False, referencedColumn=s.table('beds').column('id'))
        t.createColumn('sediment_structure_id', nullable=False, referencedColumn=s.table('sediment_structures').column('id'))
        t.createRangeCheckConstraint('chk_sediment_structures_in_beds_base_in_range', t.column('base'), 0, 100)
        t.createRangeCheckConstraint('chk_sediment_structures_in_beds_top_in_range', t.column('top'), 0, 100)
    def setupTableCustomSymbols(self, s):
        t = s.createTable('custom_symbols', hasNameColumn=True, hasDescriptionColumn=True)
        t.createColumn('project_id', nullable=False, referencedColumn=s.table('projects').column('id'))
        t.createColumn('graphic_primitive_id', nullable=False, referencedColumn=s.table('graphic_primitives').column('id'))
        t.createUniqueConstraint('u_custom_symbols_name', [t.column('name'), t.column('project_id'), ])
    def setupTableCustomSymbolsInBed(self, s):
        t = s.createTable('custom_symbols_in_beds', hasDescriptionColumn=True)
        t.createColumn('base', self.dataType('Integer'), nullable=False, defaultValue=0)
        t.createColumn('top', self.dataType('Integer'), nullable=False, defaultValue=100)
        t.createColumn('bed_id', nullable=False, referencedColumn=s.table('beds').column('id'))
        t.createColumn('custom_symbol_id', nullable=False, referencedColumn=s.table('custom_symbols').column('id'))
        t.createRangeCheckConstraint('chk_custom_symbols_in_beds_base_in_range', t.column('base'), 0, 100)
        t.createRangeCheckConstraint('chk_custom_symbols_in_beds_top_in_range', t.column('top'), 0, 100)
    def setupTableLengthUnits(self, s):
        t = s.createTable('length_units', hasNameColumn=True, nameColumnIsUnique=True, hasDescriptionColumn=True)
        t.createColumn('micro_metres', self.dataType('Integer'), nullable=False, defaultValue=0, isUnique=True)
    def setupTableBeds(self, s):
        t = s.createTable('beds', hasDescriptionColumn=True)
        t.createColumn('position', self.dataType('Integer'), nullable=False)
        t.createColumn('bed_number', self.dataType('Unicode'), nullable=False, isUnique=True, notEmpty=True)
        t.createColumn('profile_id', nullable=False, referencedColumn=s.table('projects').column('id'))
        t.createColumn('height', self.dataType('Integer'), nullable=False, defaultValue=0)
        t.createColumn('height_length_unit_id', nullable=False, referencedColumn=s.table('length_units').column('id'))
        t.createUniqueConstraint('u_bed_number_in_profile', [t.column('profile_id'), t.column('bed_number'),])
    def setupTableFieldBookEntries(self, s):
        t = s.createTable('field_book_entries')
        t.createColumn('field_book_id', nullable=False, referencedColumn=s.table('projects').column('id'))
    def setupTableFieldBooks(self, s):
        t = s.createTable('field_books', hasDescriptionColumn=True)
        t.createColumn('title', self.dataType('Unicode'), defaultText='new field book', notEmpty=True)
    def setupTableProjects(self, s):
        t = s.createTable('projects', hasNameColumn=True, hasDescriptionColumn=True)
    def setupTableProfiles(self, s):
        t = s.createTable('profiles', hasNameColumn=True, hasDescriptionColumn=True)
        t.createColumn('project_id', nullable=False, referencedColumn=s.table('projects').column('id'))
        t.createUniqueConstraint('u_profile_name_in_project', [t.column('project_id'), t.column('name'),])
    def setupPythonModules(self):
        logic = self.createPythonModule('Logic')
        self.pythonDataModule = logic.createPythonModule('Model')
        finders = logic.createPythonModule('Finders')
        presistance = logic.createPythonModule('Persistance')
        gui = self.createPythonModule('Gui')
        self.comboBoxModule = gui.createPythonModule('ComboBoxes')
        self.itemModelModule = gui.createPythonModule('ItemModels')
        self.treeViewModule = gui.createPythonModule('TreeViews')
        self.managementDialogModule = gui.createPythonModule('ManagementDialogs')
        self.editorDialogModule = gui.createPythonModule('EditorDialogs')
        self.setupDataClasses(self.pythonDataModule)
        self.setupFinderModule(finders)
        self.setupComboBoxModule(self.comboBoxModule)
        self.setupItemModelModule(self.itemModelModule)
        self.setupTreeViewModule(self.treeViewModule)
        self.setupManagementDialogModule(self.managementDialogModule)
        self.setupEditorDialogModule(self.editorDialogModule)
    def setupEditorDialogModule(self, module):
        globalTmpl = TemplateFile('templates/Gui/EditorDialogs/EditorDialogTemplate.py')
        self.createEditorDialogClasses(module, [['GraphicPrimitive', globalTmpl, ],
                                                ['Project', globalTmpl, ],
                                                ['LengthUnit', globalTmpl, ],
                                                ['Profile', globalTmpl, ],
                                                ['ProfileColumn', globalTmpl, ],
                                                ['ProfileColumnInProfile', globalTmpl, ],
                                                ['Bed', globalTmpl, ],
                                                ['Color', globalTmpl, ],
                                                ['ColorGlobal', globalTmpl, ],
                                                ['OutcropType', globalTmpl, ],
                                                ['OutcropTypeGlobal', globalTmpl, ],
                                                ['Facies', globalTmpl, ],
                                                ['FaciesGlobal', globalTmpl, ],
                                                ['Lithology', globalTmpl, ],
                                                ['LithologyGlobal', globalTmpl, ],
                                                ['TectonicUnitType', globalTmpl, ],
                                                ['TectonicUnit', globalTmpl, ],
                                                ['TectonicUnitGlobal', globalTmpl, ],
                                                ['GrainSizeType', globalTmpl, ],
                                                ['GrainSize', globalTmpl, ],
                                                ['GrainSizeGlobal', globalTmpl, ],
                                                ['LithologicUnitType', globalTmpl, ],
                                                ['LithologicUnit', globalTmpl, ],
                                                ['LithologicUnitGlobal', globalTmpl, ],
                                                ['SedimentologicUnitType', globalTmpl, ],
                                                ['SedimentologicUnit', globalTmpl, ],
                                                ['SedimentologicUnitGlobal', globalTmpl, ],
                                                ['StratigraphicUnitType', globalTmpl, ],
                                                ['StratigraphicUnit', globalTmpl, ],
                                                ['StratigraphicUnitGlobal', globalTmpl, ],
                                                ['Fossil', globalTmpl, ],
                                                ['FossilGlobal', globalTmpl, ],
                                                ['BeddingType', globalTmpl, ],
                                                ['BeddingTypeGlobal', globalTmpl, ],
                                                ['BoundaryType', globalTmpl, ],
                                                ['BoundaryTypeGlobal', globalTmpl, ],
                                                ['SedimentStructure', globalTmpl, ],
                                                ['SedimentStructureGlobal', globalTmpl, ],
                                                ['CustomSymbol', globalTmpl, ],
                                                ['CustomSymbolGlobal', globalTmpl, ],
                                                ['BeddingType', globalTmpl, ],
                                                ['BeddingTypeGlobal', globalTmpl, ],
                                                ['FieldBook', globalTmpl, ],
                                                ['FieldBookEntry', globalTmpl, ],])

    def setupManagementDialogModule(self, module):
        globalTmpl = TemplateFile('templates/Gui/ManagementDialogs/GlobalManagementDialogTemplate.py')
        inProjectTmpl = TemplateFile('templates/Gui/ManagementDialogs/InProjectManagementDialogTemplate.py')
        inProfileTmpl = TemplateFile('templates/Gui/ManagementDialogs/InProfileManagementDialogTemplate.py')
        inBedTmpl = TemplateFile('templates/Gui/ManagementDialogs/InBedManagementDialogTemplate.py')
        inFieldBookTmpl = TemplateFile('templates/Gui/ManagementDialogs/InFieldBookManagementDialogTemplate.py')
        self.createManagementDialogClasses(module, [['GraphicPrimitive', globalTmpl, 'Graphic Primitives', ],
                                                    ['Project', globalTmpl, 'Projects', ],
                                                    ['LengthUnit', globalTmpl, 'Length Units', ],        
                                                    ['FieldBook', globalTmpl, 'Field Books', ],
                                                    ['Profile', inProjectTmpl, 'Profiles', ],
                                                    ['Bed', inProfileTmpl, 'Beds', ],
                                                    ['Color', inProjectTmpl, 'Colors', ],
                                                    ['OutcropType', inProjectTmpl, 'Outcrop Types', ],
                                                    ['Facies', inProjectTmpl, 'Facies', ],
                                                    ['Lithology', inProjectTmpl, 'Lithologies', ],
                                                    ['TectonicUnitType', inProjectTmpl, 'Tectonic Unit Types', ],
                                                    ['TectonicUnit', inProjectTmpl, 'Tectonic Units', ],
                                                    ['GrainSizeType', inProjectTmpl, 'Grain Size Types', ],
                                                    ['GrainSize', inProjectTmpl, 'Grain Sizes', ],
                                                    ['LithologicUnitType', inProjectTmpl, 'Lithological Unit Types', ],
                                                    ['LithologicUnit', inProjectTmpl, 'Lithological Units', ],
                                                    ['SedimentologicUnitType', inProjectTmpl, 'Sedimentologic Unit Types', ],
                                                    ['SedimentologicUnit', inProjectTmpl, 'Sedimentologic Units', ],
                                                    ['StratigraphicUnitType', inProjectTmpl, 'Stratigraphic Unit Types', ],
                                                    ['StratigraphicUnit', inProjectTmpl, 'Stratigraphic Units', ],
                                                    ['Fossil', inProjectTmpl, 'Fossils', ],
                                                    ['BeddingType', inProjectTmpl, 'Bedding Types', ],
                                                    ['BoundaryType', inProjectTmpl, 'Boundary Types', ],
                                                    ['SedimentStructure', inProjectTmpl, 'Sediment Structures', ],
                                                    ['CustomSymbol', inProjectTmpl, 'Custom Symbols', ],
                                                    ['BeddingType', inProjectTmpl, 'Bedding Types', ],
                                                    ['ProfileColumn', inProfileTmpl, 'Profile Columns', ],
                                                    ['ProfileColumnInProfile', inProfileTmpl, 'Profile Column In Profile', ],
                                                    ['ColorInBed', inBedTmpl, 'Colors', ],
                                                    ['OutcropTypeInBed', inBedTmpl, 'Outcrop Types', ],
                                                    ['FaciesInBed', inBedTmpl, 'Facies', ],
                                                    ['LithologyInBed', inBedTmpl, 'Lithologies', ],
                                                    ['TectonicUnitInBed', inBedTmpl, 'Tectonic Units', ],
                                                    ['GrainSizeInBed', inBedTmpl, 'Grain Sizes', ],
                                                    ['LithologicUnitInBed', inBedTmpl, 'Lithologic Units', ],
                                                    ['SedimentologicUnitInBed', inBedTmpl, 'Sedimentologic Units', ],
                                                    ['StratigraphicUnitInBed', inBedTmpl, 'Stratigraphic Units', ],
                                                    ['FossilInBed', inBedTmpl, 'Fossils', ],
                                                    ['BeddingTypeInBed', inBedTmpl, 'Bedding Types', ],
                                                    ['BoundaryTypeInBed', inBedTmpl, 'Boundary Types', ],
                                                    ['SedimentStructureInBed', inBedTmpl, 'Sediment Structures', ],
                                                    ['CustomSymbolInBed', inBedTmpl, 'Custom Symbols', ],
                                                    ['BeddingTypeInBed', inBedTmpl, 'Bedding Types', ],
                                                    ['FieldBookEntry', inFieldBookTmpl, 'Field Book Entry', ],])
    def setupItemModelModule(self, module):
        globalTmpl = TemplateFile('templates/Gui/ItemModels/GlobalItemModelTemplate.py')
        inProjectTmpl = TemplateFile('templates/Gui/ItemModels/InProjectItemModelTemplate.py')
        inProfileTmpl = TemplateFile('templates/Gui/ItemModels/InProfileItemModelTemplate.py')
        inBedTmpl = TemplateFile('templates/Gui/ItemModels/InBedItemModelTemplate.py')
        inFieldBookTmpl = TemplateFile('templates/Gui/ItemModels/InFieldBookItemModelTemplate.py')

        self.createItemModelClasses(module, [['GraphicPrimitive', globalTmpl, ['Graphic Primitives', ], ],
                                                   ['Project', globalTmpl, ['Projects',], ],
                                                   ['LengthUnit', globalTmpl, ['Length Units', ], ],        
                                                   ['FieldBook', globalTmpl, ['Field Books', ], ],
                                                   ['Profile', inProjectTmpl, ['Profiles', ], ],
                                                   ['Bed', inProfileTmpl, ['Beds', ], ],
                                                   ['Color', inProjectTmpl, ['Colors', ], ],
                                                   ['OutcropType', inProjectTmpl, ['Outcrop Types', ], ],
                                                   ['Facies', inProjectTmpl, ['Facies', ], ],
                                                   ['Lithology', inProjectTmpl, ['Lithologies', ], ],
                                                   ['TectonicUnitType', inProjectTmpl, ['Tectonic Unit Types', ], ],
                                                   ['TectonicUnit', inProjectTmpl, ['Tectonic Units', ], ],
                                                   ['GrainSizeType', inProjectTmpl, ['Grain Size Types', ], ],
                                                   ['GrainSize', inProjectTmpl, ['Grain Sizes', ], ],
                                                   ['LithologicUnitType', inProjectTmpl, ['Lithological Unit Types', ], ],
                                                   ['LithologicUnit', inProjectTmpl, ['Lithological Units', ], ],
                                                   ['SedimentologicUnitType', inProjectTmpl, ['Sedimentologic Unit Types', ], ],
                                                   ['SedimentologicUnit', inProjectTmpl, ['Sedimentologic Units', ], ],
                                                   ['StratigraphicUnitType', inProjectTmpl, ['Stratigraphic Unit Types', ], ],
                                                   ['StratigraphicUnit', inProjectTmpl, ['Stratigraphic Units', ], ],
                                                   ['Fossil', inProjectTmpl, ['Fossils', ], ],
                                                   ['BeddingType', inProjectTmpl, ['Bedding Types', ], ],
                                                   ['BoundaryType', inProjectTmpl, ['Boundary Types', ], ],
                                                   ['SedimentStructure', inProjectTmpl, ['Sediment Structures', ], ],
                                                   ['CustomSymbol', inProjectTmpl, ['Custom Symbols', ], ],
                                                   ['BeddingType', inProjectTmpl, ['Bedding Types', ], ],
                                                   ['ProfileColumn', inProfileTmpl, ['Profile Columns', ], ],
                                                   ['ProfileColumnInProfile', inProfileTmpl, ['Profile Column In Profile', ], ],
                                                   ['ColorInBed', inBedTmpl, ['Colors', ], ],
                                                   ['OutcropTypeInBed', inBedTmpl, ['Outcrop Types', ], ],
                                                   ['FaciesInBed', inBedTmpl, ['Facies', ], ],
                                                   ['LithologyInBed', inBedTmpl, ['Lithologies', ], ],
                                                   ['TectonicUnitInBed', inBedTmpl, ['Tectonic Units', ], ],
                                                   ['GrainSizeInBed', inBedTmpl, ['Grain Sizes', ], ],
                                                   ['LithologicUnitInBed', inBedTmpl, ['Lithologic Units', ], ],
                                                   ['SedimentologicUnitInBed', inBedTmpl, ['Sedimentologic Units', ], ],
                                                   ['StratigraphicUnitInBed', inBedTmpl, ['Stratigraphic Units', ], ],
                                                   ['FossilInBed', inBedTmpl, ['Fossils', ], ],
                                                   ['BeddingTypeInBed', inBedTmpl, ['Bedding Types', ], ],
                                                   ['BoundaryTypeInBed', inBedTmpl, ['Boundary Types', ], ],
                                                   ['SedimentStructureInBed', inBedTmpl, ['Sediment Structures', ], ],
                                                   ['CustomSymbolInBed', inBedTmpl, ['Custom Symbols', ], ],
                                                   ['BeddingTypeInBed', inBedTmpl, ['Bedding Types', ], ],
                                                   ['FieldBookEntry', inFieldBookTmpl, ['Field Book Entry', ], ],])

    def setupTreeViewModule(self, module):
        globalTmpl = TemplateFile('templates/Gui/TreeViews/GlobalTreeViewTemplate.py')
        inProjectTmpl = TemplateFile('templates/Gui/TreeViews/InProjectManagementTreeViewTemplate.py')
        inProfileTmpl = TemplateFile('templates/Gui/TreeViews/InProfileManagementTreeViewTemplate.py')
        inBedTmpl = TemplateFile('templates/Gui/TreeViews/InBedManagementTreeViewTemplate.py')
        inFieldBookTmpl = TemplateFile('templates/Gui/TreeViews/InFieldBookManagementTreeViewTemplate.py')
        self.createTreeViewClasses(module, [['GraphicPrimitive', globalTmpl, ],
                                            ['Project', globalTmpl, ],
                                            ['LengthUnit', globalTmpl, ],        
                                            ['FieldBook', globalTmpl, ],
                                            ['Profile', inProjectTmpl, ],
                                            ['Bed', inProfileTmpl, ],
                                            ['Color', inProjectTmpl, ],
                                            ['OutcropType', inProjectTmpl, ],
                                            ['Facies', inProjectTmpl, ],
                                            ['Lithology', inProjectTmpl, ],
                                            ['TectonicUnitType', inProjectTmpl, ],
                                            ['TectonicUnit', inProjectTmpl, ],
                                            ['GrainSizeType', inProjectTmpl, ],
                                            ['GrainSize', inProjectTmpl, ],
                                            ['LithologicUnitType', inProjectTmpl, ],
                                            ['LithologicUnit', inProjectTmpl, ],
                                            ['SedimentologicUnitType', inProjectTmpl, ],
                                            ['SedimentologicUnit', inProjectTmpl, ],
                                            ['StratigraphicUnitType', inProjectTmpl, ],
                                            ['StratigraphicUnit', inProjectTmpl, ],
                                            ['Fossil', inProjectTmpl, ],
                                            ['BeddingType', inProjectTmpl, ],
                                            ['BoundaryType', inProjectTmpl, ],
                                            ['SedimentStructure', inProjectTmpl, ],
                                            ['CustomSymbol', inProjectTmpl, ],
                                            ['BeddingType', inProjectTmpl, ],
                                            ['ProfileColumn', inProfileTmpl, ],
                                            ['ProfileColumnInProfile', inProfileTmpl, ],
                                            ['ColorInBed', inBedTmpl, ],
                                            ['OutcropTypeInBed', inBedTmpl, ],
                                            ['FaciesInBed', inBedTmpl, ],
                                            ['LithologyInBed', inBedTmpl, ],
                                            ['TectonicUnitInBed', inBedTmpl, ],
                                            ['GrainSizeInBed', inBedTmpl, ],
                                            ['LithologicUnitInBed', inBedTmpl, ],
                                            ['SedimentologicUnitInBed', inBedTmpl, ],
                                            ['StratigraphicUnitInBed', inBedTmpl, ],
                                            ['FossilInBed', inBedTmpl, ],
                                            ['BeddingTypeInBed', inBedTmpl, ],
                                            ['BoundaryTypeInBed', inBedTmpl, ],
                                            ['SedimentStructureInBed', inBedTmpl, ],
                                            ['CustomSymbolInBed', inBedTmpl, ],
                                            ['BeddingTypeInBed', inBedTmpl, ],
                                            ['FieldBookEntry', inFieldBookTmpl, ],])
    def setupComboBoxModule(self, module):
        globalTmpl = TemplateFile('templates/Gui/ComboBoxes/GlobalComboBoxTemplate.py')
        inProjectTmpl = TemplateFile('templates/Gui/ComboBoxes/InProjectComboBoxTemplate.py')
        inProfileTmpl = TemplateFile('templates/Gui/ComboBoxes/InProfileComboBoxTemplate.py')
        inBedTmpl = TemplateFile('templates/Gui/ComboBoxes/InBedComboBoxTemplate.py')
        inFieldBookTmpl = TemplateFile('templates/Gui/ComboBoxes/InFieldBookComboBoxTemplate.py')
        self.createComboBoxClasses(module, [['GraphicPrimitive', globalTmpl, ],
                                            ['Project', globalTmpl, ],
                                            ['LengthUnit', globalTmpl, ],        
                                            ['FieldBook', globalTmpl, ],
                                            ['Profile', inProjectTmpl, ],
                                            ['Bed', inProfileTmpl, ],
                                            ['Color', inProjectTmpl, ],
                                            ['OutcropType', inProjectTmpl, ],
                                            ['Facies', inProjectTmpl, ],
                                            ['Lithology', inProjectTmpl, ],
                                            ['TectonicUnitType', inProjectTmpl, ],
                                            ['TectonicUnit', inProjectTmpl, ],
                                            ['GrainSizeType', inProjectTmpl, ],
                                            ['GrainSize', inProjectTmpl, ],
                                            ['LithologicUnitType', inProjectTmpl, ],
                                            ['LithologicUnit', inProjectTmpl, ],
                                            ['SedimentologicUnitType', inProjectTmpl, ],
                                            ['SedimentologicUnit', inProjectTmpl, ],
                                            ['StratigraphicUnitType', inProjectTmpl, ],
                                            ['StratigraphicUnit', inProjectTmpl, ],
                                            ['Fossil', inProjectTmpl, ],
                                            ['BeddingType', inProjectTmpl, ],
                                            ['BoundaryType', inProjectTmpl, ],
                                            ['SedimentStructure', inProjectTmpl, ],
                                            ['CustomSymbol', inProjectTmpl, ],
                                            ['BeddingType', inProjectTmpl, ],
                                            ['ProfileColumn', inProfileTmpl, ],
                                            ['ProfileColumnInProfile', inProfileTmpl, ],
                                            ['ColorInBed', inBedTmpl, ],
                                            ['OutcropTypeInBed', inBedTmpl, ],
                                            ['FaciesInBed', inBedTmpl, ],
                                            ['LithologyInBed', inBedTmpl, ],
                                            ['TectonicUnitInBed', inBedTmpl, ],
                                            ['GrainSizeInBed', inBedTmpl, ],
                                            ['LithologicUnitInBed', inBedTmpl, ],
                                            ['SedimentologicUnitInBed', inBedTmpl, ],
                                            ['StratigraphicUnitInBed', inBedTmpl, ],
                                            ['FossilInBed', inBedTmpl, ],
                                            ['BeddingTypeInBed', inBedTmpl, ],
                                            ['BoundaryTypeInBed', inBedTmpl, ],
                                            ['SedimentStructureInBed', inBedTmpl, ],
                                            ['CustomSymbolInBed', inBedTmpl, ],
                                            ['BeddingTypeInBed', inBedTmpl, ],
                                            ['FieldBookEntry', inFieldBookTmpl, ],])
    def setupFinderModule(self, module):
        globalTmpl = TemplateFile('templates/Logic/Finders/GlobalFinderTemplate.py')
        inProjectTmpl = TemplateFile('templates/Logic/Finders/InProjectFinderTemplate.py')
        inProfileTmpl = TemplateFile('templates/Logic/Finders/InProfileFinderTemplate.py')
        inBedTmpl = TemplateFile('templates/Logic/Finders/InBedFinderTemplate.py')
        inFieldBookTmpl = TemplateFile('templates/Logic/Finders/InFieldBookFinderTemplate.py')
        self.createFinderClasses(module, [['GraphicPrimitive', globalTmpl, ],
                                          ['Project', globalTmpl, ],
                                          ['LengthUnit', globalTmpl, ],
                                          ['Profile', inProjectTmpl, ],
                                          ['ProfileColumn', inProfileTmpl, ],
                                          ['ProfileColumnInProfile', inProfileTmpl, ],
                                          ['Bed', inProfileTmpl, ],
                                          ['Color', inProjectTmpl, ],
                                          ['ColorInBed', inBedTmpl, ],
                                          ['OutcropType', inProjectTmpl, ],
                                          ['OutcropTypeInBed', inBedTmpl, ],
                                          ['Facies', inProjectTmpl, ],
                                          ['FaciesInBed', inBedTmpl, ],
                                          ['Lithology', inProjectTmpl, ],
                                          ['LithologyInBed', inBedTmpl, ],
                                          ['TectonicUnitType', inProjectTmpl, ],
                                          ['TectonicUnit', inProjectTmpl, ],
                                          ['TectonicUnitInBed', inBedTmpl, ],
                                          ['GrainSizeType', inProjectTmpl, ],
                                          ['GrainSize', inProjectTmpl, ],
                                          ['GrainSizeInBed', inBedTmpl, ],
                                          ['LithologicUnitType', inProjectTmpl, ],
                                          ['LithologicUnit', inProjectTmpl, ],
                                          ['LithologicUnitInBed', inBedTmpl, ],
                                          ['SedimentologicUnitType', inProjectTmpl, ],
                                          ['SedimentologicUnit', inProjectTmpl, ],
                                          ['SedimentologicUnitInBed', inBedTmpl, ],
                                          ['StratigraphicUnitType', inProjectTmpl, ],
                                          ['StratigraphicUnit', inProjectTmpl, ],
                                          ['StratigraphicUnitInBed', inBedTmpl, ],
                                          ['Fossil', inProjectTmpl, ],
                                          ['FossilInBed', inBedTmpl, ],
                                          ['BeddingType', inProjectTmpl, ],
                                          ['BeddingTypeInBed', inBedTmpl, ],
                                          ['BoundaryType', inProjectTmpl, ],
                                          ['BoundaryTypeInBed', inBedTmpl, ],
                                          ['SedimentStructure', inProjectTmpl, ],
                                          ['SedimentStructureInBed', inBedTmpl, ],
                                          ['CustomSymbol', inProjectTmpl, ],
                                          ['CustomSymbolInBed', inBedTmpl, ],
                                          ['BeddingType', inProjectTmpl, ],
                                          ['BeddingTypeInBed', inBedTmpl, ],
                                          ['FieldBook', globalTmpl, ],
                                          ['FieldBookEntry', inFieldBookTmpl, ],])
    def setupDataClasses(self, module):
        template = TemplateFile('templates/Logic/Persistance/Entity.py')
        classEntity = module.createClass('Entity', None, None, template=template)
        self.setupLengthUnitClass(module, classEntity, self.database.schema('data').table('length_units'), template)
        self.setupGraphicPrimitiveClass(module, classEntity, self.database.schema('data').table('graphic_primitives'), template)
        self.setupProjectClass(module, classEntity, self.database.schema('data').table('projects'), template)
        self.setupTectonicUnitTypeClass(module, classEntity, self.database.schema('data').table('tectonic_unit_types'), template)
        self.setupTectonicUnitClass(module, classEntity, self.database.schema('data').table('tectonic_units'), template)
        self.setupTectonicUnitInBedClass(module, classEntity, self.database.schema('data').table('tectonic_units_in_beds'), template)
        self.setupGrainSizeTypeClass(module, classEntity, self.database.schema('data').table('grain_size_types'), template)
        self.setupGrainSizeClass(module, classEntity, self.database.schema('data').table('grain_sizes'), template)
        self.setupGrainSizeInBedClass(module, classEntity, self.database.schema('data').table('grain_sizes_in_beds'), template)
        self.setupLithologicUnitTypeClass(module, classEntity, self.database.schema('data').table('lithologic_unit_types'), template)
        self.setupLithologicUnitClass(module, classEntity, self.database.schema('data').table('lithologic_units'), template)
        self.setupLithologicUnitInBedClass(module, classEntity, self.database.schema('data').table('lithologic_units_in_beds'), template)
        self.setupSedimentologicUnitTypeClass(module, classEntity, self.database.schema('data').table('sedimentologic_unit_types'), template)
        self.setupSedimentologicUnitClass(module, classEntity, self.database.schema('data').table('sedimentologic_units'), template)
        self.setupSedimentologicUnitInBedClass(module, classEntity, self.database.schema('data').table('sedimentologic_units_in_beds'), template)
        self.setupStratigraphicUnitTypeClass(module, classEntity, self.database.schema('data').table('stratigraphic_unit_types'), template)
        self.setupStratigraphicUnitClass(module, classEntity, self.database.schema('data').table('stratigraphic_units'), template)
        self.setupStratigraphicUnitInBedClass(module, classEntity, self.database.schema('data').table('stratigraphic_units_in_beds'), template)
        self.setupColorClass(module, classEntity, self.database.schema('data').table('colors'), template)
        self.setupColorInBedClass(module, classEntity, self.database.schema('data').table('colors_in_beds'), template)
        self.setupOutcropTypeClass(module, classEntity, self.database.schema('data').table('outcrop_types'), template)
        self.setupOutcropTypeInBedClass(module, classEntity, self.database.schema('data').table('outcrop_types_in_beds'), template)
        self.setupFaciesClass(module, classEntity, self.database.schema('data').table('facies'), template)
        self.setupFaciesInBedClass(module, classEntity, self.database.schema('data').table('facies_in_beds'), template)
        self.setupLithologyClass(module, classEntity, self.database.schema('data').table('lithologies'), template)
        self.setupLithologyInBedClass(module, classEntity, self.database.schema('data').table('lithologies_in_beds'), template)
        self.setupFossilClass(module, classEntity, self.database.schema('data').table('fossils'), template)
        self.setupFossilInBedClass(module, classEntity, self.database.schema('data').table('fossils_in_beds'), template)
        self.setupBeddingTypeClass(module, classEntity, self.database.schema('data').table('bedding_types'), template)
        self.setupBeddingTypeInBedClass(module, classEntity, self.database.schema('data').table('bedding_types_in_beds'), template)
        self.setupBoundaryTypeClass(module, classEntity, self.database.schema('data').table('boundary_types'), template)
        self.setupBoundaryTypeInBedClass(module, classEntity, self.database.schema('data').table('boundary_types_in_beds'), template)
        self.setupSedimentStructureClass(module, classEntity, self.database.schema('data').table('sediment_structures'), template)
        self.setupSedimentStructureInBedClass(module, classEntity, self.database.schema('data').table('sediment_structures_in_beds'), template)
        self.setupCustomSymbolClass(module, classEntity, self.database.schema('data').table('custom_symbols'), template)
        self.setupCustomSymbolInBedClass(module, classEntity, self.database.schema('data').table('custom_symbols_in_beds'), template)
        self.setupProfileClass(module, classEntity, self.database.schema('data').table('profiles'), template)
        self.setupFieldBookClass(module, classEntity, self.database.schema('data').table('field_books'), template)
        self.setupFieldBookEntryClass(module, classEntity, self.database.schema('data').table('field_book_entries'), template)
        self.setupBedClass(module, classEntity, self.database.schema('data').table('beds'), template)
        self.setupProfileColumnClass(module, classEntity, self.database.schema('data').table('profile_columns'), template)
        self.setupProfileColumnInProfileClass(module, classEntity, self.database.schema('data').table('profile_columns_in_profiles'), template)
    def setupProfileColumnClass(self, module, baseClass, table, template):
        c = module.createClass('ProfileColumn', baseClass, table, createIdField=True, createNameField=True, createDescriptionField=True, template=template)
    def setupProfileColumnInProfileClass(self, module, baseClass, table, template):
        c = module.createClass('ProfileColumnInProfile', baseClass, table, template=template)
        c.createField(table.column('profile_id'), 'profile', backrefName='profileColumns', relationClass='Profile', cascade='all')
        c.createField(table.column('profile_column_id'), 'profileColumn', backrefName='profile', relationClass='ProfileColumn', cascade='all')
        c.createField(table.column('position'), 'position')
        c.addSortOrder(c.field('position'), ascending=True)
    def setupGraphicPrimitiveClass(self, module, baseClass, table, template):
        c = module.createClass('GraphicPrimitive', baseClass, table, createIdField=True, createNameField=True, createDescriptionField=True, template=template)
        c.createField(table.column('svg_data'), 'svgData')
        c.createField(table.column('original_path'), 'originalPath')
    def setupTectonicUnitTypeClass(self, module, baseClass, table, template):
        c = module.createClass('TectonicUnitType', baseClass, table, createIdField=True, createNameField=True, createDescriptionField=True, template=template)
        c.createField(table.column('project_id'), 'project', backrefName='tectonic_unit_types', relationClass='Project', cascade='all')
        c.addSortOrder(c.field('name'), ascending=True)
    def setupTectonicUnitClass(self, module, baseClass, table, template):
        c = module.createClass('TectonicUnit', baseClass, table, createIdField=True, createNameField=True, createDescriptionField=True, template=template)
        c.createField(table.column('project_id'), 'project', backrefName='tectonic_units', relationClass='Project', cascade='all')
        c.createField(table.column('tectonic_unit_type_id'), 'tectonicUnitType', backrefName='tectonicUnits', relationClass='TectonicUnitType', cascade='all')                  
        c.createField(table.column('graphic_primitive_id'), 'graphicPrimitive', backrefName='tectonicUnits', relationClass='GraphicPrimitive', cascade='all')
        c.addSortOrder(c.field('name'), ascending=True)
    def setupTectonicUnitInBedClass(self, module, baseClass, table, template):
        c = module.createClass('TectonicUnitInBed', baseClass, table, createIdField=True, createDescriptionField=True, template=template)
        c.createField(table.column('base'), 'base')
        c.createField(table.column('top'), 'top')
        c.createField(table.column('bed_id'), 'bed', backrefName='tectonic_units', relationClass='Bed', cascade='all')
        c.createField(table.column('tectonic_unit_id'), 'tectonic_unit', backrefName='beds', relationClass='TectonicUnit', cascade='all')
    def setupGrainSizeTypeClass(self, module, baseClass, table, template):
        c = module.createClass('GrainSizeType', baseClass, table, createIdField=True, createNameField=True, createDescriptionField=True, template=template)
        c.createField(table.column('project_id'), 'project', backrefName='grain_size_types', relationClass='Project', cascade='all')
        c.addSortOrder(c.field('name'), ascending=True)
    def setupGrainSizeClass(self, module, baseClass, table, template):
        c = module.createClass('GrainSize', baseClass, table, createIdField=True, createNameField=True, createDescriptionField=True, template=template)
        c.createField(table.column('project_id'), 'project', backrefName='grain_sizes', relationClass='Project', cascade='all')
        c.createField(table.column('grain_size_type_id'), 'grainSizeType', backrefName='grainSizes', relationClass='GrainSizeType', cascade='all')                  
        c.createField(table.column('graphic_primitive_id'), 'graphicPrimitive', backrefName='grainSizes', relationClass='GraphicPrimitive', cascade='all')
        c.createField(table.column('percent_from_max'), 'percentFromMax')
        c.addSortOrder(c.field('name'), ascending=True)
    def setupGrainSizeInBedClass(self, module, baseClass, table, template):
        c = module.createClass('GrainSizeInBed', baseClass, table, createIdField=True, createDescriptionField=True, template=template)
        c.createField(table.column('base'), 'base')
        c.createField(table.column('top'), 'top')
        c.createField(table.column('bed_id'), 'bed', backrefName='grain_sizes', relationClass='Bed', cascade='all')
        c.createField(table.column('grain_size_id'), 'grain_size', backrefName='beds', relationClass='GrainSize', cascade='all')
    def setupSedimentologicUnitTypeClass(self, module, baseClass, table, template):
        c = module.createClass('SedimentologicUnitType', baseClass, table, createIdField=True, createNameField=True, createDescriptionField=True, template=template)
        c.createField(table.column('project_id'), 'project', backrefName='sedimentologic_unit_types', relationClass='Project', cascade='all')
        c.addSortOrder(c.field('name'), ascending=True)
    def setupSedimentologicUnitClass(self, module, baseClass, table, template):
        c = module.createClass('SedimentologicUnit', baseClass, table, createIdField=True, createNameField=True, createDescriptionField=True, template=template)
        c.createField(table.column('project_id'), 'project', backrefName='sedimentologic_units', relationClass='Project', cascade='all')
        c.createField(table.column('sedimentologic_unit_type_id'), 'sedimentologicUnitType', backrefName='sedimentologicUnits', relationClass='SedimentologicUnitType', cascade='all')                  
        c.createField(table.column('graphic_primitive_id'), 'graphicPrimitive', backrefName='sedimentologicUnits', relationClass='GraphicPrimitive', cascade='all')
        c.addSortOrder(c.field('name'), ascending=True)
    def setupSedimentologicUnitInBedClass(self, module, baseClass, table, template):
        c = module.createClass('SedimentologicUnitInBed', baseClass, table, createIdField=True, createDescriptionField=True, template=template)
        c.createField(table.column('base'), 'base')
        c.createField(table.column('top'), 'top')
        c.createField(table.column('bed_id'), 'bed', backrefName='sedimentologic_units', relationClass='Bed', cascade='all')
        c.createField(table.column('sedimentologic_unit_id'), 'sedimentologic_unit', backrefName='beds', relationClass='SedimentologicUnit', cascade='all')
    def setupStratigraphicUnitTypeClass(self, module, baseClass, table, template):
        c = module.createClass('StratigraphicUnitType', baseClass, table, createIdField=True, createNameField=True, createDescriptionField=True, template=template)
        c.createField(table.column('project_id'), 'project', backrefName='stratigraphic_unit_types', relationClass='Project', cascade='all')
        c.addSortOrder(c.field('name'), ascending=True)
    def setupStratigraphicUnitClass(self, module, baseClass, table, template):
        c = module.createClass('StratigraphicUnit', baseClass, table, createIdField=True, createNameField=True, createDescriptionField=True, template=template)
        c.createField(table.column('project_id'), 'project', backrefName='stratigraphic_units', relationClass='Project', cascade='all')
        c.createField(table.column('stratigraphic_unit_type_id'), 'stratigraphicUnitType', backrefName='stratigraphicUnits', relationClass='StratigraphicUnitType', cascade='all')                  
        c.createField(table.column('graphic_primitive_id'), 'graphicPrimitive', backrefName='stratigraphicUnits', relationClass='GraphicPrimitive', cascade='all')
        c.addSortOrder(c.field('name'), ascending=True)
    def setupStratigraphicUnitInBedClass(self, module, baseClass, table, template):
        c = module.createClass('StratigraphicUnitInBed', baseClass, table, createIdField=True, createDescriptionField=True, template=template)
        c.createField(table.column('base'), 'base')
        c.createField(table.column('top'), 'top')
        c.createField(table.column('bed_id'), 'bed', backrefName='stratigraphic_units', relationClass='Bed', cascade='all')
        c.createField(table.column('stratigraphic_unit_id'), 'stratigraphic_unit', backrefName='beds', relationClass='StratigraphicUnit', cascade='all')
    def setupLithologicUnitTypeClass(self, module, baseClass, table, template):
        c = module.createClass('LithologicUnitType', baseClass, table, createIdField=True, createNameField=True, createDescriptionField=True, template=template)
        c.createField(table.column('project_id'), 'project', backrefName='lithologic_unit_types', relationClass='Project', cascade='all')
        c.addSortOrder(c.field('name'), ascending=True)
    def setupLithologicUnitClass(self, module, baseClass, table, template):
        c = module.createClass('LithologicUnit', baseClass, table, createIdField=True, createNameField=True, createDescriptionField=True, template=template)
        c.createField(table.column('project_id'), 'project', backrefName='lithologic_units', relationClass='Project', cascade='all')
        c.createField(table.column('lithologic_unit_type_id'), 'lithologicUnitType', backrefName='lithologicUnits', relationClass='LithologicUnitType', cascade='all')                  
        c.createField(table.column('graphic_primitive_id'), 'graphicPrimitive', backrefName='lithologicUnits', relationClass='GraphicPrimitive', cascade='all')
        c.addSortOrder(c.field('name'), ascending=True)
    def setupLithologicUnitInBedClass(self, module, baseClass, table, template):
        c = module.createClass('LithologicUnitInBed', baseClass, table, createIdField=True, createDescriptionField=True, template=template)
        c.createField(table.column('base'), 'base')
        c.createField(table.column('top'), 'top')
        c.createField(table.column('bed_id'), 'bed', backrefName='lithologic_units', relationClass='Bed', cascade='all')
        c.createField(table.column('lithologic_unit_id'), 'lithologic_unit', backrefName='beds', relationClass='LithologicUnit', cascade='all')
    def setupColorClass(self, module, baseClass, table, template):
        c = module.createClass('Color', baseClass, table, createIdField=True, createNameField=True, createDescriptionField=True, template=template)
        c.createField(table.column('project_id'), 'project', backrefName='colors', relationClass='Project', cascade='all')
        c.createField(table.column('graphic_primitive_id'), 'graphicPrimitive', backrefName='colors', relationClass='GraphicPrimitive', cascade='all')
        c.addSortOrder(c.field('name'), ascending=True)
    def setupColorInBedClass(self, module, baseClass, table, template):
        c = module.createClass('ColorInBed', baseClass, table, createIdField=True, createDescriptionField=True, template=template)
        c.createField(table.column('base'), 'base')
        c.createField(table.column('top'), 'top')
        c.createField(table.column('bed_id'), 'bed', backrefName='colors', relationClass='Bed', cascade='all')
        c.createField(table.column('color_id'), 'color', backrefName='beds', relationClass='Color', cascade='all')
    def setupOutcropTypeClass(self, module, baseClass, table, template):
        c = module.createClass('OutcropType', baseClass, table, createIdField=True, createNameField=True, createDescriptionField=True, template=template)
        c.createField(table.column('project_id'), 'project', backrefName='outcrop_types', relationClass='Project', cascade='all')
        c.createField(table.column('graphic_primitive_id'), 'graphicPrimitive', backrefName='outcrop_types', relationClass='GraphicPrimitive', cascade='all')
        c.addSortOrder(c.field('name'), ascending=True)
    def setupOutcropTypeInBedClass(self, module, baseClass, table, template):
        c = module.createClass('OutcropTypeInBed', baseClass, table, createIdField=True, createDescriptionField=True, template=template)
        c.createField(table.column('base'), 'base')
        c.createField(table.column('top'), 'top')
        c.createField(table.column('bed_id'), 'bed', backrefName='outcrop_types', relationClass='Bed', cascade='all')
        c.createField(table.column('outcrop_type_id'), 'outcrop_type', backrefName='beds', relationClass='OutcropType', cascade='all')
    def setupFaciesClass(self, module, baseClass, table, template):
        c = module.createClass('Facies', baseClass, table, createIdField=True, createNameField=True, createDescriptionField=True, template=template)
        c.createField(table.column('project_id'), 'project', backrefName='facies', relationClass='Project', cascade='all')
        c.createField(table.column('graphic_primitive_id'), 'graphicPrimitive', backrefName='facies', relationClass='GraphicPrimitive', cascade='all')
        c.addSortOrder(c.field('name'), ascending=True)
    def setupFaciesInBedClass(self, module, baseClass, table, template):
        c = module.createClass('FaciesInBed', baseClass, table, createIdField=True, createDescriptionField=True, template=template)
        c.createField(table.column('base'), 'base')
        c.createField(table.column('top'), 'top')
        c.createField(table.column('bed_id'), 'bed', backrefName='facies', relationClass='Bed', cascade='all')
        c.createField(table.column('facies_id'), 'facies', backrefName='beds', relationClass='Facies', cascade='all')
    def setupLithologyClass(self, module, baseClass, table, template):
        c = module.createClass('Lithology', baseClass, table, createIdField=True, createNameField=True, createDescriptionField=True, template=template)
        c.createField(table.column('project_id'), 'project', backrefName='lithologies', relationClass='Project', cascade='all')
        c.createField(table.column('graphic_primitive_id'), 'graphicPrimitive', backrefName='lithologies', relationClass='GraphicPrimitive', cascade='all')
        c.addSortOrder(c.field('name'), ascending=True)
    def setupLithologyInBedClass(self, module, baseClass, table, template):
        c = module.createClass('LithologyInBed', baseClass, table, createIdField=True, createDescriptionField=True, template=template)
        c.createField(table.column('base'), 'base')
        c.createField(table.column('top'), 'top')
        c.createField(table.column('bed_id'), 'bed', backrefName='lithologies', relationClass='Bed', cascade='all')
        c.createField(table.column('lithology_id'), 'lithology', backrefName='beds', relationClass='Lithology', cascade='all')
    def setupFossilClass(self, module, baseClass, table, template):
        c = module.createClass('Fossil', baseClass, table, createIdField=True, createNameField=True, createDescriptionField=True, template=template)
        c.createField(table.column('project_id'), 'project', backrefName='fossils', relationClass='Project', cascade='all')
        c.createField(table.column('graphic_primitive_id'), 'graphicPrimitive', backrefName='fossils', relationClass='GraphicPrimitive', cascade='all')
        c.addSortOrder(c.field('name'), ascending=True)
    def setupFossilInBedClass(self, module, baseClass, table, template):
        c = module.createClass('FossilInBed', baseClass, table, createIdField=True, createDescriptionField=True, template=template)
        c.createField(table.column('base'), 'base')
        c.createField(table.column('top'), 'top')
        c.createField(table.column('bed_id'), 'bed', backrefName='fossils', relationClass='Bed', cascade='all')
        c.createField(table.column('fossil_id'), 'fossil', backrefName='beds', relationClass='Fossil', cascade='all')
    def setupBeddingTypeClass(self, module, baseClass, table, template):
        c = module.createClass('BeddingType', baseClass, table, createIdField=True, createNameField=True, createDescriptionField=True, template=template)
        c.createField(table.column('project_id'), 'project', backrefName='beddingTypes', relationClass='Project', cascade='all')
        c.createField(table.column('graphic_primitive_id'), 'graphicPrimitive', backrefName='beddingTypes', relationClass='GraphicPrimitive', cascade='all')
        c.addSortOrder(c.field('name'), ascending=True)
    def setupBeddingTypeInBedClass(self, module, baseClass, table, template):
        c = module.createClass('BeddingTypeInBed', baseClass, table, createIdField=True, createDescriptionField=True, template=template)
        c.createField(table.column('base'), 'base')
        c.createField(table.column('top'), 'top')
        c.createField(table.column('bed_id'), 'bed', backrefName='colors', relationClass='Bed', cascade='all')
        c.createField(table.column('bedding_type_id'), 'beddingType', backrefName='beds', relationClass='BeddingType', cascade='all')
    def setupBoundaryTypeClass(self, module, baseClass, table, template):
        c = module.createClass('BoundaryType', baseClass, table, createIdField=True, createNameField=True, createDescriptionField=True, template=template)
        c.createField(table.column('project_id'), 'project', backrefName='boundaryTypes', relationClass='Project', cascade='all')
        c.createField(table.column('graphic_primitive_id'), 'graphicPrimitive', backrefName='boundaryTypes', relationClass='GraphicPrimitive', cascade='all')
        c.addSortOrder(c.field('name'), ascending=True)
    def setupBoundaryTypeInBedClass(self, module, baseClass, table, template):
        c = module.createClass('BoundaryTypeInBed', baseClass, table, createIdField=True, createDescriptionField=True, template=template)
        c.createField(table.column('base'), 'base')
        c.createField(table.column('top'), 'top')
        c.createField(table.column('bed_id'), 'bed', backrefName='colors', relationClass='Bed', cascade='all')
        c.createField(table.column('boundary_type_id'), 'boundaryType', backrefName='beds', relationClass='BoundaryType', cascade='all')
    def setupSedimentStructureClass(self, module, baseClass, table, template):
        c = module.createClass('SedimentStructure', baseClass, table, createIdField=True, createNameField=True, createDescriptionField=True, template=template)
        c.createField(table.column('project_id'), 'project', backrefName='sedimentStructures', relationClass='Project', cascade='all')
        c.createField(table.column('graphic_primitive_id'), 'graphicPrimitive', backrefName='sedimentStructures', relationClass='GraphicPrimitive', cascade='all')
        c.addSortOrder(c.field('name'), ascending=True)
    def setupSedimentStructureInBedClass(self, module, baseClass, table, template):
        c = module.createClass('SedimentStructureInBed', baseClass, table, createIdField=True, createDescriptionField=True, template=template)
        c.createField(table.column('base'), 'base')
        c.createField(table.column('top'), 'top')
        c.createField(table.column('bed_id'), 'bed', backrefName='colors', relationClass='Bed', cascade='all')
        c.createField(table.column('sediment_structure_id'), 'sedimentStructure', backrefName='beds', relationClass='SedimentStructure', cascade='all')
    def setupCustomSymbolClass(self, module, baseClass, table, template):
        c = module.createClass('CustomSymbol', baseClass, table, createIdField=True, createNameField=True, createDescriptionField=True, template=template)
        c.createField(table.column('project_id'), 'project', backrefName='customSymbols', relationClass='Project', cascade='all')
        c.createField(table.column('graphic_primitive_id'), 'graphicPrimitive', backrefName='customSymbols', relationClass='GraphicPrimitive', cascade='all')
        c.addSortOrder(c.field('name'), ascending=True)
    def setupCustomSymbolInBedClass(self, module, baseClass, table, template):
        c = module.createClass('CustomSymbolInBed', baseClass, table, createIdField=True, createDescriptionField=True, template=template)
        c.createField(table.column('base'), 'base')
        c.createField(table.column('top'), 'top')
        c.createField(table.column('bed_id'), 'bed', backrefName='colors', relationClass='Bed', cascade='all')
        c.createField(table.column('custom_symbol_id'), 'customSymbol', backrefName='beds', relationClass='CustomSymbol', cascade='all')
    def setupLengthUnitClass(self, module, baseClass, table, template):
        c = module.createClass('LengthUnit', baseClass, table, createIdField=True, createNameField=True, createDescriptionField=True, template=template)
        c.createField(table.column('micro_metres'), 'microMetres')
    def setupBedClass(self, module, baseClass, table, template):
        c = module.createClass('Bed', baseClass, table, template=template)
        c.createField(table.column('id'), 'id')
        c.createField(table.column('position'), 'position')
        c.createField(table.column('bed_number'), 'bedNumber')
        c.createField(table.column('profile_id'), 'profile', backrefName='beds', relationClass='Profile', cascade='all')
        c.createField(table.column('height'), 'height')
        c.createField(table.column('height_length_unit_id'), 'heightLenghtUnit', relationClass='LengthUnit', cascade='all')
    def setupFieldBookEntryClass(self, module, baseClass, table, template):
        c = module.createClass('FieldBookEntry', baseClass, table, template=template)
        c.createField(table.column('id'), 'id')
        c.createField(table.column('field_book_id'), 'fieldBook', backrefName='entries', relationClass='FieldBook', cascade='all')
    def setupFieldBookClass(self, module, baseClass, table, template):
        c = module.createClass('FieldBook', baseClass, table, createIdField=True, createDescriptionField=True, template=template)
        c.createField(table.column('title'), 'title')
        c.addSortOrder(c.field('title'), ascending=True)
    def setupColorClass(self, module, baseClass, table, template):
        c = module.createClass('Color', baseClass, table, createIdField=True, createNameField=True, createDescriptionField=True, template=template)
        c.createField(table.column('project_id'), 'project', backrefName='colors', relationClass='Project', cascade='all')
        c.createField(table.column('graphic_primitive_id'), 'graphicPrimitive', backrefName='colors', relationClass='GraphicPrimitive', cascade='all')
        c.addSortOrder(c.field('name'), ascending=True)
    def setupProjectClass(self, module, baseClass, table, template):
        c = module.createClass('Project', baseClass, table, createIdField=True, createNameField=True, createDescriptionField=True, template=template)
        c.addSortOrder(c.field('name'), ascending=True)
    def setupProfileClass(self, module, baseClass, table, template):
        c = module.createClass('Profile', baseClass, table, createIdField=True, createNameField=True, createDescriptionField=True, template=template)
        c.createField(table.column('project_id'), 'project', backrefName='profiles', relationClass='Project', cascade='all')
        c.addSortOrder(c.field('name'), ascending=True)
