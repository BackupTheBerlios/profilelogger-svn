"""
Boilerplate comment
"""

from Entity import *


class FieldBook(Entity):
    def __init__(self, id=None, description='', title='new field book'):
        Entity.__init__(self)
        self.id = id
        self.description = description
        self.title = title
