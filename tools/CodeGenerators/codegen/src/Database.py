from Entity import *
from Schema import *

class Database(Entity):
    def __init__(self, model, name):
        Entity.__init__(self, name)
        self.model = model
        self.schemas = {}
    def createSchema(self, name):
        self.schemas[name] = Schema(self, name)
        return self.schema(name)
    def schema(self, name):
        return self.schemas[name]
