from Entity import *
from TableColumn import *
from PrimaryKey import *
from UniqueConstraint import *
from NotEmptyConstraint import *
from ForeignKey import *
from RangeCheckConstraint import *

class Table(Entity):
    def __init__(self, schema, name, 
                 hasIdColumn=True, 
                 hasNameColumn=False, 
                 nameColumnIsUnique=False, 
                 hasDescriptionColumn=False):
        Entity.__init__(self, name)
        self.columns = {}
        self.schema = schema
        self.uniqueConstraints = {}
        self.notEmptyConstraints = {}
        self.rangeCheckConstraints = {}
        self.foreignKeys = {}
        self.primaryKey=None
        if hasIdColumn:
            self.createIdColumn('seq_%s' % self.name)
        if hasNameColumn:
            self.createNameColumn()
        if nameColumnIsUnique:
            self.createUniqueConstraintOnNameColumn()
        if hasDescriptionColumn:
            self.createDescriptionColumn()
    def createColumn(self, name, dataType=None, nullable=False, 
                     sequence=None, defaultValue=None, 
                     defaultText=None, primaryKey=False, 
                     referencedColumn=None, notEmpty=False, isUnique=False):
        self.columns[name] = TableColumn(self, name, dataType, nullable, 
                                         sequence, defaultValue, defaultText, 
                                         primaryKey, referencedColumn, 
                                         notEmpty, isUnique)
        return self.column(name)
    def column(self, name):
        return self.columns[name]
    def createPrimaryKey(self, name, column):
        self.primaryKey = PrimaryKey(self, name, column)
    def hasPrimaryKey(self):
        return self.primaryKey is not None
    def createUniqueConstraint(self, name, columns):
        self.uniqueConstraints[name] = UniqueConstraint(self, name, columns)
        return self.uniqueConstraint(name)
    def createRangeCheckConstraint(self, name, column, min, max):
        self.rangeCheckConstraints[name] = RangeCheckConstraint(self,
                                                                column,
                                                                name,
                                                                min,
                                                                max)
    def uniqueConstraint(self, name):
        return self.uniqueConstraints[name]
    def createNotEmptyConstraint(self, name, columns):
        self.notEmptyConstraints[name] = NotEmptyConstraint(self, name, columns)
        return self.notEmptyConstraint(name)
    def notEmptyConstraint(self, name):
        return self.notEmptyConstraints[name]
    def createForeignKey(self, name, localColumn, referencedColumn):
        self.foreignKeys[name] = ForeignKey(self, name, localColumn, referencedColumn)
        return self.foreignKey(name)
    def foreignKey(self, name):
        return self.foreignKeys[name]
    def createIdColumn(self, sequenceName):
        self.createColumn('id', self.schema.database.model.dataType('Integer'), sequence=self.schema.createSequence(sequenceName), primaryKey=True, nullable=False)
    def createNameColumn(self):
        self.createColumn('name', self.schema.database.model.dataType('Unicode'), 
                          nullable=False, 
                          notEmpty=True, 
                          defaultText='new item')
    def createUniqueConstraintOnNameColumn(self):
        self.createUniqueConstraint('u_%s_name' % self.name, [self.column('name'),])
    def createDescriptionColumn(self):
        self.createColumn('description', self.schema.database.model.dataType('Unicode'), nullable=False, defaultText='')
