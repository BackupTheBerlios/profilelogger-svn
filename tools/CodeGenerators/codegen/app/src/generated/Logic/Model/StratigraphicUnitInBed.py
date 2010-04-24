"""
Boilerplate comment
"""

from Entity import *


class StratigraphicUnitInBed(Entity):
    def __init__(self, id=None, description='', base=0, top=100, bed=None, stratigraphic_unit=None):
        Entity.__init__(self)
        self.id = id
        self.description = description
        self.base = base
        self.top = top
        self.bed = bed
        self.stratigraphic_unit = stratigraphic_unit
