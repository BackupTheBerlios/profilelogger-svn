from Entity import *
from Sequence import *
from Table import *

class Schema(Entity):
    def __init__(self, database, name):
        Entity.__init__(self, name)
        self.database = database
        self.sequences = {}
        self.tables = {}
    def createSequence(self, name):
        self.sequences[name] = Sequence(self, name)
        return self.sequence(name)
    def sequence(self, name):
        return self.sequences[name]
    def createTable(self, name,  
                    hasIdColumn=True, 
                    hasNameColumn=False, nameColumnIsUnique=False, 
                    hasDescriptionColumn=False):
        self.tables[name] = Table(self, name, 
                                  hasIdColumn=hasIdColumn, 
                                  hasNameColumn=hasNameColumn, 
                                  nameColumnIsUnique=nameColumnIsUnique, 
                                  hasDescriptionColumn=hasDescriptionColumn)
        return self.table(name)
    def table(self, name):
        return self.tables[name]
