from PythonEntity import *
from PythonField import *
from PythonClassSorting import *

class PythonClass(PythonEntity):
    def __init__(self, module, parentClass, name, table, sorting=[]):
        PythonEntity.__init__(self, module, name)
        self.parentClass = parentClass
        self.fields = []
        self.table = table
        self.sorting = []
    def field(self, name):
        for f in self.fields:
            if f.fieldName == name:
                return f
        return None
    def addSortOrder(self, field, ascending=True):
        self.sorting.append(PythonClassSorting(field, ascending))
    def hasTable(self):
        return self.table is not None
    def __str__(self):
        if self.parent is not None:
            return '%s.%s' % (self.parent, self.name)
        else:
            return self.name
    def createField(self, tableColumn, propertyName, backrefName=None, relationClass=None, cascade='all'):
        self.fields.append(PythonField(self, tableColumn, propertyName, backrefName, relationClass, cascade))
    def hasParentClass(self):
        return self.parentClass is not None
