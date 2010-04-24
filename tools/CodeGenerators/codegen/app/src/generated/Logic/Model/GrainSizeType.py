"""
Boilerplate comment
"""

from Entity import *


class GrainSizeType(Entity):
    def __init__(self, id=None, name='new item', description='', project=None):
        Entity.__init__(self)
        self.id = id
        self.name = name
        self.description = description
        self.project = project
