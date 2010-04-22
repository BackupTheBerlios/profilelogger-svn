from Model import *
from DataType import *
from Database import *
from Schema import *
from Table import *
from Sequence import *
from PrimaryKey import *
from UniqueConstraint import *
from ForeignKey import *
from NotEmptyConstraint import *

class Debugger(object):
    def __init__(self):
        pass
    def debug(self, model):
        ret = []
        ret.append(model.__str__())
        for dt in model.dataTypes.values():
            ret.append('\tData Type: %s' % dt.name)
        ret.append('Database: %s' % model.database.name)
        for schema in model.database.schemas.values():
            ret.append('\tSchema: %s' % schema.name)
            for sequence in schema.sequences.values():
                ret.append('\t\tSequence: %s' % sequence.name)
            for table in schema.tables.values():
                ret.append('\t\tTable: %s' % table.name)
                for col in table.columns.values():
                    ret.append('\t\t\tColumn: %s Type: %s nullable: %s Sequence: %s Default Value: %s, Default Text: "%s", Referenced Column: %s' % (col.name, 
                                                                                                                                                     col.dataType.name, 
                                                                                                                                                     col.nullable, 
                                                                                                                                                     col.sequence,
                                                                                                                                                     col.defaultValue,
                                                                                                                                                     col.defaultText,
                                                                                                                                                     col.referencedColumn))
                ret.append('\t\t\tPrimary Key: %s Column: %s.%s' % (table.primaryKey.name, table.primaryKey.column.table.name, table.primaryKey.column.name))
                for unique in table.uniqueConstraints.values():
                    cols = ''
                    for col in unique.columns:
                        cols += '%s ' % col.name
                    ret.append('\t\t\tUnique: %s Columns: %s' % (unique.name, cols))
                for notEmpty in table.notEmptyConstraints.values():
                    ret.append('\t\t\tNot Empty: %s Column: %s' % (notEmpty.name, notEmpty.column.name))
                for fk in table.foreignKeys.values():
                    ret.append('\t\t\tForeign Key: %s Local Column: %s Referenced Column: %s.%s.%s' % (fk.name,
                                                                                                       fk.localColumn.name,
                                                                                                       fk.referencedColumn.table.schema.name,
                                                                                                       fk.referencedColumn.table.name,
                                                                                                       fk.referencedColumn.name))
        for pm in model.pythonModules.values():
            self.addPythonModulesAsStrings(pm, ret)

        for row in ret:
            print row
    def addPythonModulesAsStrings(self, pythonModule, ret):
        ret.append('Python Module: %s' % pythonModule)
        for c in pythonModule.classes.values():
            ret.append('Python Class: %s derived from %s' % (c, c.parentClass))
            for field in c.fields:
                ret.append('\tField: %s Table Column: %s.%s.%s' % (field.fieldName, 
                                                                   field.tableColumn.table.schema.name, field.tableColumn.table.name, field.tableColumn))
        for pm in pythonModule.pythonModules.values():
            self.addPythonModulesAsStrings(pm, ret)
