"""
Boilerplate comment
"""

from Entity import *


class ProfileColumn(Entity):
    def __init__(self, id=None, name='new item', description=''):
        Entity.__init__(self)
        self.id = id
        self.name = name
        self.description = description
