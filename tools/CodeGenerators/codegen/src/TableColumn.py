from Entity import *
from Sequence import *
from ForeignKey import *
from PrimaryKey import *
from NotEmptyConstraint import *
from UniqueConstraint import *

class TableColumn(Entity):
    def __init__(self, table, name, 
                 type=None, nullable=False, sequence=None, 
                 defaultValue=None, defaultText=None, 
                 primaryKey=False, 
                 referencedColumn=None, 
                 notEmpty=False, isUnique=False):
        Entity.__init__(self, name)
        self.table = table
        self.dataType = type
        self.nullable = nullable
        self.sequence = sequence
        self.defaultValue = defaultValue
        self.defaultText = defaultText
        self.primaryKey = primaryKey
        self.referencedColumn = referencedColumn
        if self.primaryKey:
            self.createPrimaryKey()
        if self.referencedColumn is not None:
            self.createForeignKey()
        if notEmpty:
            self.createNotEmptyConstraint()
        if isUnique:
            self.createUniqueConstraint()
    def __str__(self):
        return '%s.%s' % (self.table, self.name)
    def hasSequence(self):
        return self.sequence is not None
    def hasDefaultValue(self):
        return self.defaultValue is not None
    def hasDefaultText(self):
        return self.defaultText is not None
    def createForeignKey(self):
        self.table.createForeignKey('fk_%s_%s_entry_exists' % (self.table.name, self.referencedColumn.table.name),
                                    self, self.referencedColumn)
    def createPrimaryKey(self):
        self.table.createPrimaryKey('pk_%s' % self.table.name, self)
    def createNotEmptyConstraint(self):
        self.table.createNotEmptyConstraint('chk_%s_%s_not_empty' % (self.table.name, self.name), self)
    def createUniqueConstraint(self):
        self.table.createUniqueConstraint('u_%s_%s' % (self.table.name, self.name), [self,])
