from TableConstraint import *

class NotEmptyConstraint(TableConstraint):
    def __init__(self, table, name, column):
        TableConstraint.__init__(self, table, name)
        self.column = column
