from TableConstraint import *

class RangeCheckConstraint(TableConstraint):
    def __init__(self, table, column, name, min, max):
        TableConstraint.__init__(self, table, name)
        self.column = column
        self.min = min
        self.max = max
