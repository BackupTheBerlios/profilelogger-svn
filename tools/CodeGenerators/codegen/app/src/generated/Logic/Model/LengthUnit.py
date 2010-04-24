"""
Boilerplate comment
"""

from Entity import *


class LengthUnit(Entity):
    def __init__(self, id=None, name='new item', description='', microMetres=0):
        Entity.__init__(self)
        self.id = id
        self.name = name
        self.description = description
        self.microMetres = microMetres
