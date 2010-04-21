from Entity import *

class DataType(Entity):
    def __init__(self, model, name):
        Entity.__init__(self, name)
        self.model = model
    def sqlAlchemyName(self):
        return self.name
