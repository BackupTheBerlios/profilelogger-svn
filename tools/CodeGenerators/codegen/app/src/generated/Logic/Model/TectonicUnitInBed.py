"""
Boilerplate comment
"""

from Entity import *


class TectonicUnitInBed(Entity):
    def __init__(self, id=None, description='', base=0, top=100, bed=None, tectonic_unit=None):
        Entity.__init__(self)
        self.id = id
        self.description = description
        self.base = base
        self.top = top
        self.bed = bed
        self.tectonic_unit = tectonic_unit
