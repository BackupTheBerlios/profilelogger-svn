from TableConstraint import *

class PrimaryKey(TableConstraint):
    def __init__(self, table, name, column=None):
        TableConstraint.__init__(self, table, name)
        self.column = column
