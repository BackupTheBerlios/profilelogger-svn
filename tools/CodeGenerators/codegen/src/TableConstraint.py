from Constraint import *

class TableConstraint(Constraint):
    def __init__(self, table, name):
        Constraint.__init__(self, name)
        self.table = table
