"""
Boilerplate comment
"""

from Entity import *


class LithologicUnitInBed(Entity):
    def __init__(self, id=None, description='', base=0, top=100, bed=None, lithologic_unit=None):
        Entity.__init__(self)
        self.id = id
        self.description = description
        self.base = base
        self.top = top
        self.bed = bed
        self.lithologic_unit = lithologic_unit
