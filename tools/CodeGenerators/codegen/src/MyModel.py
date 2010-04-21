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
        self.setupTableProjects(s)
        self.setupTableProfiles(s)
        self.setupTableColors(s)
    def setupTableProjects(self, s):
        t = s.createTable('projects')
        t.createColumn('id', self.dataType('Integer'), sequence=s.createSequence('seq_projects'), primaryKey=True)
        t.createColumn('name', self.dataType('Unicode'), defaultText='new project', notEmpty=True, isUnique=True)
        t.createColumn('description', self.dataType('Unicode'), defaultText='')


    def setupTableColors(self, s):
        t = s.createTable('colors')
        t.createColumn('id', self.dataType('Integer'), sequence=s.createSequence('seq_colors'), primaryKey=True)
        t.createColumn('name', self.dataType('Unicode'), defaultText='new color', notEmpty=True, isUnique=True)
        t.createColumn('description', self.dataType('Unicode'), defaultText='')
        t.createUniqueConstraint('u_colors_name', [t.column('name')])
    def setupTableProfiles(self, s):
        t = s.createTable('profiles')
        t.createColumn('id', self.dataType('Integer'), sequence=s.createSequence('seq_profiles'), primaryKey=True)
        t.createColumn('project_id', s.table('projects').column('id').dataType, nullable=False, referencedColumn=s.table('projects').column('id'))
        t.createColumn('name', self.dataType('Unicode'), nullable=False, defaultText='new profile', notEmpty=True)
        t.createColumn('description', self.dataType('Unicode'), defaultText='')
        t.createUniqueConstraint('u_profile_name_in_project', [t.column('project_id'), t.column('name'),])
    def setupPythonModules(self):
        model = self.createPythonModule('Model')
        classEntity = model.createClass('Entity', None, None)
        self.setupColorClass(model, classEntity, self.database.schema('data').table('colors'))
        self.setupProjectClass(model, classEntity, self.database.schema('data').table('projects'))
        self.setupProfileClass(model, classEntity, self.database.schema('data').table('profiles'))
    def setupColorClass(self, module, baseClass, table):
        c = module.createClass('Color', baseClass, table)
        c.createField(table.column('id'), 'id')
        c.createField(table.column('name'), 'name')
        c.createField(table.column('description'), 'description')
        c.addSortOrder(c.field('name'), ascending=True)

    def setupProjectClass(self, module, baseClass, table):
        c = module.createClass('Project', baseClass, table)
        c.createField(table.column('id'), 'id')
        c.createField(table.column('name'), 'name')
        c.createField(table.column('description'), 'description')
        c.addSortOrder(c.field('name'), ascending=True)
    def setupProfileClass(self, module, baseClass, table):
        c = module.createClass('Profile', baseClass, table)
        c.createField(table.column('project_id'), 'project', backrefName='profiles', relationClass='Project', cascade='all')
        c.createField(table.column('id'), 'id')
        c.createField(table.column('name'), 'name')
        c.createField(table.column('description'), 'description')
        c.addSortOrder(c.field('name'), ascending=True)
