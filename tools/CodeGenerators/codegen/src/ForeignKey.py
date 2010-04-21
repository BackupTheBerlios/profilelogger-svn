from TableConstraint import *

class ForeignKey(TableConstraint):
    def __init__(self, table, name, localColumn, referencedColumn):
        TableConstraint.__init__(self, table, name)
        self.localColumn = localColumn
        self.referencedColumn = referencedColumn
