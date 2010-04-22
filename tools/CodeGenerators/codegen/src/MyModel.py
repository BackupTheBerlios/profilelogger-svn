from Model import *
from DataType import *

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
        self.setupTableProjects(s)
        self.setupTableLengthUnits(s)
        self.setupTableProfiles(s)
        self.setupTableBeds(s)
        self.setupTableColors(s)
        self.setupTableColorsInBed(s)
        self.setupTableBeddingTypes(s)
        self.setupTableBeddingTypesInBed(s)
        self.setupTableFieldBooks(s)
        self.setupTableFieldBookEntries(s)
    def setupTableGraphicPrimitives(self, s):
        t = s.createTable('graphic_primitives', hasNameColumn=True, nameColumnIsUnique=True, hasDescriptionColumn=True)
        t.createColumn('svg_data', self.dataType('Unicode'), nullable=False, defaultText='')
        t.createColumn('original_path', self.dataType('Unicode'), nullable=False, defaultText='')
    def setupTableColors(self, s):
        t = s.createTable('colors', hasNameColumn=True, nameColumnIsUnique=True, hasDescriptionColumn=True)
        t.createColumn('project_id', nullable=False, referencedColumn=s.table('projects').column('id'))
        t.createColumn('graphic_primitive_id', nullable=False, referencedColumn=s.table('graphic_primitives').column('id'))
        t.createUniqueConstraint('u_colors_name', [t.column('name')])
    def setupTableColorsInBed(self, s):
        t = s.createTable('colors_in_beds', hasDescriptionColumn=True)
        t.createColumn('base', self.dataType('Integer'), nullable=False, defaultValue=0)
        t.createColumn('top', self.dataType('Integer'), nullable=False, defaultValue=100)
        t.createColumn('bed_id', nullable=False, referencedColumn=s.table('beds').column('id'))
        t.createColumn('color_id', nullable=False, referencedColumn=s.table('colors').column('id'))
        t.createRangeCheckConstraint('chk_colors_in_beds_base_in_range', t.column('base'), 0, 100)
        t.createRangeCheckConstraint('chk_colors_in_beds_top_in_range', t.column('top'), 0, 100)
    def setupTableBeddingTypes(self, s):
        t = s.createTable('bedding_types', hasNameColumn=True, nameColumnIsUnique=True, hasDescriptionColumn=True)
        t.createColumn('project_id', nullable=False, referencedColumn=s.table('projects').column('id'))
        t.createColumn('graphic_primitive_id', nullable=False, referencedColumn=s.table('graphic_primitives').column('id'))
        t.createUniqueConstraint('u_bedding_types_name', [t.column('name')])
    def setupTableBeddingTypesInBed(self, s):
        t = s.createTable('bedding_types_in_beds', hasDescriptionColumn=True)
        t.createColumn('base', self.dataType('Integer'), nullable=False, defaultValue=0)
        t.createColumn('top', self.dataType('Integer'), nullable=False, defaultValue=100)
        t.createColumn('bed_id', nullable=False, referencedColumn=s.table('beds').column('id'))
        t.createColumn('bedding_type_id', nullable=False, referencedColumn=s.table('bedding_types').column('id'))
        t.createRangeCheckConstraint('chk_bedding_types_in_beds_base_in_range', t.column('base'), 0, 100)
        t.createRangeCheckConstraint('chk_bedding_types_in_beds_top_in_range', t.column('top'), 0, 100)
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
        model = self.createPythonModule('Model')
        classEntity = model.createClass('Entity', None, None)
        self.setupLengthUnitClass(model, classEntity, self.database.schema('data').table('length_units'))
        self.setupGraphicPrimitiveClass(model, classEntity, self.database.schema('data').table('graphic_primitives'))
        self.setupProjectClass(model, classEntity, self.database.schema('data').table('projects'))
        self.setupColorClass(model, classEntity, self.database.schema('data').table('colors'))
        self.setupColorInBedClass(model, classEntity, self.database.schema('data').table('colors_in_beds'))
        self.setupBeddingTypeClass(model, classEntity, self.database.schema('data').table('bedding_types'))
        self.setupBeddingTypeInBedClass(model, classEntity, self.database.schema('data').table('bedding_types_in_beds'))
        self.setupProfileClass(model, classEntity, self.database.schema('data').table('profiles'))
        self.setupFieldBookClass(model, classEntity, self.database.schema('data').table('field_books'))
        self.setupFieldBookEntryClass(model, classEntity, self.database.schema('data').table('field_book_entries'))
        self.setupBedClass(model, classEntity, self.database.schema('data').table('beds'))
    def setupGraphicPrimitiveClass(self, module, baseClass, table):
        c = module.createClass('GraphicPrimitive', baseClass, table, createIdField=True, createNameField=True, createDescriptionField=True)
        c.createField(table.column('svg_data'), 'svgData')
        c.createField(table.column('original_path'), 'originalPath')
    def setupColorClass(self, module, baseClass, table):
        c = module.createClass('Color', baseClass, table, createIdField=True, createNameField=True, createDescriptionField=True)
        c.createField(table.column('project_id'), 'project', backrefName='colors', relationClass='Project', cascade='all')
        c.createField(table.column('graphic_primitive_id'), 'graphicPrimitive', backrefName='colors', relationClass='GraphicPrimitive', cascade='all')
        c.addSortOrder(c.field('name'), ascending=True)
    def setupColorInBedClass(self, module, baseClass, table):
        c = module.createClass('ColorInBed', baseClass, table, createIdField=True, createDescriptionField=True)
        c.createField(table.column('base'), 'base')
        c.createField(table.column('top'), 'top')
        c.createField(table.column('bed_id'), 'bed', backrefName='colors', relationClass='Bed', cascade='all')
        c.createField(table.column('color_id'), 'color', backrefName='beds', relationClass='Color', cascade='all')
    def setupBeddingTypeClass(self, module, baseClass, table):
        c = module.createClass('BeddingType', baseClass, table, createIdField=True, createNameField=True, createDescriptionField=True)
        c.createField(table.column('project_id'), 'project', backrefName='beddingTypes', relationClass='Project', cascade='all')
        c.createField(table.column('graphic_primitive_id'), 'graphicPrimitive', backrefName='beddingTypes', relationClass='GraphicPrimitive', cascade='all')
        c.addSortOrder(c.field('name'), ascending=True)
    def setupBeddingTypeInBedClass(self, module, baseClass, table):
        c = module.createClass('BeddingTypeInBed', baseClass, table, createIdField=True, createDescriptionField=True)
        c.createField(table.column('base'), 'base')
        c.createField(table.column('top'), 'top')
        c.createField(table.column('bed_id'), 'bed', backrefName='colors', relationClass='Bed', cascade='all')
        c.createField(table.column('bedding_type_id'), 'beddingType', backrefName='beds', relationClass='BeddingType', cascade='all')
    def setupLengthUnitClass(self, module, baseClass, table):
        c = module.createClass('LengthUnit', baseClass, table, createIdField=True, createNameField=True, createDescriptionField=True)
        c.createField(table.column('micro_metres'), 'microMetres')
    def setupBedClass(self, module, baseClass, table):
        c = module.createClass('Bed', baseClass, table)
        c.createField(table.column('id'), 'id')
        c.createField(table.column('position'), 'position')
        c.createField(table.column('bed_number'), 'bedNumber')
        c.createField(table.column('profile_id'), 'profile', backrefName='beds', relationClass='Profile', cascade='all')
        c.createField(table.column('height'), 'height')
        c.createField(table.column('height_length_unit_id'), 'heightLenghtUnit', relationClass='LengthUnit', cascade='all')
    def setupFieldBookEntryClass(self, module, baseClass, table):
        c = module.createClass('FieldBookEntry', baseClass, table)
        c.createField(table.column('id'), 'id')
        c.createField(table.column('field_book_id'), 'fieldBook', backrefName='entries', relationClass='FieldBook', cascade='all')
    def setupFieldBookClass(self, module, baseClass, table):
        c = module.createClass('FieldBook', baseClass, table, createIdField=True, createDescriptionField=True)
        c.createField(table.column('title'), 'title')
        c.addSortOrder(c.field('title'), ascending=True)
    def setupColorClass(self, module, baseClass, table):
        c = module.createClass('Color', baseClass, table, createIdField=True, createNameField=True, createDescriptionField=True)
        c.createField(table.column('project_id'), 'project', backrefName='colors', relationClass='Project', cascade='all')
        c.createField(table.column('graphic_primitive_id'), 'graphicPrimitive', backrefName='colors', relationClass='GraphicPrimitive', cascade='all')
        c.addSortOrder(c.field('name'), ascending=True)
    def setupProjectClass(self, module, baseClass, table):
        c = module.createClass('Project', baseClass, table, createIdField=True, createNameField=True, createDescriptionField=True)
        c.addSortOrder(c.field('name'), ascending=True)
    def setupProfileClass(self, module, baseClass, table):
        c = module.createClass('Profile', baseClass, table, createIdField=True, createNameField=True, createDescriptionField=True)
        c.createField(table.column('project_id'), 'project', backrefName='profiles', relationClass='Project', cascade='all')
        c.addSortOrder(c.field('name'), ascending=True)