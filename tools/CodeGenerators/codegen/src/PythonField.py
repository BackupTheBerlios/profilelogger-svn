class PythonField:
    def __init__(self, pythonClass, tableColumn, fieldName, backrefName=None, relationClass=None, cascade='all'):
        self.pythonClass = pythonClass
        self.tableColumn = tableColumn
        self.fieldName = fieldName
        self.backrefName = backrefName
        self.relationClass = relationClass
        self.cascade = cascade
    def hasCascadeRule(self):
        return self.cascade is not None
    def hasBackrefName(self):
        return self.backrefName is not None
