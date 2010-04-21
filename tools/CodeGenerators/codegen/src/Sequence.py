from Entity import *

class Sequence(Entity):
    def __init__(self, schema, name):
        Entity.__init__(self, name)
        self.schema = schema
