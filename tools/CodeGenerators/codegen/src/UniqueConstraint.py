from TableConstraint import *

class UniqueConstraint(TableConstraint):
    def __init__(self, table, name, columns=[]):
        TableConstraint.__init__(self, table, name)
        self.columns = columns
